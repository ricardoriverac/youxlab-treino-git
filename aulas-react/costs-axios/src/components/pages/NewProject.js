import styles from "./NewProject.module.css";
import { useNavigate } from "react-router-dom";
import ProjectForm from "../project/ProjectForm";
import { adicionarProjetos } from "../service/serviceProjetos";

function NewProject() {
  const navigate = useNavigate();

  async function createPost(project) {
    // initialize cost and services
    project.cost = 0;
    project.services = [];

    try {
      await adicionarProjetos(project);
      const state = { message: "Projeto criado com sucesso!" };
      navigate("/projects", { state });
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  return (
    <div className={styles.newproject_container}>
      <h1>Criar Projeto</h1>
      <p>Crie seu projeto para depois adicionar os serviços</p>
      <ProjectForm handleSubmit={createPost} btnText="Criar Projeto" />
    </div>
  );
}

export default NewProject;
