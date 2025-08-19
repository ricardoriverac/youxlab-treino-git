let posicao = 5;
switch (posicao) { // switch é uma estrutura condicional usada para avaliar uma expressão e executar diferentes blocos de código dependendo do valor dessa expressão

    case 1:  // Se posicao for igual a 1
        console.log('1° Lugar')
        break  // Encerra o bloco do case

    case 2: // Se posicao for igual a 2
        console.log('2° Lugar') 
        break

    case 3: // Se posicao for igual a 3
        console.log('3° Lugar')
        break 

    // Se posicao for 4, 5 ou 6:
    case 4: case 5: case 6: 
        console.log('Premio de participação')
        break 

    default: // Se não for nenhum dos casos acima, cai aqui
        console.log('Não subiu ao pódio')
        break  // Encerra o bloco do default
}