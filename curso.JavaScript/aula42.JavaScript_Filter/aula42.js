const idades = [12, 19, 18, 23, 11, 67, 44, 21]

const FiltroMaior18 =(valor)=>{
    if (valor >= 18){
        return valor
    }
}
const maior = idades.filter(FiltroMaior18)


const FiltroMenor18 =(valor)=>{
    if (valor < 18){
        return valor
    }
}
const menor = idades.filter(FiltroMenor18)


console.log(idades)
console.log(maior)
console.log(menor)