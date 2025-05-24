// OPERAÇÕES TERNÁRIAS 

let numero=10 // declarai variável

//PAR OU ÍMPAR
let resto=numero%2

if(resto==0){
    console.log('PAR')
}else{
    console.log('ÍMPAR')
}

//COM OPERAÇÃO TERNÁRIA
numero=10
resto=(!(numero%2) ? 'PAR':'ÍMPAR')
console.log(resto)
// ?--> comando de operacção ternária 
//0=false
//1=true

// SINTAXE de operação terária:  teste lógico ? se verdadeiro : se falso

//outro exemplo:
let numero1=10
let numero2=20
resto=((numero1 > numero2) ? 'VERDADEIRO':'FALSO')
console.log(resto)

//outro exemplo:
let st="A"
resultado=(st == "A" ? 'ATIVO':'INATIVO')
console.log(resultado)

