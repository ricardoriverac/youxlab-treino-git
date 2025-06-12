//FUNÇÃO PARA INSERIR LINHA
function insertRow(){
    // DECLARA INPUTS
    const nome=document.getElementById('nome')
    const numero=document.getElementById('numero')
    const cpf=document.getElementById('cpf')
    const email=document.getElementById('email')
    
    //ALERTA PARA PREENCHER TODOS OS CAMPOS
    if(nome.value === "" ||numero.value === ""||cpf.value === ""||email.value === ""){
        alert('ERRO!\nPrencha todos os campos')
        return ;
    }
    
    //DECLARA TABELA
    const tabela=document.getElementById("tabelaBody")
    
    //ADICIONA LINHA NOVA NA TABELA CHAMANDO A FUNÇÃO
    let linha = document.createElement('tr')
    
    //ADICIONA OS VALORES DOS INPUTS NA LINHA
    linha.innerHTML = `
    <td>${nome.value}</td> 
    <td>${numero.value}</td>
    <td>${cpf.value}</td>
    <td>${email.value}</td>
    <td>
        <div class="btnCelula">
            <button class="btnEditar">editar</button>
            <button  class="btnRemover" onclick="removeRow(this)">remover</button>
        </div>
    </td> <!-- FOI ADICIONADO AFUNÇÃO NO BOTÃO-->
    `
    
    //RETIRA OS VALORES DAS CAIXAS DE INPUT 
    nome.value=""
    numero.value=""
    cpf.value=""
    email.value=""
    
    //DECLARA A LINHA COMO FILHO DA TABEALA (adiciona linha na tabela)
    tabela.appendChild(linha)  

    const btnEditar= linha.querySelector('.btnEditar')
    //FUNÇÃO PARA EDITAR UMA LINHA
    btnEditar.addEventListener('click',()=>{
        const inputCelula = linha.querySelectorAll('td')
        nome.value = inputCelula[0].textContent
        numero.value = inputCelula[1].textContent
        cpf.value = inputCelula[2].textContent
        email.value = inputCelula[3].textContent
        
        linha.remove()
        
    })
}
//FUNÇÃO PARA REMOVER UMA LINHA NA TABELA
function removeRow(button){
    const row = button.parentNode.parentNode.parentNode
    row.parentNode.removeChild(row)
}
    

//2°-Função para remover linha 


// querySelector('tagname'): seleciona por tag HTML (ex: 'button', 'div').

// querySelector('.class'): seleciona por classe CSS.

// querySelector('#id'): seleciona por ID.












