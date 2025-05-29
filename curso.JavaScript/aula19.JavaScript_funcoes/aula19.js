let n = 0
let max = 1000

while(n<max){
    console.log("Número" + n)
    n++
    if (n>10){
        break
    }
}
console.log("Fim do loop")
 let pares = 0
for(i=n; i<=max; i++){
    if (i%2!=0){
        continue
    }
    pares ++
}
console.log("São " + pares + " números pares")