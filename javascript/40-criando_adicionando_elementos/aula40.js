const caixa1 = document.querySelector("#caixa1")
const btn_c = [...document.querySelectorAll(".curso")]
const cursos = ["HTML", "CSS", "Javascript", "PHP", "React", "MySQL", "ReactNative"]

cursos.map((el, chave) => { // Para cada elemento
    console.log(chave)
    const novoElemento = document.createElement("div") // criar um elemento div
    novoElemento.setAttribute("id","c" + chave + 1) // Atribui esse novo elemento com o id "c7"
    novoElemento.setAttribute("class","curso c1") // Atribui esse novo elemento a classe "curso c1"
    novoElemento.innerHTML = el // Deu um nome para esse elemento
    caixa1.appendChild(novoElemento) // Adicionou esse novo elemento na caixa 1
})
