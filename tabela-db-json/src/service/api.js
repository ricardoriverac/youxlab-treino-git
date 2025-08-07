import axios from "axios";

const url = "http://localhost:3000/usuarios";

export async function getResp() {
  let response = await axios
    .get(url)
    .then((response) => {
      console.log(response.data);
    })
    .catch((e) => {
      console.log(e);
    })
    .finally((f) => {
      console.log("finalizou a request");
    });
}

export async function getUser(nome) {
  console.log(nome);
  try {
    const response = await axios.get(
      `http://localhost:3000/usuarios?nome=${nome}`
    );
    console.log(response.data);
  } catch (error) {
    console.log(error);
  }
}

export async function getUsers() {
  try{
    const response = await axios.get('http://localhost:3000/usuarios')
    return response.data
  }catch(err) {
    console.log(err)
  }
}

export async function cadastrarUser( nome, idade, estadoCivil, cpf, data, setData) {
  await axios
    .post(url, { nome: nome, idade: idade, estadoCivil: estadoCivil, cpf: cpf })
    .then((resp) => {
      // console.log(resp.data)
      setData([...data, resp.data]);
    })
    .catch((e) => {
      console.log(e);
    });
}

export async function editarUser( id, newUser  ) {
  await axios
    .patch(`http://localhost:3000/usuarios/${id}`, {
      nome: newUser.nome,
      idade: newUser.idade,
      estadoCivil: newUser.estadoCivil,
      cpf: newUser.cpf
    })
    .then((resp) => {
      console.log(resp.data);
    })
    .catch((e) => {
      console.log(`erro: ${e}`);
    });
}

export async function deleteUser( id ) {
  await axios.delete(`http://localhost:3000/usuarios/${id}`)
}

// async function pegarDados() {
//   const resultado = await fetch("http://localhost:3000/usuarios").then((res) =>
//     res.json()
//   );
//   console.log(resultado);
// }

// pegarDados();

// async function testeSimples() {
//   return "Dá um like aí";
// }

// testeSimples().then((resposta) => {
//     console.log(resposta)
// })
