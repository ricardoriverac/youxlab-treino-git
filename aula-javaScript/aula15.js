const objs = document.getElementsByTagName("div")

let num = [10, 20, 30, 40, 50]

for (o in objs) {
    console.log(objs[o].innerHTML)
}

for (o of objs) {
    console.log(o.innerHTML = "Curso")
}

// JavaScript =>	for...of	Percorre os valores de arrays, strings e iteráveis	javascript<br>let frutas = ['maçã','banana','uva'];<br>for (let fruta of frutas) {<br> console.log(fruta);<br>}	maçã
// banana
// uva

// JavaScript =>	for...in	Percorre os índices ou chaves	javascript<br>let frutas = ['maçã','banana','uva'];<br>for (let i in frutas) {<br> console.log(i, frutas[i]);<br>}	0 maçã
// 1 banana
// 2 uva

// JavaScript =>	for clássico	Controle manual: índice, condição, incremento	javascript<br>for (let i = 0; i < frutas.length; i++) {<br> console.log(frutas[i]);<br>}	maçã
// banana
// uva

