const palavras = [
  {
    id: 1,
    palavra: "cenoura",
    dica: "vegetal",
  },
  {
    id: 2,
    palavra: "tijolo",
    dica: "material de construção",
  },
  {
    id: 3,
    palavra: "cachorro",
    dica: "animal de estimação",
  },
  {
    id: 4,
    palavra: "óculos",
    dica: "ajuda a enxergar",
  },
  {
    id: 5,
    palavra: "bola",
    dica: "usado em esportes",
  },
  {
    id: 6,
    palavra: "chuveiro",
    dica: "banho",
  },
  {
    id: 7,
    palavra: "espelho",
    dica: "reflete imagem",
  },
  {
    id: 8,
    palavra: "cadeira",
    dica: "móvel para sentar",
  },
  {
    id: 9,
    palavra: "panela",
    dica: "usado para cozinhar",
  },
  {
    id: 10,
    palavra: "guarda-chuva",
    dica: "protege da chuva",
  },
  {
    id: 11,
    palavra: "trem",
    dica: "meio de transporte sobre trilhos",
  },
  {
    id: 12,
    palavra: "sabão",
    dica: "usado na limpeza",
  },
  {
    id: 13,
    palavra: "caderno",
    dica: "usado para escrever",
  },
  {
    id: 14,
    palavra: "abacaxi",
    dica: "fruta tropical",
  },
  {
    id: 15,
    palavra: "travesseiro",
    dica: "usado para dormir",
  },
  {
    id: 16,
    palavra: "ventilador",
    dica: "gera vento",
  },
  {
    id: 17,
    palavra: "escada",
    dica: "ajuda a subir",
  },
  {
    id: 18,
    palavra: "tigre",
    dica: "animal selvagem",
  },
  {
    id: 19,
    palavra: "camisa",
    dica: "peça de roupa",
  },
  {
    id: 20,
    palavra: "geladeira",
    dica: "eletrodoméstico",
  },
  {
    id: 21,
    palavra: "jardim",
    dica: "tem flores e plantas",
  },
  {
    id: 22,
    palavra: "prancha",
    dica: "usada para surfar",
  },
  {
    id: 23,
    palavra: "dragão",
    dica: "criatura mitológica",
  },
  {
    id: 24,
    palavra: "dinheiro",
    dica: "meio de pagamento",
  },
  {
    id: 25,
    palavra: "teatro",
    dica: "local de apresentações",
  },
];

const alfabeto = [
  "A", "B", "C", "D", "E", "F", "G",
  "H", "I", "J", "K", "L", "M", "N",
  "O", "P", "Q", "R", "S", "T", "U",
  "V", "W", "X", "Y", "Z"
];
let palavra = "";
let dica = "";
let acertos =[]
let erros = []

function SortearPalavra(max) {
  const palavraSorteada = Math.floor(Math.random() * max);
  console.log(palavras[palavraSorteada(palavras.length)])
}
