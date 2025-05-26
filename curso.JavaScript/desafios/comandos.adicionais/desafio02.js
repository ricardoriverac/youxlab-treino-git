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

let barato = []
let intermediario = []
let caro = []

for (n of produtos){
    if (n.preco <= 100){
        barato.push(n)
    }else if (n.preco >=101 && n.preco <= 1000){
        intermediario.push(n)
    }else if(n.preco >=1000){
        caro.push(n)
    }}

let quantBarato = []
let quantIntermediario = []
let quantCaro = []


console.log("BARATOS: (" + barato.length + ')')

for (material of barato){
    console.log(material.nome +  ' (R$' + material.preco + ') ESTOQUE: ' + material.estoque)
}

let soma = 0
for (e of barato){
    quantBarato.push(e.estoque)}


for (let i = 0; i < quantBarato.length; i++) {
  soma += quantBarato[i]}


console.log("A quantidade de produtos baratos é " + soma)
console.log("-------------------------------------------")
console.log("INTERMEDIÁRIOS: (" + intermediario.length + ')')

for (material of intermediario)
    console.log(material.nome + '(R$' + material.preco + ') ESTOQUE: ' +material.estoque)
let somaI = 0
for (e of intermediario){
    quantIntermediario.push(e.estoque)
}
for(let i = 0; i < quantIntermediario.length; i++){
    somaI += quantIntermediario[i]
}
console.log('A quantidade de produtos intermediários é ' + somaI)

console.log('------------------------------------------')
console.log('CAROS: (' + caro.length + ') ' )
for (material of caro){
    console.log(material.nome + '(R$' + material.preco + '); ESTOQUE: ' + material.estoque)
}

for (e of caro){
    quantCaro.push(e.estoque)
}
let somaC = 0
for (let i = 0; i < quantCaro.length; i ++){
    somaC += quantCaro[i]
}
console.log('A quantidade de materiais caros é ' + somaC)