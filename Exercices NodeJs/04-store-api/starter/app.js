require('dotenv').config()
require('express-async-errors')
//async errors

const express = require('express')
const app = express()

const connectDB = require('./db/connect')
const productsRouter = require('./routes/products')

const notFoundMiddleware = require('./middleware/not-found')
const errorMiddleware = require('./middleware/error-handler')

// middleware
app.use(express.json())

//routes
app.get('/',(req,res) => {
    res.send('<h1>Store API</h1><a href="/api/v1/products">products route</a>')
})

app.use('/api/v1/products', productsRouter)

//product routes

app.use(notFoundMiddleware)
app.use(errorMiddleware)

const PORT = process.env.PORT || 3000

const start = async() => {
    try{
        await connectDB(process.env.MONGO_URI)
        app.listen(PORT, console.log('Server is running on port : ' + PORT))
    }catch(error){
        console.log(error)
    }
}

start()