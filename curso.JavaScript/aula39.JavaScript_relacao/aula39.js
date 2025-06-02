const caixa1 = document.querySelector('#caixa1')
const btn_c= [...document.querySelectorAll('.curso')]

console.log(caixa1.hasChildNodes())
console.log(btn_c[0].hasChildNodes())
console.log(btn_c[0].childNodes)

if(btn_c[0].children.length > 0){
  console.log('Possui filhos')
}else{
  console.log('Não possui filhos')
}

console.log(caixa1.firstElementChild.innerHTML='TESTE')