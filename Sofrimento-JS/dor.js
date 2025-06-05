function adicionar() {
  const nome = document.getElementById('nome').value.trim();
  const cpf = document.getElementById('cpf').value.trim();
  const numero = document.getElementById('numero').value.trim();
  const email = document.getElementById('email').value.trim();

  const tabela = document.getElementById('tabela').getElementsByTagName('tbody')[0];
  const novaLinha = tabela.insertRow();

// insere uma nova célula ( <td>) em uma linha da tabela ( <tr>)
  const celulaNome = novaLinha.insertCell(0);
  const celulaCpf = novaLinha.insertCell(1);
  const celulaNumero = novaLinha.insertCell(2);
  const celulaEmail = novaLinha.insertCell(3);
  const celulaBotao = novaLinha.insertCell(4); // coluna para o botão de remover 

  //adicio a uma coluna 
  celulaNome.textContent = nome;
  celulaCpf.textContent = cpf;
  celulaNumero.textContent = numero;
  celulaEmail.textContent = email;

  //botão utilizado para apagar a linha criada na tabela
  const botao= document.createElement("button");
  botao.textContent = "Remover";
  botao.onclick = function () {
    this.parentElement.parentElement.remove(); // Remove a nova linha criada
  };

  celulaBotao.appendChild(botao);


  document.getElementById('nome').value = '';
  document.getElementById('cpf').value = '';
  document.getElementById('numero').value = '';
  document.getElementById('email').value = '';
}
