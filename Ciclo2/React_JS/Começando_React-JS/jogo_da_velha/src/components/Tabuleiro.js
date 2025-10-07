import Quadrado from "./Quadrado";
import './Tabuleiro.css'

function Tabuleiro({quadrados, onClick}){
    return(
        <div className="tabuleiro">
            {quadrados.map((valor, index) => (
                <Quadrado key={index} valor={valor} onClick={()=>onClick(index)}/>
            ))}
        </div>
    )
}

export default Tabuleiro