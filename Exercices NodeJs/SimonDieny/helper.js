const getUniqueId = (pokemons) => {
    const Pokemons_ids = pokemons.map((pokemon) => {
        return pokemon.id
    })
    const highest_id = Pokemons_ids.reduce((idA,idB) => {
        return idA > idB ? idA : idB
    })
    return highest_id + 1
}

module.exports = getUniqueId