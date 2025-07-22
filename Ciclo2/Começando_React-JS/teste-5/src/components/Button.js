import { useState } from "react";        // Hook de estado do React

function Button() {
  const [contador, setContador] = useState(0);
  // Cria estado chamado "contador" com valor inicial 0.
  // "setContador" é a função usada para atualizar o valor de "contador".

  function ButtonClicado() {
    alert("Você clicou no Botão!");       //Exibe alerta
    setContador(contador + 1);            // Incrementa o contador
  }

  return (
    <button onClick={ButtonClicado}> Você clicou {contador} vezes! </button>
    // Exibe e atualiza o número de cliques
  );
}

export default Button;
