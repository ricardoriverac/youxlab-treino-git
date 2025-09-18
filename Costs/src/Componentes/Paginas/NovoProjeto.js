import styles from './NovoProjeto.module.css'

import ProjetoForm from '../proeject/ProjetoForm'

function NovoProjeto() {
     return(
        <div className={styles.novoprojeto_conatiner}>
          <h1>Criar Projeto</h1>
          <p>crie seu projeto para depois adicionar os serviços</p>
          <ProjetoForm />
        </div>
     )
}

export default NovoProjeto