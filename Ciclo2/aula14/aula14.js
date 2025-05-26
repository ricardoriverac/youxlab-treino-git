// COMANDO SWITCH CASE--> avalia uma expressão

let colocacao=5 // EXPRESSÃO

switch(colocacao){ // Avalia a variável colocacao

    case 1:  // se caso valor de colocacao for 1
        console.log('1° Lugar')
        break  // a cada FINAL de bloco é NECESSÁRIO USAR BREAK

    case 2:
        console.log('2° Lugar')
        break

    case 3:
        console.log('3° Lugar')

    case 4: case 5: case 6: // se caso valor de colocacao for 4, 5 ou 6
        console.log('Premio de participação')
        break
        
    default: // caso não seja o caso de NENHUM dos blocos a cima
        console.log('Não subiu ao pódio')
        break
}


