const valores = document.querySelectorAll('.valor')
const btnSomar = document.querySelector('#btnSomar')
const btnSubtrair = document.querySelector('#btnSubtrair')
const btnMultiplicar = document.querySelector('#btnMultiplicar')
const btnDividir = document.querySelector('#btnDividir')
const resultado = document.querySelector('#resultado')
const btnLimpar = document.querySelector('#limpar')
const armazenamento = document.querySelector('#armazenamento')

const op = [
    (val)=>{
        let res = 0
        for(v of val){
            res+=v
        }
        return res
    },
    (val)=>{
        let res = 1
        for(v of val){
            res*=v
        }
        return res
    },
    (val)=>{
        let res = val[0]
        for(let i=1; i<val.length; i++){
            res/=val[i]
        }
        return res
    },
    (val)=>{
        let res = val[0]
        for (let i = 1; i<2; i++){
           res -= val[i]
        }
        return res
    },
     (val)=>{
        for(v of val){
           console.log(v)
        }
        return res
    }
]

btnSomar.addEventListener('click', (evt)=>{
    const numeros = []
    
    for(i=0; i<2; i++){
        numeros.push(Number(valores[i].value))
    }
   const soma = op[0](numeros)
   resultado.value = soma
   armazenamento.textContent= numeros[0] + ' + ' + numeros[1] + ' = ' + soma
})


btnSubtrair.addEventListener('click',(evt)=>{
    const numeros = []

    for(i=0; i<2; i++){
        numeros.push(Number(valores[i].value))
    }
    const subtrair = op[3](numeros)
    resultado.value = subtrair
    armazenamento.textContent= numeros[0] + ' - ' + numeros[1] + ' = ' + subtrair
})

btnMultiplicar.addEventListener('click',(evt)=>{
    const numeros = []

    for(i=0; i<2; i++){
        numeros.push(Number(valores[i].value))
    }
    const multiplicar = op[1](numeros)
    resultado.value = multiplicar
    armazenamento.textContent= numeros[0] + ' x ' + numeros[1] + ' = ' + multiplicar
})

btnDividir.addEventListener('click', (evt)=>{
    const numeros = []
    for(let i = 0; i<2; i++){
        numeros.push(Number(valores[i].value))
    }
    const dividir = op[2](numeros)
    resultado.value = dividir
    armazenamento.textContent= numeros[0] + ' / ' + numeros[1] + ' = ' + dividir
})



btnLimpar.addEventListener('click', (evt)=>{
    for(el of valores){
        el.value = ''
    }
    resultado.value = ''
})