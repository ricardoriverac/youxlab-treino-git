import ProjectForm from '../project/ProjectForms'
import styles from './NewProject.module.css'
import {useNavigate}  from 'react-router-dom'

function NewProject () {

    const navigate= useNavigate()

function createPost(project){
    //intialize cost and services

    project.cost = 0
    project.services = []

    fetch("")
}



    return (
    <div className={styles.newproject_container}>
        <h1>Novo projeto</h1>
        <p> Crie seu projeto para depois adicionar serviços</p>
        <ProjectForm btnText = "Criar Projeto" />
    </div>
    )
}

export default NewProject