const p_array = document.querySelector('#array')
const txt_pesquisar = document.querySelector('#txt_pesquisar')
const botaoPesquisar = document.querySelector('#botaoPesquisar')
const resultado = document.querySelector('#resultado')

const elementosArray = ['html', 'css', 'javascript']
p_array.innerHTML = `[ ${elementosArray} ]`

botaoPesquisar.addEventListener('click',(evento)=>{
    resultado.innerHTML = 'Valor não encontrado'
    const retorno = elementosArray.find((elemento, i)=>{
        if (elemento.toUpperCase() === txt_pesquisar.value.toUpperCase()){
            resultado.innerHTML = `Valor encontrado ${elemento} na posição ${i}`
            return elemento
        }
    })
    console.log(retorno)
})