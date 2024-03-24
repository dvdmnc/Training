const Product = require('../models/product')

const getAllProducts = async (req,res) => {
    const {name, featured, company, sort, fields, numericFilters} = req.query
    let queryObject = {}
    if (name){
        queryObject.name = {$regex: name, $options: 'i'}
    }
    if(company){
        queryObject.company = {$regex: company, $options: 'i'}
    }
    if(featured){
        queryObject.featured = featured === 'true' ? true : false
    }
    if(numericFilters){
        const operatorMap = {
            '>':'$gt',
            '>=':'$gte',
            '=':'$eq',
            '<=':'$lte',
            '<':'$lt'
        }
        const regEx = /\b(<|>|<=|>=|=)\b/g
        let filters = numericFilters.replace(regEx,(match)=>`-${operatorMap[match]}-`)
        const options = ['price','rating']
        filters = filters.split(',').forEach((item) => {
            const [field, operator, value] = item.split('-')
            if(options.includes(field)){
                queryObject[field] = {[operator]:Number(value)}
            }
        })
    }
    let result = Product.find(queryObject)
    if(sort){
        const sortList = sort.split(',').join(' ')
        result = result.sort(sortList)
    }
    else{
        result = result.sort('createdAt')
    }
    if(fields){
        const fieldsList = fields.split(',').join(' ')
        result = result.select(fieldsList)
    }
    const page = Number(req.query.page) || 1
    const limit = Number(req.query.limit) || 10
    const skip = (page-1)*limit
    
    result = result.skip(skip).limit(limit)

    const products = await result
    res.status(200).json({products})
}

module.exports = {
    getAllProducts
}