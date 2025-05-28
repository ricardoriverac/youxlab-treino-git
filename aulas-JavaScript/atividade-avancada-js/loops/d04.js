const carros = [
    { marca: "Honda", modelo: "Fit", ano: 2020 },
    { marca: "Ford", modelo: "Fusion", ano: 2018 },
    { marca: "Chevrolet", modelo: "Onix", ano: 2021 },
    { marca: "Fiat", modelo: "Mobi", ano: 2021 },
    { marca: "Toyota", modelo: "Hilux", ano: 2022 },
    { marca: "Fiat", modelo: "Toro", ano: 2022 },
    { marca: "Toyota", modelo: "Corolla", ano: 2020 },
    { marca: "Honda", modelo: "HR-V", ano: 2022 },
    { marca: "Ford", modelo: "Ranger", ano: 2021 },
    { marca: "Toyota", modelo: "Yaris", ano: 2021 },
    { marca: "Chevrolet", modelo: "Cruze", ano: 2019 },
    { marca: "Ford", modelo: "EcoSport", ano: 2020 },
    { marca: "Honda", modelo: "City", ano: 2021 },
    { marca: "Ford", modelo: "Ka", ano: 2017 },
    { marca: "Fiat", modelo: "Argo", ano: 2020 },
    { marca: "Toyota", modelo: "Etios", ano: 2019 },
    { marca: "Honda", modelo: "Civic", ano: 2018 },
    { marca: "Chevrolet", modelo: "Tracker", ano: 2023 }
];

let marcas = []

for (let carro of carros){
    if(!(marcas.includes(carro.marca))){
        marcas.push(carro.marca)
    }
}

for (let modelos of marcas){
    console.log('Marca: ' + modelos)

    let anos = []
    let nomeCarros = []
    for (let nome of carros){
        if(nome.marca == modelos){
            console.log('   •' + nome.modelo + ' (' + nome.ano + ')')
            anos.push(nome.ano)
            nomeCarros.push(nome.modelo)
        }
    }

    const anoMaisNovo = Math.max(...anos)
    const anoMaisVelho = Math.min(...anos)

    console.log('O carro mais novo ' + nomeCarros[0])
    console.log('O carro mais antigo ' + nomeCarros[1])

    console.log()
}