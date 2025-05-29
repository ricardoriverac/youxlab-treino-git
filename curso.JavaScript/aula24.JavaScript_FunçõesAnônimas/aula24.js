const f=function soma(a, b){
    return console.log(a + b)
}

f(5,8)

const ff= new Function('v1', 'v2', "return v1+v2")

console.log(ff(7, 8))