import './Quadrado.css'

function Quadrado({valor, onClick}){
    return(
        <button className="quadrado" onClick={onClick}>
            {valor}
        </button>
    )
}

export default Quadrado