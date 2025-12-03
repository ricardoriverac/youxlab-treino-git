import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000",
});

export async function pegarImagem(nome) {
  return await api.get(
    `https://pixabay.com/api/?key=53454556-d33ffa45c161a8df7423360eb&q=${nome}`
  );
}

export async function salvarDados(dados) {
  return await api.post("/dados", dados);
}

export async function pegarDados() {
  return await api.get("/dados");
}

export async function apagarLinha(id) {
  return await api.delete(`/dados/${id}`);
}
