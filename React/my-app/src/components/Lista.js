import Item from "./Itens"




function List(){
    return(
        <>
            <h1>Minha lista</h1>
            <ul>
                <Item marca="Fiat"/>
                <Item marca="Suziki"/>
            </ul>
        </>
    )
}
export default List