const p_array = document.querySelector('#array')
const txt_pesquisar = document.querySelector('#txt_pesquisar')
const btnPesquisar = document.querySelector('#btnPesquisar')
const resultado = document.querySelector('#Resultado')

const elementos = ['chocolate', 'sorvete', 'bombom', 'picolé', 'brigadeiro', 'achocolatado', 'paçoca', 'bala']
p_array.innerHTML = elementos

btnPesquisar.addEventListener('click',(evt)=>{
    resultado.innerHTML = 'Valor ' + txt_pesquisar.value + ' não encontrado.'
    const ret=elementos.find((e, i)=>{
        if (e.toUpperCase()==txt_pesquisar.value.toUpperCase()){
            resultado.innerHTML='Valor encontrado: ' + e + ', na posição: ' + i
            return e   
        }
    })
    console.log(ret)
}) 