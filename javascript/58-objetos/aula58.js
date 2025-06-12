class pessoa{
    constructor(pnome, ptipo){ // Constructor é um método que é automaticamente chamado quando instancia um novo objeto dessa classe
        this.nome = pnome
        if(ptipo==1){
            this.ptipo = "Esportivo"
            this.valmax = 300
        }else if(ptipo == 2){
            this.tipo = "Utilitário"
            this.valmax = 100
        }else if(ptipo == 3){
            this.tipo = "Passeio"
            this.valmax = 160
        }else{
            this.tipo = "Militar"
            this.valmax = 180
        }
    }
}

let c1 = new Carro("Nagi") // O new executa o método constructor
let c2 = new Carro("Isagi")
let c3 = new Carro("Bachira")

console.log(c1.nome)
console.log(c2.nome)
console.log(c3.nome)
