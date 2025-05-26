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
]

let eletronicos = []
console.log('PRODUTOS')

for (p of produtos){
    console.log(p.nome + '; CATEGORIA: ' + p.categoria)
    if (p.categoria == 'Eletrônicos'){
        eletronicos.push(p)
    }
}
console.log('=======================================')
console.log('ELETRÔNICOS (' + eletronicos.length + ')')
for (produto of eletronicos){
    console.log(produto.nome + '(' + produto.categoria + ')')
}
console.log('=======================================')

let perifericos = []
for (p of produtos){
    if (p.categoria == 'Periféricos'){
        perifericos.push(p)
    }
}

console.log('PERIFÉRICOS (' + perifericos.length + ')')
for (produto of perifericos){
        console.log(produto.nome + '(' + produto.categoria + ')')}

console.log('=======================================')
let acessorios = []
for (p of produtos){
    if (p.categoria == 'Acessórios'){
        acessorios.push(p)
    }
}
console.log('ACESSÓRIOS(' + acessorios.length + ')')
for (produto of acessorios){
    console.log(produto.nome + '(' + produto.categoria + ')')
}
console.log('=======================================')
let armazenamento = []
for (p of produtos){
    if (p.categoria == 'Armazenamento'){
        armazenamento.push(p)
    }
}
console.log('ARMAZENAMENTO (' + armazenamento.length + ')')
for (produto of armazenamento){
    console.log(produto.nome + '(' + produto.categoria + ')')
}

console.log('=======================================')
let moveis = []
for (p of produtos){
    if(p.categoria == 'Móveis'){
        moveis.push(p)
    }
}
console.log('MÓVEIS (' + moveis.length + ')')
for (produto of moveis){
    console.log(produto.nome + '(' + produto.categoria + ')')
}

console.log('=======================================')
let rede = []
for (p of produtos){
    if(p.categoria == 'Rede'){
        rede.push(p)
    }
}
console.log('REDE (' + rede.length + ')')
for (produto of rede){
    console.log(produto.nome + '(' + produto.categoria + ')')
}

console.log('=======================================')
let iluminacao = []
for (p of produtos){
    if(p.categoria == 'Iluminação'){
        iluminacao.push(p)
    }
}
console.log('ILUMINAÇÃO (' + iluminacao.length + ')')
for (produto of iluminacao){
    console.log(produto.nome + '(' + produto.categoria + ')')
}

console.log('=======================================')
let utilidades = []
for (p of produtos){
    if(p.categoria == 'Utilidades'){
        utilidades.push(p)
    }
}
console.log('UTILIDADES (' + utilidades.length + ')')
for (produto of utilidades){
    console.log(produto.nome + '(' + produto.categoria + ')')
}

console.log('=======================================')
let energia = []
for (p of produtos){
    if(p.categoria == 'Energia'){
        energia.push(p)
    }
}
console.log('ENERGIA (' + energia.length + ')')
for (produto of energia){
    console.log(produto.nome + '(' + produto.categoria + ')')
}
