import styles from "./NewProject.module.css";
import ProjectForm from "../project/ProjectForm";

function NewProject() {
  return (
    <div className={styles.newproject_container}>
      <h1>Criar Projeto</h1>
      <p>Crie seu projeto para depois adicionar os serviços</p>
      <ProjectForm />
      <form>
        <div>
          <input type="text" placeholder="Insira o nome do projeto" />
        </div>
        <div>
          <input type="number" placeholder="Insira o orçamento total" />
        </div>
        <div>
          <select name="category_id">
            <option disabled selected>
              Selecione a categoria
            </option>
          </select>
        </div>
        <div>
          <input type="submit" value="Criar projeto" />
        </div>
      </form>
    </div>
  );
}

export default NewProject;
