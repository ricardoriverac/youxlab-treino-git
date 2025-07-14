const senha='oph3@okj'
let senhaValida=false

do{
    if(senha.length<8){
        console.log('INVALIDA! Senha tem menos que 8 caracteres')
    }else if(senha.length>=8){
        console.log('VALIDA! Senha tem 8 ou mais caracteres')
    }

    let letraMaicuscula=[]
    letraMaicuscula.push(...senha)
    let maiuscula=false
    for(let letra of letraMaicuscula){
        if(letra >='A'&&letra<='Z'){
            maiuscula=true
            break
        }
    }
    if (maiuscula) {
        console.log('Sua senha tem letra Maiúscula')
    } else {
        console.log('INVÁLIDA! Senha NÃO tem letra maiúscula')
    }

    let senhaNumero=[]
    senhaNumero.push(...senha)
    let numero=false 
    for (let num of senhaNumero){
        if(num >= '0' && num <= '9'){
            numero=true
            break
        }
    }
    if (numero) {
        console.log('VALIDA! Sua senha tem Número')
    } else {
        console.log('INVALIDA! Senha NÃO tem Número')
    }

    const especiais=['!','@','#','$','%']

    let senhaCaracter=[]
    senhaCaracter.push(...senha)
    let caractere=false
    for(let carac of senhaCaracter){
        if(especiais.includes(carac)){
            caractere=true
            break
        }
    }
    if (caractere) {
        console.log('VALIDA! Sua senha tem Caractere Especial')
        break
    } else {
        console.log('INVALIDA! Senha NÃO tem Caractere Especial')
    }
}while(!senhaValida);

console.log('\n')
if(senhaValida==true){
    console.log('Senha Totalmente Válida')
}else{
    console.log('Senha Inválida')
}