import Button from "./evento/Button";

function Evento({ numero }) {
  function meuEvento() {
    console.log("Ativando primeiro evento!");
  }

  function segundoEvento() {
    console.log("Ativando o segundo evento!");
  }

  return (
    <div>
      <p>Clique para disparar um evento:</p>
      <Button event={meuEvento} text="Primeiro Evento" />
      <Button event={segundoEvento} text="Segundo Evento" id="2"/>
    </div>
  );
}

export default Evento;