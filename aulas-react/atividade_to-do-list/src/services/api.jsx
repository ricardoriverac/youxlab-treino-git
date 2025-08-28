import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000",
});

export async function salvarDadosBanco(dado) {
  return await api.post("/dados", dado);
}

export async function buscarCategorias(setLista) {
  const todosDados = await api.get("/categoria");
  setLista(todosDados.data);
  return todosDados.data;
}

export async function pegarDados() {
  return await api.get("/dados");
}

export async function editarDadosApi(id, tarefa) {
  return await api.patch(`/dados/${id}`, tarefa);
}

export async function deletandoDados(id) {
  return await api.delete(`/dados/${id}`);
}

export async function pegarCategoriasFiltro() {
  const resposta = await api.get("/categoriaFiltro");
  return resposta.data;
}
