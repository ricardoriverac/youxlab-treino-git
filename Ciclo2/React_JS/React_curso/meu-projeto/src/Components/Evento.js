import Button from "./eventComponents/Button";

function Evento({}){

    function meuEvento(){
        console.log(`Ativando o primeiro evento!`);
    }

    function segundoEvento(){
        console.log('Ativando o segundo evento!');
    }

    return(
        <div>
            <p>Clique para disparar um evento:</p>

            {/* pode reaproveitar componentes!! basta mudar os dados  */}
            <Button evento={meuEvento} text="Primeiro Evento" />    
            <Button evento={segundoEvento} text="Segundo Evento" />  

        </div>
    )
}

export default Evento