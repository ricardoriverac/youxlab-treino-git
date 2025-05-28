const carros = [
  { marca: "Volkswagen", modelo: "Gol", ano: 2020 },
  { marca: "Chevrolet", modelo: "Onix", ano: 2022 },
  { marca: "Fiat", modelo: "Argo", ano: 2023 },
  { marca: "Hyundai", modelo: "HB20", ano: 2021 },
  { marca: "Renault", modelo: "Kwid", ano: 2022 },
  { marca: "Jeep", modelo: "Renegade", ano: 2021 },
  { marca: "Toyota", modelo: "Corolla Cross", ano: 2023 },
  { marca: "Hyundai", modelo: "Creta", ano: 2022 },
  { marca: "Volkswagen", modelo: "T-Cross", ano: 2022 },
  { marca: "Nissan", modelo: "Kicks", ano: 2023 },
  { marca: "Ford", modelo: "Mustang GT", ano: 2022 },
  { marca: "Chevrolet", modelo: "Camaro SS", ano: 2020 },
  { marca: "Porsche", modelo: "911 Carrera", ano: 2023 },
  { marca: "BMW", modelo: "M4", ano: 2021 },
  { marca: "Audi", modelo: "RS5", ano: 2022 },
  { marca: "Toyota", modelo: "Corolla XEi", ano: 2021 },
  { marca: "Honda", modelo: "Civic Touring", ano: 2022 },
  { marca: "Chevrolet", modelo: "Cruze LTZ", ano: 2020 },
  { marca: "Volkswagen", modelo: "Virtus", ano: 2023 },
  { marca: "Hyundai", modelo: "Elantra", ano: 2021 },
  { marca: "Fiat", modelo: "Doblò", ano: 2020 },
  { marca: "Chevrolet", modelo: "Spin", ano: 2021 },
  { marca: "Chrysler", modelo: "Pacifica", ano: 2022 },
  { marca: "Renault", modelo: "Kangoo", ano: 2020 },
  { marca: "Toyota", modelo: "Sienna", ano: 2023 },
  { marca: "Toyota", modelo: "Hilux SRX", ano: 2023 },
  { marca: "Ford", modelo: "Ranger Limited", ano: 2022 },
  { marca: "Chevrolet", modelo: "S10 High Country", ano: 2021 },
  { marca: "Fiat", modelo: "Toro Ultra", ano: 2022 },
  { marca: "Ram", modelo: "1500 Rebel", ano: 2023 }
]

let marcas = []
for (let m of carros){
    if (!marcas.includes(m.marca))
        marcas.push(m.marca)
}
for (let c of marcas) {
console.log('--------------------------------------------------')
  console.log("==" + c + "==")
  for (let carro of carros) {
    if (carro.marca == c) {
      console.log(carro.modelo + '(' + carro.ano + ')')
  }}}