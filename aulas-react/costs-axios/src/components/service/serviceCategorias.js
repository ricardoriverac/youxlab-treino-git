import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000",
});

export async function pegarCategorias() {
  return await api.get("/categories");
}
