const p_array = document.querySelector('#array')
const btnVerificar = document.querySelector('#btnVerificar')
const resultado = document.querySelector('#Resultado')

const elementos = [17, 12, 11, 10, 14, 16, 15, 19]
p_array.innerHTML = elementos

btnVerificar.addEventListener('click', (evt)=>{
    const ret = elementos.some((e, i)=>{
        if(e < 18){
            resultado.innerHTML='Array não conforme na posição ' + i
        }
        
        return e>=18
    })
    
    if(ret){
        resultado.innerHTML = 'Ok'
    }
})