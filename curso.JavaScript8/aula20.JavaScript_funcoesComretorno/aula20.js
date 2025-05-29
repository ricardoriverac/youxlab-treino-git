function soma (a, b){
    console.log ( a + '+' +  b + '=' + (a+b))
}

soma(8, 3)
soma(23, 5)

for (let i = 0; i < 11; i++){
    soma(i, i)
}

function mudarTexto (){
    let d1 = document.getElementById("d1")
    let d2 = document.getElementById("d2")
    let d3 = document.getElementById("d3")
    d1.innerHTML='Rodrigão é a mesma coisa que ricardinho'
    d2.innerHTML='Ricardinho é a mesma coisa que rodrigão'
    d3.innerHTML='É tudo a mesma coisa, normalize confundir!! #justiçapeloslabers'
}