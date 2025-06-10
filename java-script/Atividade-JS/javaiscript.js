function adicionar() {
  const nome = document.getElementById('nome').value.trim();
  const numero = document.getElementById('numero').value.trim();
  const cpf = document.getElementById('cpf').value.trim();
  const email = document.getElementById('email').value.trim();

  if (!nome || !cpf || !numero || !email) {
    alert("Preencha todos os campos!");
    return;
  }

  // Validação extra do e-mail
  if (!validarEmailCampo(email)) {
    alert("Email inválido!");
    return;
  }

  const tabela = document.getElementById('tabela').getElementsByTagName('tbody')[0];
  const novaLinha = tabela.insertRow();

  const celulaNome = novaLinha.insertCell(0);
  const celulaNumero = novaLinha.insertCell(1);
  const celulaCpf = novaLinha.insertCell(2);
  const celulaEmail = novaLinha.insertCell(3);
  const celulaBotoes = novaLinha.insertCell(4);

  celulaNome.textContent = nome; 
  celulaNumero.textContent = numero;
  celulaCpf.textContent = cpf;
  celulaEmail.textContent = email;

  const botaoRemover = document.createElement("button");
  botaoRemover.textContent = "Remover";
  botaoRemover.classList.add('remover');
  botaoRemover.onclick = function () {
    this.parentElement.parentElement.remove();
  };

  const botaoEditar = document.createElement("button");
  botaoEditar.textContent = "Editar";
  botaoEditar.classList.add('editar');
  botaoEditar.onclick = function () {
    document.getElementById('nome').value = celulaNome.textContent;
    document.getElementById('numero').value = celulaNumero.textContent;
    document.getElementById('cpf').value = celulaCpf.textContent;
    document.getElementById('email').value = celulaEmail.textContent;
    novaLinha.remove();
  };

  celulaBotoes.appendChild(botaoEditar);
  celulaBotoes.appendChild(botaoRemover);

  // Limpa os campos
  document.getElementById('nome').value = '';
  document.getElementById('numero').value = '';
  document.getElementById('cpf').value = '';
  document.getElementById('email').value = '';
}

// Máscara CPF
function formatarCPF(campo) {
  let valor = campo.value.replace(/\D/g, '');
  valor = valor.replace(/(\d{3})(\d)/, '$1.$2');
  valor = valor.replace(/(\d{3})(\d)/, '$1.$2');
  valor = valor.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
  campo.value = valor;
}

// Máscara telefone
function formatarTelefone(campo) {
  let valor = campo.value.replace(/\D/g, '');
  valor = valor.replace(/^(\d{2})(\d)/g, '($1) $2');
  valor = valor.replace(/(\d{5})(\d{4})$/, '$1-$2');
  campo.value = valor;
}

// Validação visual de e-mail
function validarEmail(campo) {
  const email = campo.value;
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  campo.style.borderColor = email && !regex.test(email) ? 'red' : '';
}

// Validação lógica de e-mail
function validarEmailCampo(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}