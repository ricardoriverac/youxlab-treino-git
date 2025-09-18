import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000",
});

export async function adicionarProjetos(project) {
  return await api.post("/projects", project);
}

export async function pegarProjetos() {
  return await api.get("/projects");
}

export async function deletarProjeto(id) {
  return await api.delete(`/projects/${id}`);
}

export async function pegarDadosProjeto(id) {
  return await api.get(`/projects/${id}`);
}

export async function editarProjeto(id, dado) {
  const response = await api.patch(`/projects/${id}`, dado);
  return response.data;
}
