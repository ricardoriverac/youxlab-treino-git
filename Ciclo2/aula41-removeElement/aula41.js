// removeElement --> REMOVE elementos HTML da página

const caixa1 = document.querySelector('#caixa1')
const cursos = ['HTML', 'CSS', 'Javascript', 'PHP', 'React', 'MySQL', 'ReactNative']

// ADICIONANDO NOVOS ELEMENTOS E PERMITINDO REMOÇÃO AO CLICAR
cursos.map((curso,chave) => {
    const novoElemento = document.createElement('div')
    novoElemento.setAttribute("id", "c" + chave)
    novoElemento.setAttribute("class", "curso c1") 
    novoElemento.innerHTML = curso

    // Adiciona o ícone da lixeira
    const botao_Lixeira = document.createElement("img")
    botao_Lixeira.setAttribute("src", "lixo.png")
    botao_Lixeira.setAttribute("class", "botao_lixeira")

    // Evento de clique no botão da lixeira
    botao_Lixeira.addEventListener("click", (evento) => {
        caixa1.removeChild(evento.target.parentNode)
    })

    novoElemento.appendChild(botao_Lixeira)
    caixa1.appendChild(novoElemento)
})
