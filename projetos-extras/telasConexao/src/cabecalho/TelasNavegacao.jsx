import { useNavigate } from "react-router-dom";
import * as React from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import { Link, useLocation } from "react-router-dom";
import "./TelasNavegacao.css";
import Header from "./Header";
import iconLivrosSelecionados from "../img/iconLivrosSelecionados.svg";
import iconLivrosNaoSelecionados from "../img/iconLivrosNaoSelecionados.svg";
import iconDashboardSelecionados from "../img/iconDashboardSelecionados.svg";
import iconDashboardNaoSelecionados from "../img/iconDashboardNaoSelecionados.svg";
import iconAlunosSelecionados from "../img/iconAlunosSelecionados.svg";
import iconAlunosNaoSelecionados from "../img/iconAlunosNaoSelecionados.svg";
import iconEmprestimosSelecionados from "../img/iconEmprestimosSelecionados.svg";
import iconEmprestimosNaoSelecionados from "../img/iconEmprestimosNaoSelecionados.svg";
import iconSobreNaoSelecionado from "../img/iconSobreNaoSelecionado.svg";
import iconSobreSelecionado from "../img/iconSobreSelecionado.svg";
import iconSair from "../img/iconSair.svg";
import Vector from "../img/Vector.svg";

function TelasNavegacao({ children }) {
  const navigate = useNavigate();
  const rota = useLocation();

  const CaminhoLogin = () => {
    localStorage.removeItem("authToken");
    navigate("/login");
  };

  const style = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 400,
    bgcolor: "background.paper",
    border: "none",
    boxShadow: 24,
    height: 156,
    p: 4,
    borderRadius: 10,
  };
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const [windowWidth, setWindowWidth] = React.useState(window.innerWidth);
  const [windowHeight, setWindowHeight] = React.useState(window.innerHeight);

  React.useEffect(() => {
    const handleResize = () => {
      setWindowWidth(window.innerWidth);
      setWindowHeight(window.innerHeight);
    };

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return (
    <div>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography
            id="modal-modal-title"
            className="titulo"
            variant="h4"
            component="h2"
            sx={{ fontFamily: "Roboto" }}
            style={{
              fontFamily: "Ubuntu",
              fontWeight: 800,
              marginTop: 20,
            }}
          >
            Deseja sair ?
          </Typography>
          <div>
            <Button className="btnSairDaModal" onClick={handleClose}>
              <img src={Vector} alt="" />
            </Button>
          </div>
          <Typography
            id="modal-modal-description"
            sx={{ mt: 2 }}
            component={"span"}
          >
            <div className="botoesdaModal">
              <Button
                onClick={handleClose}
                variant="contained"
                style={{
                  color: "#8E58BF",
                  backgroundColor: "#F7F2FA",
                  border: "solid #8E58BF",
                  borderWidth: "0.1em",
                  borderRadius: "0.5em",
                  fontSize: 15,
                  width: 150,
                  fontFamily: "Arial",
                }}
              >
                Cancelar
              </Button>

              <Button
                className="sairModal"
                onClick={CaminhoLogin}
                variant="contained"
                style={{
                  color: "white",
                  backgroundColor: "#8E58BF",
                  border: "solid #8E58BF",
                  fontSize: 15,
                  borderRadius: "0.5em",
                  width: 150,
                  fontFamily: "Arial",
                }}
              >
                Sair
              </Button>
            </div>
          </Typography>
        </Box>
      </Modal>
      <Header />
      <div className="container">
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            height: `${windowHeight - 65}px`,
            width: "80px",
            borderRight: "1px solid var(--cor-cinzaMargin)",
            alignItems: "center",
            justifyContent: "space-between",
          }}
        >
          <div className="div_icones">
            <Link to={"/dashboard"}>
              <img
                src={
                  rota.pathname === "/dashboard"
                    ? iconDashboardNaoSelecionados
                    : iconDashboardSelecionados
                }
                alt="Dashboard"
                title="Dashboard"
              />
            </Link>
            <Link to={"/emprestimo"}>
              <img
                src={
                  rota.pathname === "/emprestimo"
                    ? iconEmprestimosNaoSelecionados
                    : iconEmprestimosSelecionados
                }
                alt="Empréstimos"
                title="Empréstimos"
              />
            </Link>
            <Link to={"/livros"}>
              <img
                src={
                  rota.pathname === "/livros" ||
                  rota.pathname.startsWith("/visualizacaoLivros")
                    ? iconLivrosNaoSelecionados
                    : iconLivrosSelecionados
                }
                alt="Livros"
                title="Livros"
              />
            </Link>
            <Link to={"/alunos"}>
              <img
                src={
                  rota.pathname === "/alunos" ||
                  rota.pathname.startsWith("/visualizacaoAlunos")
                    ? iconAlunosNaoSelecionados
                    : iconAlunosSelecionados
                }
                alt="Alunos"
                title="Alunos"
              />
            </Link>

            <Link to={"/sobre"}>
              <img
                src={
                  rota.pathname === "/sobre"
                    ? iconSobreSelecionado
                    : iconSobreNaoSelecionado
                }
                alt="Sobre" 
                title="Sobre"
                style={{
                  width: 38,
                  marginLeft: 20,
                }}
              />
            </Link>
            <div className="btn_sair">
              <Button className="sair" onClick={handleOpen} title="Sair">
                <img src={iconSair} alt="Sair" />
              </Button>
            </div>
          </div>
        </div>
        <div
          style={{
            width: `${windowWidth - 80}px`,
            height: `${windowHeight - 65}px`,
          }}
        >
          {children}
        </div>
      </div>
    </div>
  );
}

export default TelasNavegacao;
