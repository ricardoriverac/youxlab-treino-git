import Item from "./Item"

function List(){
    return(
        <div>
            <h1>Minha Lista</h1>
            <ul>
                <Item marca='Ferrari' ano_lancamento={1985}/>
                <Item marca='Fiat' ano_lancamento={1964}/>
                <Item marca='Renault'/>
                <Item marca='Chevrolet' ano_lancamento="1999"/>
                <Item/>
            </ul>
        </div>
    )
}

export default List