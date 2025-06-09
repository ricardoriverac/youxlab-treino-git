btnInserir = document.querySelector(".inserir")
const tabela = document.querySelector("table")
const btnR = document.getElementById("remove")


const cadastroPessoas = (evt) => {
    let nome = document.getElementById("nome").value
    let numero = document.getElementById("numero").value
    let cpf = document.getElementById("cpf").value
    let email = document.getElementById("email").value

    if (numero.lenght < 11 ){
        alert("O número deve ter 11 dígitos")
    }

    const inputs = [nome, numero, cpf, email]
    const tr = document.createElement("tr")
    let linhas = tabela.rows.length
    tr.setAttribute("id", "linha" + (linhas -1))


    for (pessoa of inputs){
        let td = document.createElement("td")
        td.innerHTML = pessoa
        tr.appendChild(td)
    }

    let td = document.createElement("td")
    let btnRemover = document.createElement("button")
    let btnEditar = document.createElement("button")
    btnRemover.textContent = "Remover"
    btnEditar.textContent = "Editar"
    btnRemover.setAttribute("id", "remove")
    btnEditar.setAttribute("id", "edit")

    btnRemover.addEventListener("click", () => {
        tr.remove()
    })

    btnEditar.addEventListener("click", () => {
        let nome = document.getElementById("linha1")
        console.log(tr)
        document.getElementById("nome").value = tr.cells[0].innerHTML
        document.getElementById("numero").value = tr.cells[1].innerHTML
        document.getElementById("cpf").value = tr.cells[2].innerHTML
        document.getElementById("email").value = tr.cells[3].innerHTML
        tr.remove()
    })


    td.appendChild(btnEditar)
    td.appendChild(btnRemover)
    tr.appendChild(td)
    tabela.appendChild(tr)
}

btnInserir.addEventListener("click", () => {
    cadastroPessoas()
    document.getElementById("nome").value = ""
    document.getElementById("numero").value = ""
    document.getElementById("cpf").value = ""
    document.getElementById("email").value = ""
})

const editarButton = () => {
    cadastroPessoas()
    }

