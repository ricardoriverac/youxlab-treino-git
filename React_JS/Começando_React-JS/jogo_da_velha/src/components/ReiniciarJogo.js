import './ReiniciarJogo.css'

function ReiniciarJogo(){
    function reiniciar(){
        window.location.reload()
    }
    return(
        <button className="btnReiniciar" onClick={reiniciar}>Reiniciar</button>
    )
}

export default ReiniciarJogo