function nome(){
    console.log('CFB Cursos')
}

nome() // chamando a função sozinha

for (let i=0; i<10; i++){ // testanto com um loop
    nome()
}

function soma2_10(){
    let numero1 = 2
    let numero2 = 10
    let soma = numero1 + numero2
    console.log(soma)
}

for (let i=0; i<10; i++){
    soma2_10()
}

// função pra mudar o texto no browser q tá sendo chamada com um botão em html
function mudarTexto(){
    let div1 = document.getElementById('div1')
    let div2 = document.getElementById('div2')
    let div3 = document.getElementById('div3')

    div1.innerHTML='CFB Cursos'
    div2.innerHTML='CFB Cursos'
    div3.innerHTML='CFB Cursos'
}