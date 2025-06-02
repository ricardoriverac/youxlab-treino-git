const p_array = document.querySelector('#array')
const botaoVerificar = document.querySelector('#botaoVerificar')
const resultado = document.querySelector('#resultado')

const elementosArray = [16,12,10,17,15,13,11,19]
p_array.innerHTML = `[ ${elementosArray} ]`

botaoVerificar.addEventListener('click',(evento)=>{
    const retorno = elementosArray.some((elemento, i)=>{
        if (elemento < 18){
            resultado.innerHTML = `Array não conforme na posição ${i}`
        }
        return elemento >= 18
    })
    if (retorno){
        resultado.innerHTML ='OK'
    }
})