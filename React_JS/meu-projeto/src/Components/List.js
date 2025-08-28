import Item from "./Item"

function List(){
    return(
        <>
            <h1>Minha Lista</h1>
            <ul>
                <Item marca="Porche"/>
                <Item marca="Ferrari"/>
                <Item marca="BMW"/>
                
            </ul>
        </>
    )
}

export default List