import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:3000",
});

export const buscarTarefas = () => api.get("/tarefas");
export const adicionarTarefa = (tarefa) => api.post("/tarefas", tarefa);
export const atualizarTarefa = (id, tarefa) => api.put(`/tarefas/${id}`, tarefa);
export const excluirTarefa = (id) => api.delete(`/tarefas/${id}`);
