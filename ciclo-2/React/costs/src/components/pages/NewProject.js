import ProjectForm from '../project/ProjectForms'
import styles from './NewProject.module.css'

function NewProject () {
    return (
    <div className={styles.newproject_container}>
        <h1>Novo projeto</h1>
        <p> Crie seu projeto para depois adicionar serviços</p>
        <ProjectForm btnText = "Criar Projeto" />
    </div>
    )
}

export default NewProject