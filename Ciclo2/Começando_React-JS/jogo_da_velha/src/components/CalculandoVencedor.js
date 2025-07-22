function CalculaVencedor(quadrados) {
  const combinacoesVencedoras = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8], // linhas
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8], // colunas
    [0, 4, 8],
    [2, 4, 6], // diagonais
  ];
  for(let [a,b,c] of combinacoesVencedoras){
    if(quadrados[a] && quadrados[a]===quadrados[b] && quadrados[a]===quadrados[c]){
        return quadrados[a]
    }
  }
  return null
}
 export default CalculaVencedor