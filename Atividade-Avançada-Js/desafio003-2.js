let maria = 0;
let joao = 0;
let nulo = 0;
let branco = 0;
let totalVotos = 0;

while (true) {
    let voto = prompt(
` Vote digitando o número:
1 - Maria
2 - João
3 - Nulo
4 - Branco
Digite seu voto:`);

    if (voto == "1") {
        maria++;
        totalVotos++;
    } else if (voto == "2") {
        joao++;
        totalVotos++;
    } else if (voto == "3") {
        nulo++;
        totalVotos++;
    } else if (voto == "4") {
        branco++;
        totalVotos++;
    } else {
        alert(" Opção inválida! Vote novamente.");
        continue; 
    }

    let continuar = prompt("Deseja votar novamente? (s/n)");

    if (continuar.toLowerCase() != "s") {
        break;
    }
}

function porcentagem(valor) {
    return ((valor / totalVotos) * 100).toFixed(2);
}

alert(
` Resultado da Votação:

 Maria: ${maria} voto(s) (${porcentagem(maria)}%)
 João: ${joao} voto(s) (${porcentagem(joao)}%)
 Nulo: ${nulo} voto(s) (${porcentagem(nulo)}%)
 Branco: ${branco} voto(s) (${porcentagem(branco)}%)

 Total de votos: ${totalVotos}
`
);
