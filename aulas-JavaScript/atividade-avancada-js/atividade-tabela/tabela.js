const limparInput = ()=>{
    const input = document.getElementsByClassName('input')
    for (limpar of input){
        limpar.value=''
    }
}

function inserirPessoa(){
    const nome = document.getElementById('inputNome').value
    const numero = document.getElementById('inputNumeroTelefone').value
    const cpf = document.getElementById('inputCpf').value
    const email = document.getElementById('inputEmail').value
    const tabela = document.getElementById('tabela')
    
    if (nome === "" || numero === "" || cpf === "" || email === ""){
        alert("Preencha todos os campos")
        return
    }

    let novaLinha = document.createElement('tr')
    novaLinha.innerHTML = `<td>${nome}</td>
                            <td>${numero}</td>
                            <td>${cpf}</td>
                            <td>${email}</td>
                            <td><button class="botaoEditar">Editar</button>
                            <button class="botaoRemover">Remover</button></td>
                            `
    tabela.appendChild(novaLinha)
    limparInput()
    
    const botaoRemover = novaLinha.querySelector('.botaoRemover')
    botaoRemover.addEventListener('click', (evento)=>{
        novaLinha.remove()
    })

    const nomeInput = document.getElementById('inputNome')
    const numeroInput = document.getElementById('inputNumeroTelefone')
    const cpfInput = document.getElementById('inputCpf')
    const emailInput = document.getElementById('inputEmail')

    const botaoEditar = novaLinha.querySelector('.botaoEditar')
    botaoEditar.addEventListener('click', (evento)=>{
        const dados = novaLinha.querySelectorAll('td')
        
        nomeInput.value = dados[0].textContent
        numeroInput.value = dados[1].textContent
        cpfInput.value = dados[2].textContent
        emailInput.value = dados[3].textContent

        novaLinha.remove()
    })
}