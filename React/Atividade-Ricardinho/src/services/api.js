import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:3000/",
});

export async function listarPessoas() {
  return await api.get("/pessoas");
}

export async function salvarPessoa(item) {
  return await api.post("/pessoas",item);
}

export async function ApagarPessoas(id) {
  return await api.delete(`/pessoas/${id}`);
}

export async function EditarPessoa(id, item) {
    return await api.patch(`/pessoas/${id}`, item)
}