import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:3000/",
});

export async function buscarTodos() {
  return await api.get("/dados");
}

export async function salvarDado(pessoa) {
  return await api.post("/dados", pessoa);
}

export async function atualizarDado(id, pessoa) {
  return await api.patch(`/dados/${id}`, pessoa);
}

export async function deletarDado(id) {
  return await api.delete(`/dados/${id}`);
}
