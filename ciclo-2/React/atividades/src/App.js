import { useEffect, useState } from "react";
import Formulario from "./components/Formulario";
import Tabela from "./components/Tabela";
import { buscarTodos, salvarDado, deletarDado } from "./services/api";

function App() {
  const [dados, setDados] = useState([]);
  const [nome, setNome] = useState("");
  const [cpf, setCPF] = useState("");
  const [nascimento, setNascimento] = useState("");

  useEffect(() => {
    carregarDados();
  }, []);

  async function salvarPessoa(novaPessoa) {
    await salvarDado(novaPessoa);
    carregarDados();
  }

  async function carregarDados() {
    try {
      const resposta = await buscarTodos();
      setDados(resposta.data);
    } catch (error) {
      console.error(error);
    }
  }

  async function removerPessoa(id) {
    try {
      await deletarDado(id);
      carregarDados();
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div>
      <Formulario
        salvarPessoa={salvarPessoa}
        dados={dados}
        setDados={setDados}
        nome={nome}
        nascimento={nascimento}
        cpf={cpf}
        setNome={setNome}
        setCPF={setCPF}
        setNascimento={setNascimento}
      />
      <Tabela
        dados={dados}
        setNome={setNome}
        setCPF={setCPF}
        setNascimento={setNascimento}
        removerPessoa={removerPessoa}
      />
    </div>
  );
}

export default App;