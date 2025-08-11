import { useState } from "react";

import style from "./formulario.module.css";
import FormularioInputs from "../componeteInputs/formularioInputs";
import TabelaDados from "../ComponenteTabela/tabela";

function Formulario() {
  const [nome, setNome] = useState("");
  const [cpf, setCpf] = useState("");
  const [data, setData] = useState("");
  const [dados, setDados] = useState([]);

  const adicionar = () => {
    if (nome.trim() && cpf.trim() && data.trim()) {
      setDados([...dados, { nome, cpf, data }]);
      setNome("");
      setCpf("");
      setData("");
    }
  };

  const remover = (index) => {
    const novosDados = [...dados];
    novosDados.splice(index, 1);
    setDados(novosDados);
  };

  const editar = (index) => {
    const item = dados[index];
    setNome(item.nome);
    setCpf(item.cpf);
    setData(item.data);
    remover(index);
  };

  return (
    <div>
      <h2 className={style.h2}>Cadastro</h2>
      <FormularioInputs
        nome={nome}
        cpf={cpf}
        data={data}
        setNome={setNome}
        setCpf={setCpf}
        setData={setData}
        adicionar={adicionar}
      />
      <TabelaDados dados={dados} remover={remover} editar={editar} />
    </div>
  );
}

export default Formulario;
