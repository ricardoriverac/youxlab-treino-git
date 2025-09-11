import savings from '../../img/savings.svg'


function Inicio() {


     return(
        <section>
         <h1>Bem-vindo ao <span>Costs</span></h1>
         <p>comece a gerencia os seus projetos agora mesmo!</p>
         <a href="/">Criar Projeto</a>
         <img src={savings} alt="costs" />
        </section>
     )
}

export default Inicio