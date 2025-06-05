function validarSenha(senha) {
  const erros = [];

  // Verificações
  let temMaiuscula = false;
  let temNumero = false;
  let temEspecial = false;
  const especiais = "!@#$%";

  for (let i = 0; i < senha.length; i++) {
    const c = senha[i];

    if (c >= 'A' && c <= 'Z') {
      temMaiuscula = true;
    }

    if (c >= '0' && c <= '9') {
      temNumero = true;
    }

    if (especiais.includes(c)) {
      temEspecial = true;
    }
  }

  if (senha.length < 8) {
    erros.push("A senha deve ter pelo menos 8 caracteres.");
  }

  if (!temMaiuscula) {
    erros.push("A senha deve conter pelo menos uma letra maiúscula.");
  }

  if (!temNumero) {
    erros.push("A senha deve conter pelo menos um número.");
  }

  if (!temEspecial) {
    erros.push("A senha deve conter pelo menos um caractere especial (!@#$%).");
  }

  return erros;
}

// Loop de repetição
let senhaValida = false;
let senha;

do {
  senha = prompt("Digite sua senha:");
  const erros = validarSenha(senha);

  if (erros.length === 0) {
    senhaValida = true;
    alert("✅ Senha válida!");
  } else {
    alert("❌ Senha inválida:\n" + erros.join("\n"));
  }
} while (!senhaValida);
