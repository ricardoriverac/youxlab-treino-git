import { useEffect } from "react"
import style from "./Formulario.module.css"


function Formulario({ salvarPessoa, pessoaEditando }) {
  const [nome, setNome] = useState("");
  const [cpf, setCPF] = useState("");
  const [nascimento, setNascimento] = useState("");

  useEffect(() => {
    if (pessoaEditando) {
      setNome(pessoaEditando.nome || "");
      setCPF(pessoaEditando.cpf || "");
      setNascimento(pessoaEditando.nascimento || "");
    }
  }, [pessoaEditando]);

  function salvarDados() {
    const pessoa = { nome, cpf, nascimento };
    salvarPessoa(pessoa);
  }

  function onEditar() {
    if (pessoaEditando) {
      const pessoa = { ...pessoaEditando, nome, cpf, nascimento };
      salvarPessoa(pessoa);
    }
  }
 
  return (
    <div>
      <p>
        <label>Nome: </label>
        <input
          value={nome}
          type="text"
          placeholder="Digite seu nome"
          onChange={(e) => setNome(e.target.value)}
        />
      </p>
      <p>
        <label>CPF: </label>
        <input
          value={cpf}
          type="text"
          placeholder="Qual é o seu CPF"
          onChange={(e) => setCPF(e.target.value)}
        />
      </p>
      <p>
        <label>Data de nascimento: </label>
        <input
          value={nascimento}
          type="date"
          placeholder="Data de nascimento"
          onChange={(e) => setNascimento(e.target.value)}
        />
      </p>
        <button onClick={salvarDados}>Salvar Dados</button>

    </div>
  );
}

export default Formulario;
