function inserirLinha() {
    // Pegando os valores dos inputs
    const nome = document.getElementById("inputNome").value; //document.getElementById() para pegar os valores desses campos e os armazenamos em variáveis.
    const telefone = document.getElementById("inputNumeroTelefone").value;
    const cpf = document.getElementById("inputCpf").value;
    const email = document.getElementById("inputEmail").value;

    // Verificar se os campos não estão vazios
    if (!nome || !telefone || !cpf || !email) {
        alert("Por favor, preencha todos os campos!"); //Se algum campo estiver vazio, ele exibe um alerta pedindo para o usuário preencher todos os campos e sai da função com return
        return;
    }

    // Criar nova linha na tabela
    const tabela = document.getElementById("tabela").getElementsByTagName('tbody')[0];//a função pega o elemento da tabela com getElementById('tabela'), depois encontra o corpo da tabela (<tbody>) com getElementsByTagName('tbody')[0]
    const novaLinha = tabela.insertRow();//insertRow() é utilizada para adicionar uma nova linha

    // Adicionando os valores nas células da nova linha
    // interpolação de strings)para criar os elementos de células (<td>) na nova linha.
    // Usando template literals para colocar os dados nas células da tabela. 
    // O $ e {} é onde estamos colocando as variáveis (como nome, telefone, etc.) diretamente na string.-->

    novaLinha.innerHTML = `
        <td>${nome}</td>
        <td>${telefone}</td>
        <td>${cpf}</td>
        <td>${email}</td>
        <td>
            <button class="btnEditar" onclick="editarLinha(this)">Editar</button>
            <button class="btnRemover" onclick="removerLinha(this)">Remover</button>
        </td>
    `;


    // impar os campos após adicionar
    document.getElementById("inputNome").value = '';
    document.getElementById("inputNumeroTelefone").value = '';
    document.getElementById("inputCpf").value = '';
    document.getElementById("inputEmail").value = '';
}

// Função para remover uma linha
function removerLinha(botao) {
    // Encontrar a linha (tr) que contém o botão "Remover"
    const linha = botao.closest('tr'); //closest puxa o elemeto mais proximo, que seria "tr"
    linha.remove();
}

/// Variável global para armazenar a linha selecionada para edição
let linhaSelecionada = null; //null é usado para indicar que nenhuma linha foi selecionada ainda
//let foi usado para poder ser modificado
// Função para editar uma linha
function editarLinha(botao) {
    // Encontrar a linha (tr) que contém o botão "Editar"
    const linha = botao.closest('tr');
    
    // Obter os valores atuais da linha
    const nome = linha.cells[0].textContent; //cells: É uma coleção de todas as células (<td>) dentro da linha (<tr>).
    const telefone = linha.cells[1].textContent; // textContent extrai o texto visível dentro dessa célula.
    const cpf = linha.cells[2].textContent; //O [] mostra qual campo/indice/celula ele está.
    const email = linha.cells[3].textContent;

    // Colocar os valores nos campos do formulário para edição
    document.getElementById("inputNome").value = nome;
    document.getElementById("inputNumeroTelefone").value = telefone;
    document.getElementById("inputCpf").value = cpf;
    document.getElementById("inputEmail").value = email;

    // Alterar o texto do botão "Inserir" para "Atualizar"
    const botaoInserir = document.getElementById('botaoInserir');
    botaoInserir.textContent = "Atualizar"; // Mudamos o texto do botão
    botaoInserir.setAttribute('onclick', 'atualizarLinha()'); //setAttribute é um método utilizado para modificar um elemento html

    // Armazenar a linha selecionada para edição
    linhaSelecionada = linha;
}

// Função para atualizar a linha com os novos valores
function atualizarLinha() {
  if (linhaSelecionada === null) {
    alert("Nenhuma linha selecionada para editar.");
    return;
  }

  // Pegando os novos valores dos inputs
  const nome = document.getElementById('inputNome').value;
  const telefone = document.getElementById('inputNumeroTelefone').value;
  const cpf = document.getElementById('inputCpf').value;
  const email = document.getElementById('inputEmail').value;

  // Atualizando as células da linha com os novos dados
  linhaSelecionada.cells[0].textContent = nome;
  linhaSelecionada.cells[1].textContent = telefone;
  linhaSelecionada.cells[2].textContent = cpf;
  linhaSelecionada.cells[3].textContent = email;

  // Voltar o botão para "Inserir" 
  const botaoInserir = document.getElementById('botaoInserir');
  botaoInserir.textContent = "Inserir";
  botaoInserir.removeEventListener('click', atualizarLinha);
  botaoInserir.addEventListener('click', inserirLinha);//Aqui ele chama a funçao inserirLinha dnv.

  // Limpando os campos do formulário
  document.getElementById('inputNome').value = '';
  document.getElementById('inputNumeroTelefone').value = '';
  document.getElementById('inputCpf').value = '';
  document.getElementById('inputEmail').value = '';

  // Resetar a linha selecionada
  linhaSelecionada = null; //null é usado pois ele não ha um valor existente, nenhum valor.
}