class pessoa{
    constructor(pnome){ // Constructor é um método que é automaticamente chamado quando instancia um novo objeto dessa classe
        this.nome = pnome
    }
}

let p1 = new pessoa("Nagi") // O new executa o método constructor
let p2 = new pessoa("Isagi")
let p3 = new pessoa("Bachira")

console.log(p1.nome)
console.log(p2.nome)
console.log(p3.nome)
