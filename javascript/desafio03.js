const carros = [
    { marca: "Toyota", modelo: "Corolla", ano: 2020 },
    { marca: "Toyota", modelo: "Hilux", ano: 2022 },
    { marca: "Toyota", modelo: "Yaris", ano: 2019 },
    { marca: "Honda", modelo: "Civic", ano: 2018 },
    { marca: "Honda", modelo: "Fit", ano: 2020 },
    { marca: "Honda", modelo: "HR-V", ano: 2021 },
    { marca: "Ford", modelo: "Focus", ano: 2017 },
    { marca: "Ford", modelo: "Fiesta", ano: 2016 },
    { marca: "Ford", modelo: "EcoSport", ano: 2020 },
    { marca: "Chevrolet", modelo: "Onix", ano: 2021 },
    { marca: "Chevrolet", modelo: "Prisma", ano: 2019 },
    { marca: "Chevrolet", modelo: "Cruze", ano: 2018 },
    { marca: "Volkswagen", modelo: "Golf", ano: 2017 },
    { marca: "Volkswagen", modelo: "Polo", ano: 2021 },
    { marca: "Volkswagen", modelo: "T-Cross", ano: 2022 }
  ];

let toyota = []
let honda = []
let ford = []
let chevrolet = []
let volkswagen = []
let carroMaisAntigoToyota = carros[0] // Definiu o primeiro carro como se fosse o mais antigo
let carroMaisAntigoHonda = carros[0]
let carroMaisAntigoFord = carros[0]
let carroMaisAntigoChevrolet = carros[0]
let carroMaisAntigoVolkswagen = carros[0]
let carroNovoToyota = carros[0] // Definiu o primeiro carro como se fosse o mais novo
let carroNovoHonda = carros[0]
let carroNovoFord = carros[0]
let carroNovoChevrolet = carros[0]
let carroNovoVolkswagen = carros[0]

for (carro of carros){ // Para cada carro em carros
    if(carro.marca == "Toyota"){ // Se a marca do carro for "Toyota"
        toyota.push(carro) // Coloca o carro na lista
    }

    if(carro.marca == "Honda"){
        honda.push(carro)
    }

    if(carro.marca == "Ford"){
        ford.push(carro)
    }

    if(carro.marca == "Chevrolet"){
        chevrolet.push(carro)
    }

    if(carro.marca == "Volkswagen"){
        volkswagen.push(carro)
    }
}

console.log("TOYOTA")
for (carro of toyota){
    console.log("Marca: ", carro.marca, ", modelo: ", carro.modelo, ", ano: ", carro.ano)
    if (carro.ano < carroMaisAntigoToyota.ano){ // Se encontrar um carro mais velho vai mudando a variável
        carroMaisAntigoToyota = carro
    }
    if(carro.ano > carroNovoToyota.ano){
        carroNovoToyota = carro
    }
}
console.log("Carro mais antigo Toyota: ", carroMaisAntigoToyota)
console.log("Carro mais novo Toyota: ", carroNovoToyota)

console.log("\nHONDA")
for (carro of honda){
    console.log("Marca: ", carro.marca, ", modelo: ", carro.modelo, ", ano: ", carro.ano)
    if(carro.ano < carroMaisAntigoHonda.ano){
        carroMaisAntigoHonda = carro
    }
    if(carro.ano > carroNovoHonda.ano){
        carroNovoHonda = carro
    }
}
console.log("Carro mais antigo Honda: ", carroMaisAntigoHonda)
console.log("Carro mais novo Honda: ", carroNovoHonda)

console.log("\nFORD")
for (carro of ford){
    console.log("Marca: ", carro.marca, ", modelo: ", carro.modelo, ", ano: ", carro.ano)
    if(carro.ano < carroMaisAntigoFord.ano){
        carroMaisAntigoFord = carro
    }
    if(carro.ano > carroNovoFord.ano){
        carroNovoFord = carro
    }
}
console.log("Carro mais antigo Ford: ", carroMaisAntigoFord)
console.log("Carro mais novo Ford: ", carroNovoFord)

console.log("\nCHEVROLET")
for (carro of chevrolet){
    console.log("Marca: ", carro.marca, ", modelo: ", carro.modelo, ", ano: ", carro.ano)
    if(carro.ano < carroMaisAntigoChevrolet.ano){
        carroMaisAntigoChevrolet = carro
    }
    if(carro.ano > carroNovoChevrolet.ano){
        carroNovoChevrolet = carro
    }
}
console.log("Carro mais antigo Chevrolet: ", carroMaisAntigoChevrolet)
console.log("Carro mais novo Chevrolet: ", carroNovoChevrolet)

console.log("\nVOLKSWAGEN")
for (carro of volkswagen){
    console.log("Marca: ", carro.marca, ", modelo: ", carro.modelo, ", ano: ", carro.ano)
    if(carro.ano < carroMaisAntigoVolkswagen.ano){
        carroMaisAntigoVolkswagen = carro
    }
    if(carro.ano > carroNovoVolkswagen.ano){
        carroNovoVolkswagen = carro
    }
}
console.log("Carro mais antigo Volkswagen: ", carroMaisAntigoVolkswagen)
console.log("Carro mais novo Volkswagen: ", carroNovoVolkswagen)
