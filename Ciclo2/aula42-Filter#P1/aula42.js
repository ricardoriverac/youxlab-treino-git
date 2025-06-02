//MÉTODO filter--> permite fazer uma filtragem nos elementos de um array

const idades=[15, 21, 30, 17, 18, 44, 12, 50]

//filtrando somente as idades maior ou igual a 18 anos

//MANEIRA DIRETA
const maior=idades.filter((valor)=>{
    if(valor>=18){
        return valor
    }
})

const menor=idades.filter((valor)=>{
    if(valor<18){
        return valor
    }
})


//MANEIRA INDIRETA
// // const filterMaior=(valor,indice,array)=>{
//     const filterMaior=(valor)=>{
//         if (valor>=18)
//             return valor
//     }
// const maior=idades.filter(filterMaior)

console.log(idades)
console.log(maior)
console.log(menor)