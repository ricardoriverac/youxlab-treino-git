const caixa = document.querySelector("#caixa")
const btn_limpar = document.querySelector("#btn_limpar")
const btn = document.querySelector(".btn")

let musicas = new Set(["musica1", "musica boa", "musica10"]) // Set não permite entradas duplicadas

musicas.add("musica muito legal")
musicas.add("musica1")
musicas.add("musica1")
musicas.add("musica10")

console.log(musicas)

musicas.forEach((el) => {
    caixa.innerHTML += el + "<br/>"
})

const btn_restaurar = document.createElement("button")
btn_restaurar.setAttribute("id", "btn_restaurar")
btn_restaurar.textContent = "Restaurar"

btn_limpar.addEventListener("click", () => {
    caixa.innerHTML = ""
})

// for(let m of musicas){
//     caixa.innerHTML += m + "<br/>"
// }
