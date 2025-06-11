const caixa = document.querySelector("#caixa")

let mapa = new Map()

mapa.set("curso", "javascript")
mapa.set(10, "CBF Cursos")
mapa.set(1, 100)
mapa.set("canal", 100)

console.log(mapa)

let pes = 10
res = ""
if(mapa.has(pes)){
    res = "A chave existe na coleção com o valor: " + mapa.get(pes)
}else{
    res = "A chave NÃO está na coleção"
}

res += "<br/> O tamanho da coleção é: " + mapa.size
caixa.innerHTML = res

mapa.forEach((el) => {
    console.log(el)
})

// caixa.innerHTML = mapa.get("Curso")
