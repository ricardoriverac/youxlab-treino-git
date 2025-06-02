// removeElement --> apaga elementos html dinamicamente da página

const caixa1 = document.querySelector('#caixa1')  // pega a caixa onde os cursos vão ser colocados
const cursos = ['HTML', 'CSS', 'Javascript', 'PHP', 'React', 'MySQL', 'ReactNative']  // lista de cursos

// cria os elementos de curso na tela e permite excluir clicando no ícone
cursos.map((curso, chave) => {
    const novoElemento = document.createElement('div')  // cria a div do curso
    novoElemento.setAttribute("id", "c" + chave)         // define um id único
    novoElemento.setAttribute("class", "curso c1")       // aplica classes de estilo
    novoElemento.innerHTML = curso                       // insere o nome do curso

    const botao_Lixeira = document.createElement("img")  // cria o ícone de lixeira
    botao_Lixeira.setAttribute("src", "/home/youx/Downloads/lixo.png")        // define a imagem do ícone
    botao_Lixeira.setAttribute("class", "botao_lixeira") // adiciona classe para estilizar

    // quando clicar no ícone, remove a div do curso correspondente
    botao_Lixeira.addEventListener("click", (evento) => {
        caixa1.removeChild(evento.target.parentNode)     // remove a div pai (curso)
    })

    novoElemento.appendChild(botao_Lixeira)  // adiciona o ícone dentro da div do curso
    caixa1.appendChild(novoElemento)         // coloca a div do curso na caixa principal
})
