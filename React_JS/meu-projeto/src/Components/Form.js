function Form() {
  function cadastrarUsuario(event) {
    event.preventDefault(); 
    console.log("Usuário Cadastrado!");
  }

  return (
    <div>
      <h1>Meu Cadastro:</h1>
      <form onSubmit={cadastrarUsuario}>
        <div>
          <input type="text" placeholder="Digite seu nome" />
        </div>
        <div>
          <input type="submit" value="Cadastrar" />
        </div>
      </form>
    </div>
  );
}

export default Form;
