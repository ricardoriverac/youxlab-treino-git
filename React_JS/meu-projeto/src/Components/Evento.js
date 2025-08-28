function Evento({numero}){

    function meuEvento(){
        console.log(`Foi Ativado! ${numero}`);
    }

    return(
        <div>
            <p>Clique para disparar um evento:</p>
            <button onClick={meuEvento}>Ativar!</button>
        </div>
    )
}

export default Evento