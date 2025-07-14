let carros = [
    { marca: "Toyota", modelo: "Corolla", ano: 2020 },
    { marca: "Honda", modelo: "Civic", ano: 2019 },
    { marca: "Ford", modelo: "Focus", ano: 2018 },
    { marca: "Chevrolet", modelo: "Onix", ano: 2021 },
    { marca: "Volkswagen", modelo: "Polo", ano: 2022 },
    { marca: "Toyota", modelo: "Yaris", ano: 2021 },
    { marca: "Honda", modelo: "Fit", ano: 2017 },
    { marca: "Chevrolet", modelo: "Cruze", ano: 2020 },
    { marca: "Ford", modelo: "Ka", ano: 2019 },
    { marca: "Volkswagen", modelo: "Virtus", ano: 2023 },
    { marca: "Hyundai", modelo: "HB20", ano: 2022 },
    { marca: "Jeep", modelo: "Renegade", ano: 2021 },
    { marca: "Toyota", modelo: "Hilux", ano: 2023 },
    { marca: "Honda", modelo: "HR-V", ano: 2020 },
    { marca: "Chevrolet", modelo: "Spin", ano: 2018 }
];

let maiorAno=0
let anoToyota=[]
console.log('Categoria: Toyota')
for(let carro of carros){
    if (carro.marca=='Toyota'){
        console.log('Modelo: '+carro.modelo+'  Ano: '+carro.ano)
        anoToyota.push(carro.ano)
    }
}
maiorAno= Math.max(...anoToyota)
console.log('O carro mais novo é do ano de '+maiorAno)
console.log('\n')

maiorAno=0
let anoHonda=[]
console.log('Categoria: Honda')
for(let carro of carros){
    if (carro.marca=='Honda'){
        console.log('Modelo: '+carro.modelo+'  Ano: '+carro.ano)
        anoHonda.push(carro.ano)
    }
}
maiorAno= Math.max(...anoHonda)
console.log('O carro mais novo é do ano de '+maiorAno)
console.log('\n')

maiorAno=0
let anoFord=[]
console.log('Categoria: Ford')
for(let carro of carros){
    if (carro.marca=='Ford'){
        console.log('Modelo: '+carro.modelo+'  Ano: '+carro.ano)
        anoFord.push(carro.ano)
    }
}
maiorAno=Math.max(...anoFord)
console.log('O carro mais novo é do ano de '+maiorAno)
console.log('\n')

maiorAno=0
let anoChevrolet=[]
console.log('Categoria: Chevrolet')
for(let carro of carros){
    if (carro.marca=='Chevrolet'){
        console.log('Modelo: '+carro.modelo+'  Ano: '+carro.ano)
        anoChevrolet.push(carro.ano)
    }
}
maiorAno=Math.max(...anoChevrolet)
console.log('O carro mais novo é do ano de '+maiorAno)
console.log('\n')

maiorAno=0
let anoVolkswagen=[]
console.log('Categoria: Volkswagen')
for(let carro of carros){
    if (carro.marca=='Volkswagen'){
        console.log('Modelo: '+carro.modelo+'  Ano: '+carro.ano)
        anoVolkswagen.push(carro.ano)
    }
}
maiorAno=Math.max(...anoVolkswagen)
console.log('O carro mais novo é do ano de '+maiorAno)
console.log('\n')