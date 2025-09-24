import { useEffect, useState } from "react";
import {
  enviarEmailRedefinirSenha,
  logando,
  recuperarSenha,
} from "../services/api";
import { useLocation, useNavigate } from "react-router-dom";
import { toastError, toastSuccess, toastWarning } from "../toasts/toast";
import "./Login.css";
import iconTelaLogin from "../imagem/iconTelaLogin.svg";
import iconConexaoLiteraria from "../imagem/iconConexaoLiteraria.svg";
import iconOlhoAberto from "../imagem/iconOlhoAberto.svg";
import iconOlhoFechado from "../imagem/iconOlhoFechado.svg";
import RedefinirSenha from "../modais/RedefinirSenha";
import { CircularProgress } from "@mui/material";
import institutoYouX from "../imagem/institutoYouX.svg";
import { ToastContainer } from "react-toastify";

export default function Login() {
  const [tipoInput, setTipoInput] = useState(false);
  const [mudarClasse, setMudarClasse] = useState(false);
  const [mudarClasseSenha, setMudarClasseSenha] = useState(false);
  const [valorEmail, setValorEmail] = useState("");
  const [load, setLoad] = useState(false);
  const [valorSenha, setValorSenha] = useState("");
  const [tentativas, setTentativas] = useState(0);
  const [emailRedefinir, setEmailRedefinir] = useState("");
  const [codigoVerificacao, setCodigoVerificacao] = useState("");
  const [exibirEmailSenha, setExibirEmailSenha] = useState(true);
  const [openRedefinirSenha, setOpenRedefinirSenha] = useState(false);
  const [loadEnviarEmail, setLoadEnviarEmail] = useState(false);
  const [novaSenha, setNovaSenha] = useState("");
  const [confirmarSenha, setConfirmarSenha] = useState("");
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    if (tentativas > 0) alteraClasseErro();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [valorEmail, valorSenha]);

  function mostrarSenha() {
    setTipoInput(!tipoInput);
  }

  function alteraClasseErro() {
    setMudarClasse(!(valorEmail !== ""));
    setMudarClasseSenha(!(valorSenha !== ""));
  }

  function validaCampos() {
    return valorEmail !== "" && valorSenha !== "";
  }

  async function entrarSistema() {
    localStorage.removeItem("authToken");
    alteraClasseErro();
    setTentativas(tentativas + 1);
    const isValido = validaCampos();
    if (isValido) { 
      try {
        setLoad(true);
        const objetoLogin = {
          login: valorEmail,
          senha: valorSenha,
        };
        const { data } = await logando(objetoLogin);
        localStorage.setItem("authToken", data);
        navigate("/livros");
      } catch (error) {
        toastError("Usuário ou senha incorretos.");
      } finally {
        setLoad(false);
      }
    }
  }

  async function enviarEmail() {
    if (!validaEmail()) return;
    try {
      setLoadEnviarEmail(true);
      const objEmail = {
        email: emailRedefinir,
      };
      await enviarEmailRedefinirSenha(objEmail);
      setExibirEmailSenha(false);
    } catch (error) {
      toastError("Erro ao enviar email.");
    } finally {
      setLoadEnviarEmail(false);
    }
  }

  async function redefinirSenha() {
    if (!validaCamposRedefinirSenha()) return;
    try {
      const dadosEnviar = {
        codigo: codigoVerificacao,
        novaSenha: novaSenha,
        confirmarSenha: confirmarSenha,
      };
      await recuperarSenha(dadosEnviar);
      toastSuccess("Senha redefinida com sucesso.");
    } catch (error) {
      toastError("Erro ao redefinir senha.");
    } finally {
      setLoadEnviarEmail(false);
      cancelar();
    }
  }

  function validaEmail() {
    if (emailRedefinir === "") {
      toastWarning("Preencha o campo de e-mail.");
      return false;
    }
    const regexEmail =
      /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$/;
    if (!regexEmail.test(emailRedefinir)) {
      toastWarning("E-mail inválido.");
      return false;
    }
    return true;
  }

  function validaCamposRedefinirSenha() {
    if (novaSenha === "" || confirmarSenha === "" || codigoVerificacao === "") {
      toastWarning("Preencha todos os campos.");
      return false;
    }
    if (novaSenha.length < 8 || confirmarSenha < 8) {
      toastWarning("A senha deve ter no mínimo 8 caracteres.");
      return false;
    }
    if (novaSenha !== confirmarSenha) {
      toastWarning("As senhas não coincidem.");
      return false;
    }
    return true;
  }

  function cancelar() {
    setOpenRedefinirSenha(false);
    setExibirEmailSenha(true);
    setEmailRedefinir("");
    setCodigoVerificacao("");
    setNovaSenha("");
    setConfirmarSenha("");
  }

  return (
    <div className="containerLogin">
      <RedefinirSenha
        open={openRedefinirSenha}
        emailRedefinir={emailRedefinir}
        exibirEmailSenha={exibirEmailSenha}
        changeEmail={(e) => setEmailRedefinir(e)}
        codigoVerificacao={codigoVerificacao}
        changeCodigoVerificacao={(e) => setCodigoVerificacao(e)}
        enviarEmail={enviarEmail}
        cancelar={() => cancelar()}
        loadEnviarEmail={loadEnviarEmail}
        novaSenha={novaSenha}
        changeNovaSenha={(e) => setNovaSenha(e)}
        confirmarSenha={confirmarSenha}
        changeConfirmarSenha={(e) => setConfirmarSenha(e)}
        redefinirSenha={redefinirSenha}
      />
      <div className="caixa_img">
        <img src={iconTelaLogin} alt="Imagem Login" />
      </div>

      <div className="caixa_usuario">
        <img src={iconConexaoLiteraria} alt="coneção literária" />

        <div className={mudarClasse ? "erro" : "caixa_input"}>
          <label>Email</label>
          <input
            type="email"
            value={valorEmail}
            onChange={(e) => setValorEmail(e.target.value)}
          />
          {mudarClasse && <p className="texto_erro">Preencha este campo.</p>}
          <label>Senha</label>

          <div className={mudarClasseSenha ? "erro_senha" : "input_senha"}>
            <input
              type={tipoInput ? "text" : "password"}
              value={valorSenha}
              onChange={(e) => setValorSenha(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  entrarSistema();
                }
              }}
            />
            <button onClick={mostrarSenha}>
              <img
                src={tipoInput ? iconOlhoFechado : iconOlhoAberto}
                alt="Visualizar senha"
              />
            </button>
          </div>

          {mudarClasseSenha && (
            <p className="texto_erro">Preencha este campo.</p>
          )}
        </div>
        <button disabled={load} onClick={entrarSistema}>
          {load ? <CircularProgress size={24} color="white" /> : "Entrar"}
        </button>
        <p
          style={{ color: "var(--cor-roxoEscuro)", cursor: "pointer" }}
          onClick={() => setOpenRedefinirSenha(true)}
        >
          Esqueci minha senha
        </p>
        <div className="img_instituto">
          <p>
            Desenvolvido pelo <img src={institutoYouX} alt="Instituto YouX" />
          </p>
        </div>
      </div>
      <ToastContainer />
    </div>
  );
}
