import { useState } from "react";

function Form() {
  function cadastrarUsuario(e) {
    e.preventDefault();
    console.log(`Usuario ${name} foi cadastrado com a senha ${password}`);
  }

  const [name, setName] = useState()
  const [password , setPassworrd] = useState()
  return (
    <>
      <h1>Meu cadastro:</h1>
      <form onSubmit={cadastrarUsuario}>
        <label htmlFor="name">Nome:</label>
        <>
          <input
            type="text"
            id="name"
            name="name"
            placeholder="Qual é o seu nome?"
            value={name}
            onChange={(e)=> setName(e.target.value)}
          />
        </>
        <label htmlFor="password">Senha:</label>
        <>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Digite a sua senha:"
            onChange={(e)=> setPassworrd(e.target.value)}

          />
        </>
        <>
          <input type="submit" value="Cadastrar" />
        </>
      </form>
    </>
  );
}

export default Form;
