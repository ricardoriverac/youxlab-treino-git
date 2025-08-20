import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000",
});

export async function salvarNovosDados(dado) {
  return await api.post("/dados", dado);
}

export async function buscarTodosDados() {
  return await api.get("/dados");
}

export async function editarDadosApi(pessoa, id) {
  return await api.patch(`/dados/${id}`, pessoa);
}

export async function deletandoDados(id) {
  return await api.delete(`/dados/${id}`);
}
