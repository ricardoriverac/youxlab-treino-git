class livro{
    canal = 'CFB Cursos'
    constructor(pnome, ptipo){
        if(ptipo == 1){
            this.tipo = 'Romance'
            this.casal = 'Olive & Adam'
        }else if(ptipo == 2){
            this.tipo = 'Fantasia'
            this.casal = 'Feyre & Rhysand'
        }else{
            this.tipo = 'Distopia'
            this.casal = 'Aaron & Juliette'
        }
        this.nome = pnome
    }
    info(){
        console.log(`Nome do livro: ${this.nome}`)
        console.log(`Tipo: ${this.tipo}`)
        console.log(`Casal principal: ${this.casal}`)
        console.log('--------------------------------')
    }
} 

let l1 =  new livro('Hipotese do amor', 1)
let l2 = new livro('Corte de espinhos e rosas', 2)
let l3 = new livro('Estilhaça-me', 3)

l1.info()
l2.info()
l3.info()