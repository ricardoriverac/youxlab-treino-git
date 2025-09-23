import axios from 'axios'

const api = axios.create({
    baseURL: 'http://localhost:5000'
})


 async function getPeople() {
    try{
        const resposta = await fetch(url)
        const dados = await resposta.json()
        console.log("Todos os dados de People: ", dados);
    }catch(erro){
        console.log(erro);
    }
 }

 getPeople()