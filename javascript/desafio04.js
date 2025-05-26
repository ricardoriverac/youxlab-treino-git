let senha = prompt("Digite uma senha: ")
while (senha.length < 8 || !/[A-Z]/.test(senha)){
    alert("A senha deve conter pelo menos 8 caracteres")
    senha = prompt("Digite uma senha: ")
}

while(senha == /[A-Z]/.test(senha)){
    alert("A senha deve ter pelo menos 1 letra maiúscula")
}


if (senha.length >= 8 || /[A-Z]/.test(senha)){
    alert("Senha aceita")
}
