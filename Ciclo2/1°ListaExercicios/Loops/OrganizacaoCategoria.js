let produtos = [
    { nome: "Camiseta", categoria: "Vestuário", preco: 50, estoque: 30 },
    { nome: "Tênis", categoria: "Calçados", preco: 120, estoque: 15 },
    { nome: "Calça Jeans", categoria: "Vestuário", preco: 90, estoque: 20 },
    { nome: "Relógio", categoria: "Acessórios", preco: 200, estoque: 8 },
    { nome: "Boné", categoria: "Acessórios", preco: 40, estoque: 50 },
    { nome: "Celular", categoria: "Eletrônicos", preco: 1500, estoque: 5 },
    { nome: "Fone de Ouvido", categoria: "Eletrônicos", preco: 80, estoque: 25 },
    { nome: "Mochila", categoria: "Acessórios", preco: 100, estoque: 12 },
    { nome: "Sandália", categoria: "Calçados", preco: 70, estoque: 18 },
    { nome: "Tablet", categoria: "Eletrônicos", preco: 900, estoque: 7 }
];

let quantidadeAcessorios=0
console.log('Categoria: Acessórios')
for(let produto of produtos){
    if (produto.categoria=='Acessórios'){
        console.log(produto.nome)
        quantidadeAcessorios+=produto.estoque
    }
}
console.log('Quantidade de Acessórios: '+quantidadeAcessorios)
console.log('\n')

let quantidadeVestuario=0
console.log('Categoria: Vestuário')
for(let produto of produtos){
    if (produto.categoria=='Vestuário'){
        console.log(produto.nome)
        quantidadeVestuario+=produto.estoque
    }
}
console.log('Quantidade de Vestuário: '+quantidadeVestuario)
console.log('\n')

let quantidadeCalcados=0
console.log('Categoria: Calçados')
for(let produto of produtos){
    if (produto.categoria=='Calçados'){
        console.log(produto.nome)
        quantidadeCalcados+=produto.estoque
    }
}
console.log('Quantidade de Calçados: '+quantidadeCalcados)
console.log('\n')

let quantidadeEletronico=0
console.log('Categoria: Eletrônicos')
for(let produto of produtos){
    if (produto.categoria=='Eletrônicos'){
        console.log(produto.nome)
        quantidadeEletronico+=produto.estoque
    }
}
console.log('Quantidade de Eletrônicos: '+quantidadeEletronico)
console.log('\n')