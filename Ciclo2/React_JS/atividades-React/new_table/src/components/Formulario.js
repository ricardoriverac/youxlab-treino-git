import { useEffect, useState } from "react";

import styles from "./Formulario.module.css";

import { SalvarDados, MostrarPessoas, Editar } from "../service/api";
import Input from "./Input";
import Tabela from "./Tabela";

function Formulario() {
  const [dados, setDados] = useState([]);

  const [name, setName] = useState();
  const [cpf, setCpf] = useState();
  const [dataNascimento, setDataNascimento] = useState();
  const [id, setId] = useState(null);
  const [editando, setEditando] = useState(false);

  useEffect(() => {
    buscarPessoas();
  }, []);

  async function buscarPessoas() {
    try {
      const pessoas = await MostrarPessoas();
      setDados(pessoas.data);
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  async function salvar() {
    if (!name || !cpf || !dataNascimento) {
      alert("Preencha todos os campos!");
      return;
    } else {
      let person = {
        name: name,
        cpf: cpf,
        dataNascimento: dataNascimento,
      };

      try {
        if (!editando) {
          await SalvarDados(person);
        } else {
          await Editar(person, id);
          setId(null)
          setEditando(false)
        }
      } catch (err) {
        alert("Ocorreu um erro!");
        console.log("err :>> ", err);
      }
    }

    setName("");
    setCpf("");
    setDataNascimento("");

    buscarPessoas();
  }

  function editar(pessoa) {
    setEditando(true);

    setName(pessoa.name);
    setCpf(pessoa.cpf);
    setDataNascimento(pessoa.dataNascimento);
    setId(pessoa.id);
    console.log(pessoa);
  }

  return (
    <div>
      <form className={styles.form}>
        <Input
          text="Nome" // label
          type="text"
          name="nome"
          placeholder="Digite o nome"
          value={name}
          handleOnChange={(evento) => setName(evento.target.value)}
        />
        <Input
          text="CPF" // label
          type="number"
          name="cpf"
          placeholder="Digite o CPF"
          value={cpf}
          handleOnChange={(evento) => setCpf(evento.target.value)}
        />
        <Input
          text="Data de nascimento" // label
          type="date"
          name="data de nascimento"
          placeholder="Digite a data de nascimetno"
          value={dataNascimento}
          handleOnChange={(evento) => setDataNascimento(evento.target.value)}
        />
        <submit className={styles.btnSalvar} onClick={salvar}>
          Salvar
        </submit>
      </form>

      <Tabela
        setDados={setDados}
        dados={dados}
        buscarPessoas={buscarPessoas}
        editar={editar}
      />
    </div>
  );
}

export default Formulario;
