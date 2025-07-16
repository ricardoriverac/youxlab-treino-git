// Lista de produtos (objetos):
const produtos = [
    {nome: 'Computador', id: 1},
    {nome: 'Mouse', id: 2},
    {nome: 'Headset', id: 3}
]

function RenderizandoListas(){
    const listaDeProdutos = produtos.map(produto =>        //Percorre a lista e transforma cada item em um elemento JSX
        <li key={produto.id}>                              {/*	Key --> Identificador único que o React usa pra organizar a lista */}
            {produto.nome}
        </li>
    )
    
    return(
        <ul>{listaDeProdutos}</ul>                        // Mostra a lista na tela
    )
}

export default RenderizandoListas