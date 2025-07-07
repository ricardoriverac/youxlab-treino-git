import { data, useHistory } from 'react-router-dom'

import ProjectForm from '../project/ProjectForm'

import styles from './NewProjects.module.css'

function NewProject (){

    const history = useHistory()

    function createPost(project){

        // initialize cost and services
        project.cost = 0
        project.services = []

        fetch('https:/localhost:5000/projects', {
            method: 'POST',
            headers: {
                'Content-type': "application/json",
            }
        }).then((resp => resp.json())
        .then((data) => {
            console.log(data)
        })
        ).catch(err => console.log(err))

    }

    return(
        <div className={styles.newProject_container}>
            <h1>Criar Projeto</h1>
            <p>Crie seu projeto para depois adicionar os serviços</p>
            <ProjectForm btnText="Criar Projeto"/>
        </div>
    )
}

export default NewProject
