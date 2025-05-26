const produtos = [ 
    { nome: "Notebook", categoria: "Eletrônicos", preco: 3500, estoque: 5 }, 
    { nome: "Mouse", categoria: "Periféricos", preco: 80, estoque: 25 }, 
    { nome: "Teclado Mecânico", categoria: "Periféricos", preco: 250, estoque: 12 }, 
    { nome: "Smartphone", categoria: "Eletrônicos", preco: 2200, estoque: 8 }, 
    { nome: "Monitor", categoria: "Eletrônicos", preco: 900, estoque: 10 }, 
    { nome: "Pen Drive 32GB", categoria: "Acessórios", preco: 45, estoque: 50 }, 
    { nome: "HD Externo", categoria: "Armazenamento", preco: 400, estoque: 7 }, 
    { nome: "Webcam", categoria: "Periféricos", preco: 320, estoque: 15 }, 
    { nome: "Impressora", categoria: "Periféricos", preco: 850, estoque: 4 },
    { nome: "Cadeira Gamer", categoria: "Móveis", preco: 1500, estoque: 3 }, 
    { nome: "Roteador", categoria: "Rede", preco: 300, estoque: 9 }, 
    { nome: "Headset", categoria: "Acessórios", preco: 200, estoque: 20 }, 
    { nome: "Tablet", categoria: "Eletrônicos", preco: 1800, estoque: 6 }, 
    { nome: "Carregador Portátil", categoria: "Acessórios", preco: 120, estoque: 30 }, 
    { nome: "Cabo HDMI", categoria: "Acessórios", preco: 60, estoque: 40 }, 
    { nome: "Switch de Rede", categoria: "Rede", preco: 250, estoque: 11 }, 
    { nome: "Luminária LED", categoria: "Iluminação", preco: 100, estoque: 18 }, 
    { nome: "Extensão Elétrica", categoria: "Utilidades", preco: 70, estoque: 35 }, 
    { nome: "Notebook Gamer", categoria: "Eletrônicos", preco: 7500, estoque: 2 }, 
    { nome: "Estabilizador", categoria: "Energia", preco: 350, estoque: 5 } 
];

const barato = []
const intermediario = []
const caro = []

produtos.forEach(produto => {
    if(produto.preco <= 100){
        barato.push(produto)
    }else if(produto.preco <= 1000){
        intermediario.push(produto)
    }else{
        caro.push(produto)
    }
})

// barato
console.log('Produtos baratos:')
barato.forEach(produto => {
    console.log(produto.nome + ' - ' + produto.categoria + ' - Preço: R$' + produto.preco)
})
console.log('Tem ' + barato.length + ' produtos disponíveis')
console.log()

// intermediario
console.log('Produtos intermediários:')
intermediario.forEach(produto => {
    console.log(produto.nome + ' - ' + produto.categoria + ' - Preço: R$' + produto.preco)
})
console.log('Tem ' + intermediario.length + ' produtos disponíveis')
console.log()

// caro
console.log('Produtos caros:')
caro.forEach(produto => {
    console.log(produto.nome + ' - ' + produto.categoria + ' - Preço: R$' + produto.preco)
})
console.log('Tem ' + caro.length + ' produtos disponíveis')