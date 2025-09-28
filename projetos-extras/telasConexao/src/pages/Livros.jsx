import "./Livros.css";
import lupa from "../imagem/lupa.svg";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  buscarLivros,
  buscarGeneros,
  buscarTodosAlunos,
  efetuandoEmprestimo,
  cadastrarLivro,
} from "../services/api";
import Tabela from "../tabelas/Tabela";
import iconVisualizar from "../imagem/iconVisualizar.svg";
import iconEmprestar from "../imagem/iconEmprestar.svg";
import EmprestarLivro from "../modais/EmprestarLivro";
import InputAutoComplete from "../Componets/InputAutoComplete";
import CadastrarLivro from "../modais/CadastrarLivro";
import { ToastContainer } from "react-toastify";
import { toastError, toastSuccess, toastWarning } from "../toasts/toast";
import { hoje } from "../modais/RenovarEmprestimo";
import formatarDate from "../utils/formataData";
import validaData from "../utils/ValidaData";
import { limparMascara } from "../utils/formataInputTelefoneVazio";

export default function Livros() {
  const [dadosLivros, setDadosLivros] = useState([]);
  const [dadosFormatadosLivros, setDadosFormatadosLivros] = useState([]);
  const [generoOpcoes, setGeneroOpcoes] = useState([]);
  const [generoSelecionado, setGeneroSelecionado] = useState(null);
  const [valorBusca, setValorBusca] = useState("");
  const [qtdLivrosPag, setQtdLivrosPag] = useState(null);
  const [loadingPagina, setLoadingPagina] = useState(false);
  const [verificarModal, setVerificarModal] = useState(false);
  const [loadCadastro, setLoadCadastro] = useState(false);
  const [nomesAlunos, setNomesAlunos] = useState([]);
  const [informacoesLivro, setInformacoesLivro] = useState([]);
  const [dataDevolvendo, setDataDevolvendo] = useState(0);
  const [alunoSelecionado, setAlunoSelecionado] = useState(null);
  const [nomeNovoAluno, setNomeNovoAluno] = useState("");
  const [telefoneNovoAluno, setTelefoneNovoAluno] = useState("");
  const [modalCdastrarLivrosOpen, setModalCdastrarLivrosOpen] = useState(false);
  const [atualizarCadastro, setAtualizarCadastro] = useState(false);

  const navigate = useNavigate();

  const colunasLivros = [
    "titulo",
    "autor",
    "genero",
    "disponibilidade",
    "localizacao",
    "acoes",
  ];

  const estiloTabelaLivros = {
    height: "130%",
    width: "100%",
    margin: "0 auto",
    border: "1px solid var(--cor-cinzaMargin)",
    borderRadius: 2,
  };

  const acoes = [
    {
      texto: "Emprestar",
      icon: iconEmprestar,
      func: (e) => acaoEmprestar(e),
    },
    {
      texto: "Visualizar",
      icon: iconVisualizar,
      func: (e) => acaoVisualizar(e),
    },
  ];

  useEffect(() => {
    carregarDadosLivros();
    carregarGenero();
    buscarNomeAlunos();
    // eslint-disable-next-line
  }, []);

  useEffect(() => {
    formataDadosLivros();
    // eslint-disable-next-line
  }, [dadosLivros]);

  useEffect(() => {
    carregarDadosLivros();
    // eslint-disable-next-line
  }, [generoSelecionado]);

  useEffect(() => {
    if (valorBusca === "") {
      carregarDadosLivros();
    }
    // eslint-disable-next-line
  }, [valorBusca]);

  useEffect(() => {
    carregarDadosLivros();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [atualizarCadastro]);

  useEffect(() => {
    carregarDadosLivros();
    // eslint-disable-next-line
  }, [verificarModal]);

  async function carregarDadosLivros(pagina = 1, limite = 10) {
    try {
      setLoadingPagina(true);
      const filtroLivros = {
        id_genero: generoSelecionado?.id,
        titulo: valorBusca,
      };
      const { data } = await buscarLivros(limite, pagina, filtroLivros);
      setDadosLivros(data.livros);
      setQtdLivrosPag(data.quantidadeLivros);
    } catch (error) {
      toastError("Erro ao carregar livros");
    } finally {
      setLoadingPagina(false);
    }
  }

  async function carregarGenero() {
    try {
      const { data } = await buscarGeneros();
      formataGenero(data);
    } catch (error) {
      toastError("Erro ao carregar gêneros");
    }
  }

  async function cadastrandoLivros(dados) {
    try {
      setLoadCadastro(true);
      await cadastrarLivro(dados);
      toastSuccess("Livro cadastrado com sucesso!");
      setModalCdastrarLivrosOpen(false);
      setAtualizarCadastro(!atualizarCadastro);
    } catch (err) {
      toastError("Erro ao cadastrar livro");
    } finally {
      setLoadCadastro(false);
    }
  }

  async function buscarNomeAlunos() {
    try {
      const { data } = await buscarTodosAlunos();
      acessandoNomes(data);
    } catch (error) {
      toastError("Erro ao buscar alunos");
    }
  }

  async function fazendoEmprestimo() {
    if (validaData(dataDevolvendo)) {
      setVerificarModal(true);
      return;
    }

    try {
      let objEmprestar = {
        id_livro: informacoesLivro?.id,
        id_aluno: !alunoSelecionado ? null : alunoSelecionado?.id,
        nomeNovoAluno: nomeNovoAluno,
        telefoneNovoAluno: limparMascara(telefoneNovoAluno),
        dataAtual: hoje(),
        dataEntrega: formatarDate(dataDevolvendo),
      };
      await efetuandoEmprestimo(objEmprestar);
      await carregarDadosLivros();
      toastSuccess("Empréstimo efetuado com sucesso");
      setVerificarModal(false);
    } catch (error) {
      if (error.response.data === "Quantidade de livros insuficientes") {
        toastWarning("Quantidade de livros insuficientes");
      } else {
        toastError("Erro ao emprestar livro");
      }
    }
  }

  function acessandoNomes(nomes) {
    let dadosNomes = [];
    // eslint-disable-next-line
    nomes.map((nome) => {
      dadosNomes.push({
        ...nome,
        label: nome.nome,
      });
    });
    setNomesAlunos(dadosNomes);
  }

  function formataGenero(generos) {
    let objGeneros = [];
    // eslint-disable-next-line
    generos.map((genero) => {
      objGeneros.push({
        ...genero,
        label: genero.nome,
      });
    });
    setGeneroOpcoes(objGeneros);
  }

  function calcularDisponibilidade(qtdLivros, qtdEmprestado) {
    return qtdLivros - qtdEmprestado;
  }

  
  function formataDadosLivros() {
    let objRetorno = [];
    // eslint-disable-next-line
    dadosLivros?.map((c) => {
      objRetorno.push({
        id: c.id,
        titulo: c.titulo,
        autor: c.autor,
        genero: c?.genero?.map((e) => e.nome + " "),
        disponibilidade: calcularDisponibilidade(
          c.quantidadeLivros,
          c.quantidadeEmprestado
        ),
        localizacao: c.localizacaoPratileira,
      });
    });
    setDadosFormatadosLivros(objRetorno);
  }

  function acaoEmprestar(dados) {
    setVerificarModal(true);
    setInformacoesLivro(dados);
  }

  function acaoVisualizar(dados) {
    navigate(`/visualizacaoLivros/${dados.id}`);
  }

  function calculadorQtdPaginas() {
    const limiteLivros = 10;
    const totalPaginasLivros = Math.ceil(qtdLivrosPag / limiteLivros);
    return totalPaginasLivros;
  }

  function clickPaginacao(event, value) {
    carregarDadosLivros(value);
  }

  function cancelar() {
    setVerificarModal(false);
    setModalCdastrarLivrosOpen(false);
    limpandoCampos();
  }

  function limpandoCampos() {
    setAlunoSelecionado(null);
    setNomeNovoAluno(null);
    setTelefoneNovoAluno(null);
    setDataDevolvendo(null);
  }

  return (
    <div className="container_livro">
      <ToastContainer />
      <EmprestarLivro
        open={verificarModal}
        cancelar={cancelar}
        emprestar={fazendoEmprestimo}
        titulo={informacoesLivro?.titulo}
        dataDevolvendo={dataDevolvendo}
        setDataDevolvendo={setDataDevolvendo}
        options={nomesAlunos}
        alunoSelecionado={alunoSelecionado}
        setAlunoSelecionado={setAlunoSelecionado}
        nomeNovoAluno={nomeNovoAluno}
        setNomeNovoAluno={setNomeNovoAluno}
        telefoneNovoAluno={telefoneNovoAluno}
        setTelefoneNovoAluno={setTelefoneNovoAluno}
      />
      <CadastrarLivro
        load={loadCadastro}
        open={modalCdastrarLivrosOpen}
        cancelar={cancelar}
        cadastrar={(e) => cadastrandoLivros(e)}
        options={generoOpcoes}
      />
      <div className="caixa_livro">
        <h1>Livros</h1>
        <button onClick={() => setModalCdastrarLivrosOpen(true)}>
          Cadastrar livro
        </button>
      </div>

      <div className="caixa_filtros">
        <div className="input_buscar">
          <input
            type="text"
            placeholder="Buscar livro"
            value={valorBusca}
            onChange={(e) => setValorBusca(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                carregarDadosLivros();
              }
            }}
          />
          <button onClick={() => carregarDadosLivros()}>
            <img src={lupa} alt="lupa de pesquisa" />
          </button>
        </div>
        <div style={{ width: "20%" }}>
          <InputAutoComplete
            options={generoOpcoes}
            placeholder="Gênero"
            value={generoSelecionado}
            change={(e) => setGeneroSelecionado(e)}
            style={{
              "& .MuiOutlinedInput-root": {
                borderColor: "--cor-cinzaMargin",
                borderRadius: "0.8em",
                height: "3em",
              },
            }}
          />
        </div>
      </div>

      <div className="caixa_tabela">
        {dadosLivros.length === 0 ? (
          <span> Nenhum dado encontrado.</span>
        ) : (
          <Tabela
            dados={dadosFormatadosLivros}
            colunas={colunasLivros}
            estiloTabela={estiloTabelaLivros}
            qtdPaginas={calculadorQtdPaginas()}
            clickPaginacao={clickPaginacao}
            acoes={acoes}
            carregandoPagina={loadingPagina}
          />
        )}
      </div>
    </div>
  );
}
