import Item from "./Item"

function List(){
    return(
        <>
            <h1>Minha Lista</h1>
            <ul>
                <Item marca="Porche" anoLancamento={1985}/>
                <Item marca="Ferrari" anoLancamento={1964}/>
                <Item marca="BMW"/>
                <Item marca="Fiat" anoLancamento={1952}/>
                <Item/>
            </ul>
        </>
    )
}

export default List