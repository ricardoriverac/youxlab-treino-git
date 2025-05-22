"use strict" 

//MANEIRAS DE DECLARA VARIÁVEL

// var (variável)--> faz com que todo o código tenha acesso a essa var
if (true){
    var nome='Sophia' // variável declarada dentro deste comando 
}
console.log(nome) //APARECE pois essa variável foi declarada com o var



// let (variável)--> só consegue acessar no escopo que foi criada para FRENTE 
if (true){
    let nome2='Sophia' // variável declarada dentro deste comando 
}
console.log(nome2) //NÃO aparecerá pois essa variável foi declarada dentro de um comando 

// outro exemplo com o let (variável)
function teste(){
    if (true){
        let nome3='Sophia'
        console.log("Dentro do if do teste:"+ nome3) 
    }
    console.log("Dentro de teste:"+ nome3)// Não aparece pois não foi buscado no mesmo escopo (no caso dentro do comando if)
}
teste() // aparece pois foi buscado no mesmo escopo
console.log(nome3) //NÃO aparece pois não foi buscado dentro do escopo

let nome4='Sophia' // com o let é possível a auteração de conteúdo da variável
nome4='sosô' // variável modificada. 
console.log(nome4) // Então ao exercer a variável aparecerá o novo conteúdo

nome4=10 // Também pode alterar a variável com um tipo de valor diferente
console.log(nome4) // Com isso, convertera de forma AUTOMÁTICA


//const (variável)--> Modelo de variável que NÃO PODE SER ALTERADA depois de definida 
const idade=16 // NÃO PODE-SE ALTERAR SEU VALOR
console.log(idade)