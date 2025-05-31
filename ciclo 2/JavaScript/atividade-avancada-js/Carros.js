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

function mostrarCarrosPorMarca(marca) {
    let carrosMarca = carros.filter(carro => carro.marca === marca);
    console.log(`Categoria: ${marca}`);
    
    let maiorAno = 0;
    for (let i = 0; i < carrosMarca.length; i++) {
        let carro = carrosMarca[i];
        console.log(`Modelo: ${carro.modelo}  Ano: ${carro.ano}`);
        if (carro.ano > maiorAno) maiorAno = carro.ano;
    }
    
    console.log(`O carro mais novo é do ano de ${maiorAno}`);
    console.log('\n');
}

mostrarCarrosPorMarca('Toyota');
mostrarCarrosPorMarca('Honda');
mostrarCarrosPorMarca('Ford');
mostrarCarrosPorMarca('Chevrolet');
mostrarCarrosPorMarca('Volkswagen');
z