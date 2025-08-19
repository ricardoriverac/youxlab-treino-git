//uso do map 1 exemplo de uso:
//const frutas = ['Maça', 'Laranja', 'Banana','Abacate']
// frutas.map((el, i)=>{ //pode passar dois paramentros ou tres, eles indicam o elemento da coleçao e oque ele ta interando, todos em ordem. ex: 1 seria mça  console.log("Frutas: " + el + " Posiçao das frutas: ") //operando os elementos +i)
//let c = frutas.map((el, i)=>{
  //      return "<div>"+el+"</div>"
//})

//console.log(c)

//MAIS SOBRE A FUNÇAO MAP:
// let el = document.getElementsByTagName("div");
//let el2 = [...el];
//el2.map((e, l) => {
  //  e.innerHTML="lexi legal"//usando spread
  //console.log(e);
// });


//const el = document.getElementsByTagName("div");
//const val= Array.prototype.map.call(el,({innerHTML})=>innerHTML)
//console.log(val)

const converterInt=(e)=>parseInt(e)
const dobrar=(e)=>e*2
let num =['1' , '2', '3', '4', '5'].map(dobrar)
num.map(converterInt)
console.log(num)