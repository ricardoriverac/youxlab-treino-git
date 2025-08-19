// função parametrizada
function funcao() {
    console.log('curso de javascript')
}

funcao() // chamando a função 1x
console.log('\n')

//funçao pode ser chamada qnts * quiser
funcao()
funcao()
funcao()
console.log('\n')

// usando dentro de um loop
for (let i = 0; i < 10; i++) {
    funcao() // vai repetir 10x essa função
}
console.log('\n')

// exemplo de funçao com soma
function soma2_10() {
    let numero1 = 2
    let numero2 = 10
    let resultado = numero1 + numero2
    console.log(resultado)
}

soma2_10() // chama a função e faz a soma
console.log('\n')

// função que muda o conteúdo de 3 divs na página
function mudartextodiv() {
    let div1 = document.getElementById('div1')
    let div2 = document.getElementById('div2')
    let div3 = document.getElementById('div3')
    
    // troca o texto das divs pra "curso de javascript"
    div1.innerHTML = 'curso de javascript'
    div2.innerHTML = 'curso de javascript'
    div3.innerHTML = 'curso de javascript'
}

// o texto das divs só muda depois que essa função for chamada
console.log('\n')
