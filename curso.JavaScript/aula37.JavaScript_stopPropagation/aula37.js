const caixa1 = document.querySelector('#caixa1')
const btn_d1 = document.querySelector('#d1')
const todos = [...document.querySelectorAll('.curso')]

caixa1.addEventListener('click', (evt)=>{
    console.log(evt.target + 'clicou') 
})

//btn_d1.addEventListener('click', (evt)=>{
  //  evt.stopPropagation

todos.map((el)=>{
    el.addEventListener('click', (evt)=>{
        evt.stopPropagation()
})
})

