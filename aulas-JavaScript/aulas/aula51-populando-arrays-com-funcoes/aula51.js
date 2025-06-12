let valores1 = [1,2,3,4,5]
const operacoes1 = [
    (valor)=>{
        let resultado1 = 0
        for (v of valor){
            resultado1+= v
        }
        return resultado1
    },
    (valor)=>{
        let resultado1 = 1
        for (v of valor){
            resultado1*=v
        }
        return resultado1
    },
    (valor)=>{
        for (v of valor){
            console.log(v)
        }
    }
]

operacoes1[2](valores1)

// calculadora

const botaoSoma = document.getElementById('botaoSoma')
const botaoSubtracao = document.getElementById('botaoSubtracao')
const botaoMultiplicacao = document.getElementById('botaoMultiplicacao')
const botaoDivisao = document.getElementById('botaoDivisao')

const operacoes = [
    ()=>{
        const valores = [document.getElementById('valor1').value,document.getElementById('valor2').value]
        resultado.value = Number(valores[0]) + Number(valores[1])
    },

    ()=>{
        const valores = [document.getElementById('valor1').value,document.getElementById('valor2').value]
        resultado.value = Number(valores[0]) - Number(valores[1])
    },

    ()=>{
        const valores = [document.getElementById('valor1').value,document.getElementById('valor2').value]
        resultado.value = Number(valores[0]) * Number(valores[1])
    },

    ()=>{
        const valores = [document.getElementById('valor1').value,document.getElementById('valor2').value]
        resultado.value = Number(valores[0]) / Number(valores[1])
    }
]

botaoSoma.addEventListener('click', operacoes[0])
botaoSubtracao.addEventListener('click', operacoes[1])
botaoMultiplicacao.addEventListener('click', operacoes[2])
botaoDivisao.addEventListener('click', operacoes[3])