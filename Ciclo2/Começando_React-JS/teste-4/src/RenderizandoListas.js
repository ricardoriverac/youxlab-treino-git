// Lista de produtos (objetos):
const produtos = [
    {nome: 'Computador', fruta: false , id: 1},
    {nome: 'Mouse', fruta: false ,id: 2},
    {nome: 'Headset', fruta: false ,id: 3},
    {nome: 'Laranja', fruta: true, id: 4 }
]

function RenderizandoListas(){
    const listaDeProdutos = produtos.map(produto =>        // map --> Percorre a lista e transforma cada item em um elemento JSX
        <li 
            key={produto.id}                               // Key --> Identificador único que o React usa pra organizar a lista 
            style={{
                color: produto.fruta ? 'magenta' : 'green'            // Adiciona um css nos protudos e se o prduto for uma fruta a cor muda
            }}
        >                              
            {produto.nome}
        </li>
    )
    
    return(
        <ul>{listaDeProdutos}</ul>                        // Mostra a lista na tela
    )
}

export default RenderizandoListas