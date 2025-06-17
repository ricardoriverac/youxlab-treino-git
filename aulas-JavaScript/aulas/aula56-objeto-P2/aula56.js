class Carro{
    constructor(parametroNome, parametroTipo){
        this.nome = parametroNome

        if(parametroTipo == 1){
            this.tipo = 'Esportivo'
            this.velocidadeMax = 300

        }else if(parametroTipo == 2){
            this.tipo = 'Utilitário'
            this.velocidadeMax = 100

        }else if(parametroTipo == 3){
            this.tipo = 'Passeio'
            this.velocidadeMax = 160

        }else{
            this.tipo = 'Militar'
            this.velocidadeMax = 180
        }
    }

    getNome(){
        return this.nome
    }
    getTipo(){
        return this.tipo
    }
    getVelocidadeMax(){
        return this.velocidadeMax
    }
    getInfo(){
        return [this.nome, this.tipo, this.velocidadeMax]
    }

    info(){
        console.log(`Nome: ${this.nome}`)
        console.log(`Tipo: ${this.tipo}`)
        console.log(`V.Max: ${this.velocidadeMax}`)
        console.log('--------------------')
    }
}

let carro1 = new Carro('Rapidão', 1)
let carro2 = new Carro('Super Luxo', 2)
let carro3 = new Carro('Bombadão', 4)
let carro4 = new Carro('Carrego tudo', 3)

// carro1.info()
// carro2.info()
// carro3.info()
// carro4.info()

console.log(carro1.getNome())