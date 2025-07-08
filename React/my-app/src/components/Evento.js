function Evento() {

    function meuEvt() {
        console.log("AEEEEE")
    } 

    return(
       <div>
           <p>Clique :D</p>
           <button onClick={meuEvt}>!!!!Clique Aqui!!!!</button>
       </div>
    )
}

export default Evento