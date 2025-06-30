import Item from './Item'

function List(){
    return(
        <>
            <h1>Minha Lista</h1>
            <ul>
                <Item marca = "Ferrari" ano_lancamento = {1947} info = "A Ferrari é uma fabricante italiana de carros esportivos de luxo, com sede em Maranello."/>
                <Item marca = "Fiat" ano_lancamento = {1998} info = "A Fiat é uma fabricante italiana de automóveis, atualmente parte da Stellantis."/>
                <Item marca = "Renault" ano_lancamento = {1976} info = "A Renault é uma fabricante francesa de automóveis fundada em 1899, com uma forte presença no Brasil e no mundo."/>
                <Item marca = "Porshe" info="A Porsche é uma fabricante alemã de automóveis de luxo e alto desempenho, com sede em Stuttgart."/>
                <Item marca="Chevrolet " ano_lancamento={1999} info="A Chevrolet é uma marca de automóveis da General Motors (GM) fundada em 1911, conhecida por sua ampla gama de veículos, desde carros subcompactos até caminhões comerciais de médio porte. "/>
                <Item />
            </ul>
        </>
    )
}


export default List
