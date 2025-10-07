// // sintaxe
function primeiraFuncao(){

    return new Promise((resolve)=>{

        setTimeout(()=>{
            console.log("Esperou 1 segundo")
            resolve()
        },1000)

    })

}

async function segundaFuncao(){

    console.log("Iniciou");
    await primeiraFuncao()
    console.log("Terminou");

}


// prático
function getUser(id){

    return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        .then(dada => dada.json())
        .catch(erro => console.log(erro))

}

async function showUserName (id) {

    try{
        const user = await getUser(id)
        console.log(`O nome do usuário é: ${user.name}`);
    }catch (erro){
        console.log(`ERRO: ${erro}`);
    }
    
}

showUserName(3)

