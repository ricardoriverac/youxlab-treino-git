import { useState, useEffect } from "react";
import Forms from "./components/Forms";
import Tabela from "./components/Tabela";
import Filter from "./components/Filter";
import ModalEditar from "./components/ModalEditar";
import {
  buscarTarefas,
  adicionarTarefa,
  atualizarTarefa,
  excluirTarefa,
} from "./services/api";

function App() {
  const [tarefas, setTarefas] = useState([]);
  const [nome, setNome] = useState("");
  const [categoria, setCategoria] = useState("");
  const [dataEntrega, setDataEntrega] = useState("");
  const [isEditando, setIsEditando] = useState(false);
  const [tarefaEditando, setTarefaEditando] = useState(null);

  const [filter, setFilter] = useState("todas");
  const [filterCategoria, setFilterCategoria] = useState("");
  const [ordenacao, setOrdenacao] = useState("recentes");

  const [modalAberto, setModalAberto] = useState(false);

  useEffect(() => {
    const carregarTarefas = async () => {
      try {
        const resposta = await buscarTarefas();
        const tarefasComStatus = resposta.data.map(calcularStatus);
        setTarefas(tarefasComStatus);
      } catch (error) {
        console.error("Erro ao buscar tarefas:", error);
      }
    };
    carregarTarefas();
  }, []);

  const calcularStatus = (tarefa) => {
    const hoje = new Date();
    const data = new Date(tarefa.dataEntrega);
    let status = tarefa.status;

    if (status !== "concluida") {
      status = data < hoje ? "atrasada" : "pendente";
    }

    return { ...tarefa, status };
  };

  const alternarConclusao = async (tarefa) => {
    try {
      const novoStatus =
        tarefa.status === "concluida" ? "pendente" : "concluida";
      const tarefaAtualizada = { ...tarefa, status: novoStatus };

      await atualizarTarefa(tarefa.id, tarefaAtualizada);

      setTarefas(
        tarefas.map((t) =>
          t.id === tarefa.id ? { ...t, status: novoStatus } : t
        )
      );
    } catch (error) {
      console.error("Erro ao atualizar conclusão:", error);
    }
  };

  const salvarTarefa = async (tarefa) => {
    try {
      if (isEditando) {
        await atualizarTarefa(tarefaEditando.id, tarefa);

        const atualizadas = tarefas.map((t) =>
          t.id === tarefaEditando.id
            ? calcularStatus({ ...tarefaEditando, ...tarefa })
            : t
        );

        setTarefas(atualizadas);
        setIsEditando(false);
        setTarefaEditando(null);
      } else {
        const resposta = await adicionarTarefa({
          ...tarefa,
          dataCriacao: new Date(),
        });
        const nova = calcularStatus(resposta.data);
        setTarefas([...tarefas, nova]);
      }

      setNome("");
      setCategoria("");
      setDataEntrega("");
    } catch (error) {
      console.error("Erro ao salvar tarefa:", error);
    }
  };

  const editarTarefa = (t) => {
    setTarefaEditando(t);
    setModalAberto(true);
  };

  const salvarEdicao = async (tarefaAtualizada) => {
    try {
      await atualizarTarefa(tarefaAtualizada.id, tarefaAtualizada);
      const atualizadas = tarefas.map((t) =>
        t.id === tarefaAtualizada.id ? calcularStatus(tarefaAtualizada) : t
      );
      setTarefas(atualizadas);
    } catch (error) {
      console.error("Erro ao salvar edição:", error);
    }
  };

  const removerTarefa = async (id) => {
    try {
      await excluirTarefa(id);
      setTarefas(tarefas.filter((t) => t.id !== id));
    } catch (error) {
      console.error("Erro ao remover tarefa:", error);
    }
  };

  const tarefasFiltradasEOrdenadas = () => {
    let lista = [...tarefas];

    if (filter === "pendentes") {
      lista = lista.filter(
        (t) => t.status === "pendente" || t.status === "atrasada"
      );
    } else if (filter === "concluidas") {
      lista = lista.filter((t) => t.status === "concluida");
    } else if (filter === "categoria" && filterCategoria) {
      lista = lista.filter((t) => t.categoria === filterCategoria);
    }

    if (ordenacao === "recentes") {
      lista.sort((a, b) => b.dataCriacao - a.dataCriacao);
    } else if (ordenacao === "entrega") {
      lista.sort((a, b) => new Date(a.dataEntrega) - new Date(b.dataEntrega));
    } else if (ordenacao === "alfabetica") {
      lista.sort((a, b) => a.nome.localeCompare(b.nome));
    }

    return lista;
  };

  return (
    <div>
      <h1>Lista de Tarefas</h1>

      <Forms
        salvarTarefa={salvarTarefa}
        nome={nome}
        setNome={setNome}
        categoria={categoria}
        setCategoria={setCategoria}
        dataEntrega={dataEntrega}
        setDataEntrega={setDataEntrega}
        isEditando={isEditando}
      />

      <Filter
        filter={filter}
        setFilter={setFilter}
        filterCategoria={filterCategoria}
        setFilterCategoria={setFilterCategoria}
        ordenacao={ordenacao}
        setOrdenacao={setOrdenacao}
      />

      <Tabela
        tarefas={tarefasFiltradasEOrdenadas()}
        editarTarefa={editarTarefa}
        removerTarefa={removerTarefa}
        alternarConclusao={alternarConclusao}
      />

      {modalAberto && (
        <ModalEditar
          tarefa={tarefaEditando}
          onClose={() => setModalAberto(false)}
          onSave={salvarEdicao}
        />
      )}
    </div>
  );
}

export default App;
