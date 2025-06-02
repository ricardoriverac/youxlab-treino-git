const caixa1 = document.querySelector("#caixa1")
const btn_c = [...document.querySelectorAll(".curso")]
const cursos = ["HTML", "CSS", "Javascript", "PHP", "React", "MySQL", "ReactNative"]

cursos.map((el, chave) => { // Para cada elemento
    console.log(chave)
    const novoElemento = document.createElement("div") // criar um elemento div
    novoElemento.setAttribute("id","c" + chave) // Atribui esse novo elemento com o id "c7"
    novoElemento.setAttribute("class","curso c1") // Atribui esse novo elemento a classe "curso c1"
    novoElemento.innerHTML = el // Deu um nome para esse elemento

    const btn_lixeira = document.createElement("img")
    btn_lixeira.setAttribute("src", "https://cdn-icons-png.flaticon.com/512/1345/1345874.png")
    btn_lixeira.setAttribute("class", "btn_lixeira")
    btn_lixeira.addEventListener("click", (evt) => {
        caixa1.removeChild(evt.target.parentNode) // Remove o elemento que clicar
        
    })
    novoElemento.appendChild(btn_lixeira)
    caixa1.appendChild(novoElemento) // Adicionou esse novo elemento na caixa 1
})
