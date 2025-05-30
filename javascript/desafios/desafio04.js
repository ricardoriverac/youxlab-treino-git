
function alterandoValor (){
    let senha = "123@#$DSE"
    const senha2 = document.getElementById("password")
    // console.log(senha2.value)
    if (senha.length < 8){
        console.log("A senha deve conter pelo menos 8 caracteres")
    }
    
    if (!/[A-Z]/.test(senha)){
        console.log("A senha deve ter pelo menos 1 letra maiúscula")
    }
    
    if (!/[0-9]/.test(senha)){
        console.log("A senha deve ter pelo menos 1 número")
    }
    
    if (!/[!@#$%¨&*]/.test(senha)){
        console.log("A senha deve ter pelo menos 1 caractere especial")
    }
    console.log(senha2)
}
