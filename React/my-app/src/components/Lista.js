import Item from "./Itens"




function List(){
    return(
        <>
            <h1>Minha lista</h1>
            <ul>
                <Item marca="Fiat" ano_lancamento={1920}/>
                <Item marca="Suziki" ano_lancamento={1980}/>
                <Item/>
            </ul>
        </>
    )
}
export default List