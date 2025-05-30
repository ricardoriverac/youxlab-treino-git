const dc1 = document.getElementById('d1')
const dc2 = document.getElementById('d2')
const dc3 = document.getElementById('d3')
const dc4 = document.getElementById('d4')
const dc5 = document.getElementById('d5')
const dc6 = document.getElementById('d6')

const elementos = [dc1, dc2, dc3, dc4, dc5, dc6]
console.log(elementos)
elementos.map((e)=>{
    console.log(e)
})

console.log(dc1)
console.log(dc1.innerHTML)
console.log(dc1.id)
dc1.innerHTML = 'CFB Cursos'