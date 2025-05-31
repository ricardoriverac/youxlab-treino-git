const senha = 'Alexia@2023';
let senhaValida = false;

function validarComprimento(senha) {
    return senha.length >= 8;
}

function temMaiuscula(senha) {
    for (let letra of senha) {
        if (letra >= 'A' && letra <= 'Z') {
            return true;
        }
    }
    return false;
}

function temNumero(senha) {
    for (let num of senha) {
        if (num >= '0' && num <= '9') {
            return true;
        }
    }
    return false;
}

function temCaractereEspecial(senha) {
    const especiais = ['!', '@', '#', '$', '%'];
    for (let carac of senha) {
        if (especiais.includes(carac)) {
            return true;
        }
    }
    return false;
}

do {
    let erro = false;

    if (!validarComprimento(senha)) {
        console.log('INVALIDA! Senha tem menos que 8 caracteres');
        erro = true;
    } else {
        console.log('VALIDA! Senha tem 8 ou mais caracteres');
    }

    if (!temMaiuscula(senha)) {
        console.log('INVÁLIDA! Senha NÃO tem letra maiúscula');
        erro = true;
    } else {
        console.log('Sua senha tem letra Maiúscula');
    }

    if (!temNumero(senha)) {
        console.log('INVALIDA! Senha NÃO tem Número');
        erro = true;
    } else {
        console.log('VALIDA! Sua senha tem Número');
    }

    if (!temCaractereEspecial(senha)) {
        console.log('INVALIDA! Senha NÃO tem Caractere Especial');
        erro = true;
    } else {
        console.log('VALIDA! Sua senha tem Caractere Especial');
    }

    if (!erro) {
        senhaValida = true;
        console.log('Senha Totalmente Válida');
    }

} while (!senhaValida);