require('./db/connect')
const express = require('express')
const app = express()
const tasks = require('./routes/tasks')
const connectDB = require('./db/connect')
require('dotenv').config()
const notFound = require('./middleware/not-found')
const errorHandlerMiddleware = require('./middleware/error')

//middleware
app.use(express.static('./public'))
app.use(express.json())

//routes
app.use('/api/v1/tasks', tasks)
app.use(notFound)
app.use(errorHandlerMiddleware)

const PORT = process.env.PORT || 3000

const start = async () => {
    try{
        await connectDB(process.env.MONGO_URI)
        app.listen(PORT, error => {
            if(!error){
                console.log('App is successfully running on port :' + PORT)
            }
            else{
                console.log('Error occured, the server can\'t start', error)
            }
        })
        
    }
    catch(error){
        console.log(error)
    }
}

start()