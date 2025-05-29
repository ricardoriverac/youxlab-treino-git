let senha = 'youxLab98765'
do {if (!senha.length >= 8){
        console.log('SENHA NÃO CONTÉM A QUANTIDADE MINÍMA DE CARACTERES.')
    }if (!senha.match(/[A-Z]/g)){
        console.log('A SENHA NÃO CONTÉM LETRA MAIÚSCULA.')
    }if (!senha.match(/[0-9]/g)){
        console.log('SUA SENHA NÃO CONTÉM NÚMEROS.')
        continue
    }if(!senha.match(/[\W|_]/g)){
        console.log('A SUA SENHA NÃO CONTÉM SÍMBOLOS.')
    }}while(!senha.match(/[A-Z]/g) && !senha.match(/[\W|_]/g) && !senha.match(/[0-9]/g) && !senha.length >= 8){

    }console.log('Tudo certo, fim do programa')
