import React, { useState } from 'react';

function Formulario() {
  const [nome, setNome] = useState('');
  const [cpf, setCpf] = useState('');
  const [data, setData] = useState('');
  const [dados, setDados] = useState([]);

  const adicionar = () => {
    if (nome.trim() && cpf.trim() && data.trim()) {
      setDados([...dados, { nome, cpf, data }]);
      setNome('');
      setCpf('');
      setData('');
    }
  };
   
  const remover = (index) => {
    const novosDados = [...dados]
    novosDados.splice(index,1)
    setDados(novosDados)
  }
  
  






  return (
    <div>
      <input
        type="text"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
        placeholder="Seu nome"
      />
      <input
        type="text"
        value={cpf}
        onChange={(e) => setCpf(e.target.value)}
        placeholder="Seu CPF"
      />
      <input
        type="text"
        value={data}
        onChange={(e) => setData(e.target.value)}
        placeholder="Sua data de nascimento"
      />
      <button onClick={adicionar}>Adicionar</button>

      <table>
        <thead>
          <tr>
            <th>Nome</th>
            <th>CPF</th>
            <th>Data de Nascimento</th>
          </tr>
        </thead>
        <tbody>
          {dados.map((item, index) => (
            <tr key={index}>
              <td>{item.nome}</td>
              <td>{item.cpf}</td>
              <td>{item.data}</td>
              <td>
                <button onClick={() => remover(index)}>Remover</button>

              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Formulario;