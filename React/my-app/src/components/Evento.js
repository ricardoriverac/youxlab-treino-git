import Button from "./Butao"


function Evento() {

    function meuEvt() {
        console.log("Ativando")
    } 

    function segundoEvt() {
       console.log("segundo")
    }

    return(
       <div>
           <p>Clique :D</p>
           <Button event={meuEvt} text="Novo Evento"/>
           <Button event={segundoEvt} text="Evento 2"/>
       </div>
    )
}

export default Evento