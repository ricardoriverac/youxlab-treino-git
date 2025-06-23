const jogo = document.querySelector(".jogo")
const btn_add = document.querySelector(".btn_add")
const jogador_x_o = document.querySelector(".jogador_x_o")
const ganhador = document.querySelector(".ganhador")

let jogadorX = true
let jogadorO = false
let jogadorXNome = ''
let jogadorONome = ''
let i = 0
let indX = 0
let indO = 0
let empate = true
const combinacoes = [[0,1,2], [0,3,6], [3,4,5], [0,4,8], [2, 4, 6], [2,4,8], [1,4,7], [6, 7, 8]]

for(i = 0; i < 9; i++){
    const colunas = document.createElement("div")
    colunas.setAttribute("class", "coluna")
    colunas.setAttribute("id", "c" + i)
    jogo.appendChild(colunas)
}

const coluna = document.querySelectorAll(".coluna")

const vitoriasX = document.createElement("label")
vitoriasX.setAttribute("id", "vitoriasX")
vitoriasX.textContent = "Vitórias X: 0"
ganhador.appendChild(vitoriasX)

const vitoriasO = document.createElement("label")
vitoriasO.setAttribute("id", "vitoriasO")
vitoriasO.textContent = "Vitórias O: 0"
ganhador.appendChild(vitoriasO)

const jogador = document.createElement("label")
jogador.setAttribute("id", "jogadores")
jogador.textContent = "Vez do jogador X"
jogador_x_o.appendChild(jogador)

btn_add.addEventListener("click", (evt) => {
    let  jogador1 = document.querySelector("#jgdr1")
    let jogador2 = document.querySelector("#jgdr2")
    jogadorXNome = `${jogador1.value}`
    jogadorONome = `${jogador2.value}`
    vitoriasX.textContent = `Vitórias de ${jogadorXNome} : 0`
    vitoriasO.textContent = `Vitórias de ${jogadorONome} : 0`
})

function velha() {
    return [...coluna].every(quadrado => quadrado.textContent !== "")
}

coluna.forEach((quadrado) => {
    quadrado.addEventListener("click", (evt) => {
        if(jogadorX){
            if(quadrado.textContent == ""){
                quadrado.style.backgroundColor = "#90D1CA";
                quadrado.textContent="X"
                jogador.textContent = "Vez do jogador O"
                jogadorO = true
                jogadorX = false
            }
        }else{
            if(quadrado.textContent == ""){
                quadrado.style.backgroundColor = "#129990"
                quadrado.textContent="O"
                jogador.textContent = "Vez do jogador X"
                jogadorX = true
                jogadorO = false
            }
        }

        combinacoes.forEach(colum => {
            if(coluna[colum[0]].textContent == "X" & coluna[colum[1]].textContent == "X" & coluna[colum[2]].textContent == "X"){
                 for (indice of coluna){
                    indice.textContent = ""
                    indice.style.backgroundColor = "white";
                }
                jogador.textContent = "Vez do jogador X"
                jogadorX = true
                jogadorO = false
                indX++
                vitoriasX.textContent = `Vitórias de ${jogadorXNome}: ${indX}`
            }else if(coluna[colum[0]].textContent == "O" & coluna[colum[1]].textContent == "O" & coluna[colum[2]].textContent == "O"){
                for (indice of coluna){
                    indice.textContent = ""
                    indice.style.backgroundColor = "white";
                }
                jogador.textContent = "Vez do jogador X"
                jogadorX = true
                jogadorO = false
                indO++
                vitoriasO.textContent = `Vitórias de ${jogadorONome} : ${indO}`
            }
        })
        if(velha()) {
            alert("deu velha")
        }

        // if(coluna[0].textContent == "X" & coluna[1].textContent == "X" & coluna[2].textContent == "X"){
        //     for (indice of coluna){
        //         indice.textContent = "X"
        //         indice.textContent = ""
        //     }
        //     ind++
        //     vitoriasX.textContent = `Vitórias X: ${ind}`
        // }
    })
})


// coluna.addEventListener("click", (evt) => {
    
//     if(jogadorX){
//         coluna.textContent = "X"
//         jogador
//     }else{
//     jogadorX = true
//     coluna.textContent = "O"
//     }
//         })
