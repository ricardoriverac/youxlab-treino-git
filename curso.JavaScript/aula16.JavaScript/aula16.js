const objs = document.getElementsByTagName("div")

let num = [1, 4, 7, 10, 12]

for(i= 0; i < num.length; i++){
    console.log(num[i])
}

console.log('---------------------')

for(n of num){
    console.log(n)
}

console.log('---------------------')

for(n in num){
    console.log(num[n])
}

console.log('---------------------')