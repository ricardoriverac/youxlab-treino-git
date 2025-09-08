import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:3000/",
});

export async function listarCArtegorias() {
  return await api.get("/cartegoria");
}

export async function AdicionarTipo(item) {
  return await api.post("/cartegoria", item);
}

export async function Apagar(id) {
  return await api.delete(`/cartegoria/${id}`);
}

export async function Editar(id, item) {
  return await api.patch(`/cartegoria/${id}`, item);
}
