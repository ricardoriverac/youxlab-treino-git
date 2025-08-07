import { Container, Box, TextField, Alert, Stack } from "@mui/material";
import "./TelaLogin.module.css";
import Titulo from "./Titulo";
import Button from "@mui/material/Button";
import Divider from "@mui/material/Divider";
import Chip from "@mui/material/Chip";
import { useNavigate } from "react-router-dom";
import LoginIcon from "@mui/icons-material/Login";
import PersonAddIcon from "@mui/icons-material/PersonAdd";
import { useState } from "react";
import Senha from "./Senha";

function TelaLogin() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [nome, setNome] = useState("")
  const [senha, setSenha] = useState("");
  const [alerta, setAlerta] = useState(false);
  const [cadastro, setCadastro] = useState(false);

  function Alerta(){
    setCadastro(true)
    return
  }

  function RotaCriarConta() {
    return navigate("/criarconta");
  }

  function Verificar() {
    fetch(`http://localhost:3000/usuarios?email=${email}`)
      .then((resp) => resp.json())
      .then((data) => {
        if (data.length === 0) {
          Alerta()
        }
        const usuario = data[0];
        console.log(senha);
        const nomeUsuario = usuario.nome
        console.log(nomeUsuario)

        if (usuario.senha === senha) {
          alert("Seja bem-vindo");
          navigate("/bibliotecavirtual", {
            state: {
              nome:nomeUsuario
            }
          });
        } else {
          setAlerta(true);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }

  return (
    <Container
      maxWidth="sm"
      sx={{
        justifyContent: "center",
        display: "flex",
        alignItems: "center",
        margin: "auto",
        marginTop: "50px",
      }}
    >
      <Box
        component="section"
        sx={{
          height: "80vh",
          boxShadow: "1px 1px 8px 1px #AA60C8",
          display: "flex",
          flexDirection: "column",
          bgcolor: "#fff",
        }}
        >
        {cadastro ? (
          <Stack sx={{ width: "100%" }} spacing={2}>
            <Alert variant="filled" severity="info">
              Essa conta não está cadastrada.
            </Alert>
          </Stack>
        ) : (
          <></>
        )}

        {alerta ? (
          <Stack sx={{ width: "100%" }} spacing={2}>
            <Alert variant="filled" severity="error">
              Senha incorreta!
            </Alert>{" "}
          </Stack>
        ) : (
          <></>
        )}

        <Titulo
          titulo="Biblioteca Virtual"
          label="Faça login para acessar o sistema"
        />
        <TextField
          onChange={(e) => setEmail(e.target.value)}
          id="email-basic"
          label="Email*"
          variant="outlined"
          sx={{
            width: "500px",
            display: "flex",
            justifyContent: "center",
            marginTop: "50px",
            margin: "25px",
          }}
        />

        <Senha onChange={(e) => setSenha(e.target.value)} alerta={alerta} />

        {/* <TextField onChange={(e) => setSenha(e.target.value)}
          id="senha-basic"
          label="Senha*"
          variant="outlined"
          type="password"
          sx={{
            width: "50 <Senha onChange={(e) => setSenha(e.target.value)}/>0px",
            display: "flex",
            justifyContent: "center",
            marginTop: "50px",
            margin: "25px",
          }}
        /> */}

        <Button
          onClick={Verificar}
          variant="contained"
          sx={{
            width: "500px",
            margin: "25px",
            bgcolor: "#AA60C8",
          }}
        >
          <LoginIcon />
          Entrar
        </Button>

        <Divider>
          <Chip label="Ou" size="small" />
        </Divider>

        <Button
          variant="outlined"
          onClick={RotaCriarConta}
          sx={{
            width: "500px",
            margin: "25px",
            color: "#AA60C8",
            border: "1px solid #AA60C8",
          }}
        >
          <PersonAddIcon />
          Criar conta
        </Button>
      </Box>
    </Container>
  );
}

export default TelaLogin;
