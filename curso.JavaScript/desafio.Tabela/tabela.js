const dados = [...document.querySelectorAll('.dados')]
// const pessoa = [...document.querySelector('#estilo')]
const btnInserir=document.getElementById('btnInserir')
const btnRemover=document.getElementsByClassName('btnRemover')


dados.map((ele)=>{
    btnInserir.addEventListener('click', (evt)=>{
        const para = document.createElement('tr')
        const input = document.getElementById('digite').value
        const node = document.createElement('td')
        para.appendChild(node)
        const element = document.getElementById('estilo')
        element.appendChild(para)
    })
    
})