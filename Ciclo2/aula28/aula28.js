let senha = 'sophia21'

while(true){
    if (senha.length < 8) {
        console.log(senha)
        console.log('ERRO!\nSua senha tem menos que 8 caracteres ')
        break
    }else{
        console.log(senha)
        console.log('Sua senha TEM 8 caracteres')
        break
    }
}


let TemMaicuscula = false;
do {
    for (let indice = 0; indice < senha.length; indice++) {
        let letra = senha[indice];
        if (
            letra === letra.toLocaleUpperCase() &&
            letra !== letra.toLocaleLowerCase()
        ) {
            TemMaicuscula = true;
            break;
        }
    }
    if (!TemMaicuscula) {
        console.log('ERRO!\nA senha precisa conter pelo menos uma letra MAIÚSCULA');
        break;
    }
} while (!TemMaicuscula);

console.log('Senha válida!');

if (TemMaicuscula) {
    console.log('Sua senha tem letra maiúscula');
}