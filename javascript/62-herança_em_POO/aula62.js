class Carro{ // Classe PAI
    constructor(nome, portas){
        this.nome = nome
        this.portas = portas
        this.ligado = false
        this.vel = 0
        this.cor = undefined
    }
    ligar = function(){
        this.ligado = true
    }
    deligar = function(){
        this.ligado = false
    }
}

// class Militar extends{ // A classe militar vai herdar a classe Carro

// } 

const c1 = new Carro("Normal", 4)

console.log(c1.nome)