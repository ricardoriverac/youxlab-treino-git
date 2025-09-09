import { salvarNovaPessoa, verificarLogin } from "../services/api";
import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import "./Login.css";

function Login() {
  const [isSignUp, setIsSignUp] = useState(false);
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [emailEntrar, setEmailEntrar] = useState("");
  const [senhaEntrar, setSenhaEntrar] = useState("");

  const navigate = useNavigate();

  async function cadastrarPessoa() {
    let pessoaCadastrada = {
      nome: nome,
      email: email,
      senha: senha,
    };

    if (
      pessoaCadastrada.nome === "" ||
      pessoaCadastrada.email === "" ||
      pessoaCadastrada.senha === ""
    ) {
      alert("Preencha todos os dados!");
    } else {
      try {
        await salvarNovaPessoa(pessoaCadastrada);
        navigate("/home");
      } catch (err) {
        console.log("err :>> ", err);
      }
    }

    setNome("");
    setEmail("");
    setSenha("");
  }

  async function entrar() {
    let dadosEntrar = {
      email: emailEntrar,
      senha: senhaEntrar,
    };

    try {
      const { data } = await verificarLogin(dadosEntrar);
      console.log("logar :>> ", data);
      if (data === true) {
        navigate("/home");
      } else {
        alert("Deu ruim");
      }
    } catch (err) {
      console.log("err :>> ", err);
    }

    setEmailEntrar("");
    setSenhaEntrar("");
  }

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <div
        id="container"
        className={`container ${isSignUp ? "right-panel-active" : ""}`}
      >
        <div className="form-container sign-up-container">
          <form onSubmit={(e) => e.preventDefault()}>
            <h1>Cadastrar</h1>
            <input
              type="text"
              placeholder="Nome"
              onChange={(e) => setNome(e.target.value)}
              value={nome}
            />
            <input
              type="email"
              placeholder="E-mail"
              onChange={(e) => setEmail(e.target.value)}
              value={email}
            />
            <input
              type="password"
              placeholder="Senha"
              onChange={(e) => setSenha(e.target.value)}
              value={senha}
            />
            <button type="submit" onClick={cadastrarPessoa}>
              Cadastrar
            </button>
          </form>
        </div>

        <div className="form-container sign-in-container">
          <form onSubmit={(e) => e.preventDefault()}>
            <h1>Entrar</h1>
            <input
              type="email"
              placeholder="E-mail"
              onChange={(e) => setEmailEntrar(e.target.value)}
              value={emailEntrar}
            />
            <input
              type="password"
              placeholder="Senha"
              onChange={(e) => setSenhaEntrar(e.target.value)}
              value={senhaEntrar}
            />
            <button type="submit" onClick={entrar}>
              Entrar
            </button>
          </form>
        </div>

        <div className="overlay-container">
          <div className="overlay">
            <div className="overlay-panel overlay-left">
              <h1>Olá, amigo!</h1>
              <p>Insira seus dados pessoais e comece sua jornada conosco!</p>
              <p>Ou entre na sua conta.</p>
              <button className="ghost" onClick={() => setIsSignUp(false)}>
                Entrar
              </button>
            </div>
            <div className="overlay-panel overlay-right">
              <h1>Bem-vindo de volta!</h1>
              <p>
                Para continuar conectado com a gente, faça login com suas
                informações.
              </p>
              <p>Caso não tenha uma conta cadastre-se abaixo.</p>
              <button className="ghost" onClick={() => setIsSignUp(true)}>
                Cadastro
              </button>
            </div>
          </div>
        </div>
      </div>
      <Link to="/home">ir pra home</Link>
    </div>
  );
}

export default Login;
