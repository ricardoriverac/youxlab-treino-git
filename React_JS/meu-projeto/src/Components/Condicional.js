import { useState } from "react";

function Condicional() {
  const [email, setEmail] = useState();
  const [userEmail, setUserEmail] = useState()

  function enviarEmail(evento) {
    evento.preventDefault();
    setUserEmail(email)
  }

  function limparEmail(evento){
    // se não houver nada no valor userEmail não entra na Condicional
    setUserEmail('')
  }

  return (
    <div>
      <h2>Cadastre o seu e-mail</h2>
      <form>
        <input
          type="email"
          placeholder="Digite o seu e-mail..."
          onChange={(evento) => setEmail(evento.target.value)}
        ></input>
        <button type="submit" onClick={enviarEmail}>
          Enviar e-mail
        </button>
        {/* Só ocorre se userEmail estiver preenchido */}
        {userEmail &&( 
            <div>
                <p>O e-mail do usuario: {userEmail}</p>
                <button onClick={limparEmail}> Limpar e-mail</button>
            </div>
        )}
      </form>
    </div>
  );
}

export default Condicional;
