let senha = []
if (senha.length >= 8){
    console.log('SENHA COM 8 CARACTERES.')
}else{
    console.log('SENHA NÃO CONTÉM A QUANTIDADE MINÍMA DE CARACTERES.')
}if (senha.match(/[A-Z]/g)){
    console.log('A SENHA CONTÉM LETRA MAIÚSCULA.')
}else{
    console.log('A SENHA NÃO CONTÉM LETRA MAIÚSCULA.')
}if (senha.match(/[0-9]/g)){
    console.log('SUA SENHA POSSUI NÚMEROS.')
}else{
    console.log('SUA SENHA NÃO CONTÉM NÚMEROS.')
}if(senha.match(/[\W|_]/g)){
    console.log("A SUA SENHA CONTÉM SÍMBOLOS.")
}else{
    console.log('A SUA SENHA NÃO CONTÉM SÍMBOLOS.')
}
