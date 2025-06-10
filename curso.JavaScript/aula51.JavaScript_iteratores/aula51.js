const resp = document.getElementById('digite')
const btnAdicionar = document.getElementById('btnAdicionar')
const aqui = document.getElementById('aqui')


const valores = [12, 7, 9, 10, 2]

const it_valores = valores[Symbol.iterator]()

console.log(it_valores.next())
console.log(it_valores.next())
console.log(it_valores.next())
console.log(it_valores.next())
console.log(it_valores.next())
console.log(it_valores.next())

const texto = resp.value


btnAdicionar.addEventListener('click', (evt)=>{
    const txt = texto[Symbol.iterator]()
    aqui.innerHTML = txt.next()
})



// console.log(txt.next())
// console.log(txt.next())
// console.log(txt.next())
// console.log(txt.next())
// console.log(txt.next())
// console.log(txt.next())
// console.log(txt.next())

