import axios from "axios";

const api = axios.create({
  baseURL: "http://10.0.3.245:8080/pessoasX",
});

const apiProduto = axios.create({
  baseURL: "http://10.0.3.245:8080/produtosX",
});

export async function salvarNovaPessoa(pessoa) {
  return await api.post("/salvarPessoas", pessoa);
}

export async function verificarLogin(pessoa) {
  return await api.post("/login", pessoa);
}

export async function pegarProdutos() {
  return await apiProduto.get("/buscarTdsProdutos");
}

export async function salvarNovoProduro(produto) {
  return await apiProduto.post("/salvarProdutos", produto);
}
