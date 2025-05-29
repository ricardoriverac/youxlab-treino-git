//const cursos = ['JavaScript', 'Python', 'HTML', 'CSS', 'PHP']
//cursos.map((ell, i)=>{
 //   console.log('CURSO: ' + ell + ' | POSIÇÃO: ' + i)
//})

//let el =document.getElementsByTagName("div")
//const valores = Array.prototype.map.call(el, ({innerHTML})=>{innerHTML})
//console.log(valores)

//el = [...el]
//console.log(el)
//el.map((e, i)=>{
 //   e.innerHTML="CFB Cursos"})

const converterint =(e)=>parseInt(e)
let num = ['1', '2', '3', '4'].map(converterint)
console.log(num)
