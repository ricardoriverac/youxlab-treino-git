// ARRAY 

const valor1=document.getElementById("v1")
const valor2=document.getElementById("v2")

const btnSoma=document.getElementById("btnSoma")
const btnSubtracao=document.getElementById("btnSubtracao")
const btnMultiplicacao=document.getElementById("btnMultiplicacao")
const btnDivisao=document.getElementById("btnDivisao")

const resultado=document.getElementById("resultado")

const valores=[]


// array de operações 
const operacoes=[
    (valor)=>{      //[0] posição do array - função de soma dos valores
        let soma=0
        for(val of valor){
            soma+=val
        }
        return soma
        
    },
    
    (valor)=>{      //[1] posição do array - função de subtração dos valores
        let subtracao=valor[0]
        for(let indice = 1; indice < valor.length; indice++){
            subtracao-=valor[indice]
        }
        return subtracao
    },

    (valor)=>{      //[2]] posição do array - função de multiplicação dos valores
        let multiplicacao=1
        for(val of valor){
            multiplicacao*=val
        }
        return multiplicacao
    },

    (valor)=>{      //[3] posição do array - função de divisão dos valores
        let divisao=valor[0]
        for(let indice = 1; indice < valor.length; indice++){
            divisao/=valor[indice]
        }
        return divisao
    }
]

btnSoma.addEventListener("click",(evento)=>{
    valores.push(Number(valor1.value))
    valores.push(Number(valor2.value))
    let som=operacoes[0](valores)
    resultado.value=som
})

btnSubtracao.addEventListener("click",(evento)=>{
    valores.push(Number(valor1.value))
    valores.push(Number(valor2.value))
    let sub=operacoes[1](valores)
    resultado.value=sub
})

btnMultiplicacao.addEventListener("click",(evento)=>{
    valores.push(Number(valor1.value))
    valores.push(Number(valor2.value))
    let mul=operacoes[2](valores)
    resultado.value=mul
})

btnDivisao.addEventListener("click",(evento)=>{
    valores.push(Number(valor1.value))
    valores.push(Number(valor2.value))
    let div=operacoes[3](valores)
    resultado.value=div
})










//chama a função:
//sintaxe--> console.log( array_com_funções[posição_da_função_desejada](array_com_os_valores) )

// console.log(operacoes[0](valores)) //soma os valores

// console.log(operacoes[1](valores)) // multiplica os valores

// operacoes[2](valores) //imprime os valores da tela --> já tem o console.log na função, com isso, é chamada assim


