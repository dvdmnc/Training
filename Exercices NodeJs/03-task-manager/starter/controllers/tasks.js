const Task = require('../models/Task')
const asyncWrapper = require('../middleware/async')
const {createCustomError} = require('../errors/custom-error')

const getAllTasks = asyncWrapper(async (req,res) => {
    const Tasks = await Task.find({})
    res.status(200).json({Tasks})
})

const createTask =asyncWrapper(async (req,res) => {
        const task = await Task.create(req.body)
        res.status(201).json({task})
})

const getTask = asyncWrapper(async (req,res,next) => {
        const task = await Task.findOne({_id:req.params.id})
        if(!task){
            return next(createCustomError('No task with id: ' + req.params.id, 404))
        }
        res.status(200).json({task})
})

const updateTask = asyncWrapper(async (req,res,next) => {
    if (req.body.name.length == 0){
        return res.status(500).json({msg:'Name should not be empty'})
    }
        const task = await Task.findOneAndUpdate({_id:req.params.id},req.body,{returnDocument:'after'})
        if(!task){
            return next(createCustomError('No task with id: ' + req.params.id, 404))
        }
        res.status(200).json({task})
})

const deleteTask = asyncWrapper(async (req,res,next) => {
        result = await Task.deleteOne({_id:req.params.id})
        if(result.deletedCount < 1){
            return next(createCustomError('No task with id: ' + req.params.id, 404))
        }
        res.status(202).json({msg:'Task successfully deleted'})
})

module.exports = {
    getAllTasks, createTask, getTask, updateTask, deleteTask
}