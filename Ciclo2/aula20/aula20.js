// FUNÇÃO em Javascript  #P1

//estrutura do comando

function funcao(){ // Declaração da função
    console.log('Curso de Javascript')
}

funcao() // chamada da função 
console.log('\n')

// pode-se chamar quantas vezes quiser:
funcao()
funcao()
funcao()
console.log('\n')

//Pode ser colocada em um loop
for(let indice=0; indice<10; indice++){
    funcao()  //chamou a função 10x
}
console.log('\n')


//Outro exemplo:
function soma2_10(){ // declaração da fução que soma 2+10
    let numero1=2
    let numero2=10
    let soma= numero1+numero2
    console.log(soma)
}

soma2_10() // cahamda da função
console.log('\n')


//outro exmplo:
//Função para mudar o texto das divs
function mudarTextoDiv(){
    let div1=document.getElementById('div1')
    let div2=document.getElementById('div2')
    let div3=document.getElementById('div3')
    div1.innerHTML="Curso de Javascript"
    div2.innerHTML="Curso de Javascript"
    div3.innerHTML="Curso de Javascript"
}


// somente depois de executar a função o conteúdo modificou
console.log('\n')