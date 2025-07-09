import Item from "./Item";

function List() {
  return (
    <>
      <h1>Minha lista</h1>
      <ul>
        <Item marca="Ferrari" ano_lancamento={1985} />
        <Item marca="Fiat"ano_lancamento={1950} />
        <Item marca="Fusca Azul" ano_lancamento={1945}/>
        <Item marca="Chevrolet" ano_lancamento="1999"/>
      </ul>
    </>
  );
}

export default List;
