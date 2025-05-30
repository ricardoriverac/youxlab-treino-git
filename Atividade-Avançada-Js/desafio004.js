const comentarios = [];
const palavrasOfensivas = ["bobo", "feio", "chato",]; 

for (let i = 1; i ; i++) {
  const comentario = prompt(`Digite o comentário ${i}:`);

  if (comentario.toLowerCase() === "cancelar") {
    alert("Processo cancelado pelo usuário.");
    break;
  }

  let possuiPalavraOfensiva = false;
  for (let palavra of palavrasOfensivas) {
    if (comentario.toLowerCase().includes(palavra)) {
      possuiPalavraOfensiva = true;
      break;
    }
  }

  if (possuiPalavraOfensiva) {
    alert("Comentário ignorado por conter palavra ofensiva.");
    continue;
  }

  comentarios.push(comentario);
}

console.log("Comentários válidos:");
console.log(comentarios);
