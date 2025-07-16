import { useState } from "react"; // useState() --> responsável por variáveis mutáveis

function Condicional_if() {
  const [estaLogado, setEstaLogado] = useState(false); // pode-se modificar o valor dessas variáveis

  // "estaLogado" var que recebe o valor false (deslogado)
  // "setEstaLogado" função que muda o valor de "estaLogado" 

  return (
    <>
      <h1>Exemplo: Renderização Condicional com Login </h1>

      <button onClick={() => setEstaLogado(!estaLogado)}>     {/*Ao clicar o valor de "estaLogado" muda*/}
        {estaLogado ? "logout" : "login"}                     {/* Se valor de "estaLogado" for true "Logout", Se não "Login" */}
      </button>

        <h2>
            {estaLogado
            ? "Bem Vindo de Volta!"
            : "Olá! Faça o login para continuar"}
        </h2>
    </>
  );
}

export default Condicional_if;
