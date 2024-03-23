const express = require('express')
let pokemons = require('./mock-pockemon')
const getUniqueId = require('./helper.js')
const parser = require('body-parser')

const app = express()
const port = 3000

app.use(parser.json())

app.get('/api/pokemons',(req,res) => {
    res.json({message : 'Here are all the pokemons in your pokedex', data : pokemons})
})

app.post('/api/pokemons',(req,res) => {
    let id = getUniqueId(pokemons)
    let newPokemon = {...req.body, id:id, created: new Date()}
    pokemons.push(newPokemon)
    res.json({message: 'The pokemon ' + newPokemon.name + ' has been added to the pokemons list', data : newPokemon})
})

app.put('/api/pokemons/:id',(req,res) => {
    let id = parseInt(req.params.id)
    let pokemon = pokemons.filter((pokemon) => pokemon.id === id)
    pokemons = pokemons.filter((pokemon) => pokemon.id !== id)
    let modifiedPokemon = {...req.body, id:id, created: pokemon.created}
    pokemons.push(modifiedPokemon)
    res.json({message:'The Pokemon has been modified !',data: modifiedPokemon})
})

app.delete('/api/pokemons/:id',(req,res) => {
    pokemons = pokemons.filter((pokemon) => pokemon.id !== parseInt(req.params.id))
    res.json({message:'The pokemon has been deleted',data:pokemons})
})

app.listen(port, (error) =>{ 
    if(!error) 
        console.log("Server is Successfully Running, and App is listening on port "+ port) 
    else 
        console.log("Error occurred, server can't start", error); 
    } )