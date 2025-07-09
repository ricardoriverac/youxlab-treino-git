function Evento({numero}){

    function meuEvento(){
        console.log(`Ois, fui clicdao ${numero}`)
    }
        
    return (
        <>
        <p> CLique para desparar um evento</p>
        <button onClick={meuEvento}>Ativar </button>
        </>
    )

}

export default Evento 