const axios = require('axios')

const url = 'https://api.github.com/users/Gutoneitzke/repos'

async function getRepositorio() {
     axios
        .get(url)
        .then(resposta => {
            console.log(resposta.data);
            console.log('Success');
        })
        .catch(erro =>{
            console.log(erro);
            console.log('Error');
        })
        .finally(final => {
            console.log('End the request');
        })
}

getRepositorio()