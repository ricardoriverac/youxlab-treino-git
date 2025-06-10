const p_array = document.querySelector('#array')
const btnVerificar = document.querySelector('#btnVerificar')
const resultado = document.querySelector('#Resultado')

const elementos = [7, 23, 12, 76, 32, 21, 18]
p_array.innerHTML = elementos

btnVerificar.addEventListener('click', (evt)=>{
    const ret = elementos.every((e, i)=>{
        if(e < 18){
            resultado.innerHTML='Array não conforme na posição ' + i
        }
        
        return e>=18
    })
    
    if(ret){
        resultado.innerHTML = 'Ok'
    }
})