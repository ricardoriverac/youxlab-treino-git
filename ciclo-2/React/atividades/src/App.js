import { useEffect, useState } from "react";
import Formulario from "./components/Formulario";
import Tabela from "./components/Tabela";
import { buscarTodos, salvarDado, atualizarDado, deletarDado } from "./services/api";

function App() {
  const [dados, setDados] = useState([]);
  const [idEditando, setIdEditando] = useState(null);
  const [nome, setNome] = useState("");
  const [cpf, setCPF] = useState("");
  const [nascimento, setNascimento] = useState("");

  useEffect(() => {
    carregarDados();
  }, []);

  async function carregarDados() {
    try {
      const resposta = await buscarTodos();
      setDados(resposta.data);
    } catch (error) {
      console.error(error);
    }
  }

  async function salvarPessoa(pessoa) {
    try {
      if (idEditando) {
        await atualizarDado(idEditando, pessoa);
        setIdEditando(null);
      } else {
        await salvarDado(pessoa);
      }
      limparFormulario();
      carregarDados();
    } catch (error) {
      console.error(error);
    }
  }

  function editarPessoa(pessoa) {
    setIdEditando(pessoa.id);
    setNome(pessoa.nome);
    setCPF(pessoa.cpf);
    setNascimento(pessoa.nascimento);
  }

  async function removerPessoa(id) {
    try {
      await deletarDado(id);
      carregarDados();
    } catch (error) {
      console.error(error);
    }
  }

  function limparFormulario() {
    setNome("");
    setCPF("");
    setNascimento("");
  }

  return (
    <div>
      <Formulario
        salvarPessoa={salvarPessoa}
        nome={nome}
        cpf={cpf}
        nascimento={nascimento}
        setNome={setNome}
        setCPF={setCPF}
        setNascimento={setNascimento}
        isEditando={!!idEditando}
      />
      <Tabela
        dados={dados}
        editarPessoa={editarPessoa}
        removerPessoa={removerPessoa}
      />
    </div>
  );
}

export default App;