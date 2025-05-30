const senha = 'javjs'

do{
    if (senha.length < 8){
        console.log('A senha deve ter no mínino 8 caracteres')
    }
    if (!(/[A-Z]/.test(senha))){
        console.log('A senha deve conter no mínimo 1 letra maiúscula')
    }
    if (!(/[0-9]/.test(senha))){
        console.log('A senha deve conter no mínimo 1 numero') 
    }
    
}while(!(senha))