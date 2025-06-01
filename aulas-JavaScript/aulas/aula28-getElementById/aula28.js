const divC1 = document.getElementById('c1')
const divC2 = document.getElementById('c2')
const divC3 = document.getElementById('c3')
const divC4 = document.getElementById('c4')
const divC5 = document.getElementById('c5')
const divC6 = document.getElementById('c6')

console.log(divC1)
console.log(divC1.id)
console.log(divC1.innerHTML)

const arrayElementos = [divC1, divC2, divC3, divC4, divC5, divC6]

// usando o for pra mudar o nome
for (let div of arrayElementos){
    div.innerHTML = 'YouxLab'
}

// usando o map
arrayElementos.map((elemento)=>{
    console.log(elemento)
})

console.log(arrayElementos)