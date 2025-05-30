const carros = [
    { marca: "Honda", modelo: "Civic 2023" },
    { marca: "Honda", modelo: "Fit 2014" },
    { marca: "Honda", modelo: "Accord 2005" }, 

    { marca: "Ford", modelo: "Bronco 2023" },
    { marca: "Ford", modelo: "EcoSport 2015" },
    { marca: "Ford", modelo: "Escort 1998" },

    { marca: "Volkswagen", modelo: "Nivus 2023" },
    { marca: "Volkswagen", modelo: "Fox 2013" },
    { marca: "Volkswagen", modelo: "Fusca 1980" },

    { marca: "Nissan", modelo: "Kicks 2023" },
    { marca: "Nissan", modelo: "Sentra 2012" },
    { marca: "Nissan", modelo: "Maxima 2000" }
];


let Honda = []
let Ford = []
let Volkswagem = []
let Nissan = []
let HondaAntigo = carros[0]
let FordAntigo = carros[0]
let VolkswagemAntigo = [0]
let NissanAntigo = carros[0]
let HondaNovo = carros[0]
let FordNovo = carros[0]
let VolkswagemNovo = carros[0]
let NissanNovo = carros[0]


for (carro in carros){
    if (carro.marca == "Honda" )
        Honda.push(carro)   
    }
    if (carro.marca == "Ford"){
        Ford.push(carro)
    }    
    if (carro.marca == "Volkswagem"){
        Hyundai.push(carro)
    }
    if (carro.marca == "Nissan"){
        Nissan.push(carro)
    }

console.log("Honda")
for(carro of Honda){
console.log("marca:", carro.marca, "modelo:", carro.modelo ,"modelo", carro.modelo)
   if (carro.ano , HondaAntigo.ano){
    HondaAntigo = carro
    }
    if (carro.ano > HondaNovo.ano){
        HondaNovo = carro
    }

}
console.log("Modelo mais antigo Honda:", HondaAntigo)
console.log("Modelo mais novo Honda:", HondaNovo)

console.log("Ford")
for(carro of Ford){
console.log("marca:", carro.marca, "modelo:", carro.modelo ,"modelo", carro.modelo)
   if (carro.ano , FordAntigo.ano){
    FordAntigo = carro
    }
    if (carro.ano > FordNovo.ano){
        FordNovo = carro
    }

}
console.log("Modelo mais antigo Ford:", FordAntigo)
console.log("Modelo mais novo Ford:", FordNovo)

console.log("Volkswagem")
for(carro of Volkswagem){
console.log("marca:", carro.marca, "modelo:", carro.modelo ,"modelo", carro.modelo)
   if (carro.ano , VolkswagenAntigo.ano){
    VolkswagemAntigo = carro
    }
    if (carro.ano > VolkswagemNovo.ano){
        VolkswagenNovo = carro
    }

}
console.log("Modelo mais antigo Volskswagem:", VolkswagemAntigo)
console.log("Modelo mais novo Volkswagem:", VolkswagemNovo)

console.log("Nissan")
for(carro of Nissan){
console.log("marca:", carro.marca, "modelo:", carro.modelo ,"modelo", carro.modelo)
   if (carro.ano , NissanAntigo.ano){
    NissanAntigo = carro
    }
    if (carro.ano > NissanNovo.ano){
        NissanNovo = carro
    }

}
console.log("Modelo mais antigo Nissan:", NissanAntigo)
console.log("Modelo mais novo Nissan:", NissanNovo)