import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5001",
});

export async function SalvarDados(pessoa) {
  return await api.post("/people", pessoa);
}

export async function MostrarPessoas() {
  return await api.get("/people");
}

export async function Deletar(id) {
  return await api.delete(`/people/${id}`);
}

export async function Editar(pessoa, id) {
    return await api.patch(`/people/${id}`, pessoa)
}