import { useState } from "react";

function Form() {

    const [name, setName] = useState() 
    const [password, setPassword] = useState() 


  function cadastrarUsuario(event) {
    event.preventDefault();
    console.log(`Usuário: ${name}`);
    console.log(`Senha: ${password}`);
  }

  return (
    <div>
      <h1>Meu Cadastro:</h1>
      <form onSubmit={cadastrarUsuario}>
        <div>
          <label htmlFor="name">Nome:</label>
          <input
            type="text"
            id="name"
            name="name"
            placeholder="Digite seu nome"
            onChange={(e) => setName(e.target.value)}   // a cada letra digitada, modifica o valor do state 
          />
        </div>
        <div>
          <label htmlFor="password">Senha:</label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Digite sua senha"
            onChange={(e) => setPassword(e.target.value)}   // a cada letra digitada, modifica o valor do state 
          />
        </div>
        <div>
          <input type="submit" value="Cadastrar" />
        </div>
      </form>
    </div>
  );
}

export default Form;
