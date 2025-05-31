//usando funçao anonima
const f = new Function('v1', 'v2', 'return v1 + v2') //parametrizada em modo anonimo
console.log(f(10,5))

//usando rest
const F = (...valores) => {
    let res = 0
    for (let v of valores) {
        res += v
    }
    return res
}
console.log(F(10,5))

//passando pra outros parametros
const f2 = new Function('v1', 'v2', 'v3', 'return v1 + v2 + v3') //funçao anonima
console.log(f2(10,5,15))
