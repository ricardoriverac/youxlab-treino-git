const p_array = document.querySelector('#array')
const botaoVerificar = document.querySelector('#botaoVerificar')
const resultado = document.querySelector('#resultado')

const elementosArray = [21,25,14,20,19,18,22]
p_array.innerHTML = `[ ${elementosArray} ]`

botaoVerificar.addEventListener('click',(evento)=>{
    const retorno = elementosArray.every((elemento, i)=>{
        if (elemento < 18){
            resultado.innerHTML = `Array não conforme na posição ${i}`
        }
        return elemento >= 18
    })
    if (retorno){
        resultado.innerHTML ='OK'
    }
    //console.log(retorno)
})