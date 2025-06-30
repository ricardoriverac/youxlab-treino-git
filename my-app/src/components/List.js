import Item from './Item'

function List(){
    return(
        <>
            <h1>Minha Lista</h1>
            <ul>
                <Item marca = "Ferrari" info = "A Ferrari é uma fabricante italiana de carros esportivos de luxo, com sede em Maranello."/>
                <Item marca = "Fiat" info = "A Fiat é uma fabricante italiana de automóveis, atualmente parte da Stellantis."/>
                <Item marca = "Renault" info = "A Renault é uma fabricante francesa de automóveis fundada em 1899, com uma forte presença no Brasil e no mundo."/>
            </ul>
        </>
    )
}

export default List
