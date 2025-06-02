
//const filtroMaior18=(valor,indice,array)=>{
    const filtroMaior18=(valor)=>{
        if(valor >= 18)
            return valor
        
    }
const idades=[15,21,30,48,17,18,22]
const maior=idades.filter((val,ind,arr)=>{
     if(val >= 18)
            return val
})

const menor=idades.filter((val,ind,arr)=>{
     if(val < 18)
            return val
})
//const maior=idades.filter(filtroMaior18)//pode ter uma funçao que opera o filter separado
console.log(idades)
console.log(maior)
console.log(menor)