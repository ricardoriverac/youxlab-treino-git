const palavrasForca = [
  { palavra: "CACHORRO", dica: "Mamífero domesticado com faro aguçado." },
  { palavra: "PRAIA", dica: "Faixa de terra entre o continente e o oceano." },
  { palavra: "PIPOCA", dica: "Explode com calor e é feita de milho." },
  { palavra: "ESCOLA", dica: "Instituição voltada ao processo educativo." },
  { palavra: "FUTEBOL", dica: "Modalidade esportiva com dois times e uma bola." },
  { palavra: "BICICLETA", dica: "Veículo de propulsão humana sobre duas rodas." },
  { palavra: "SORVETE", dica: "Preparação congelada, geralmente doce." },
  { palavra: "LIVRO", dica: "Objeto que registra conhecimento em páginas." },
  { palavra: "GUARDA-CHUVA", dica: "Instrumento portátil de proteção contra precipitação." },
  { palavra: "JANELA", dica: "Abertura arquitetônica com função de ventilação ou visão." },
  { palavra: "RELOGIO", dica: "Dispositivo usado para medir o tempo." },
  { palavra: "TRAVESSEIRO", dica: "Objeto macio utilizado no apoio da cabeça ao dormir." },
  { palavra: "ABOBORA", dica: "Fruto comestível de cor alaranjada e casca grossa." },
  { palavra: "MONTANHA", dica: "Elevação natural do relevo, superior a uma colina." },
  { palavra: "VIOLAO", dica: "Instrumento de cordas tocado com os dedos ou palheta." },
  { palavra: "CAFÉ", dica: "Bebida estimulante obtida de sementes torradas." },
  { palavra: "LANTERNA", dica: "Fonte portátil de luz artificial." },
  { palavra: "COMPUTADOR", dica: "Máquina capaz de executar operações lógicas e matemáticas." },
  { palavra: "CELULAR", dica: "Dispositivo multifuncional com comunicação sem fio." },
  { palavra: "BIBLIOTECA", dica: "Espaço dedicado à organização e consulta de acervos literários." },
  { palavra: "CAMINHAO", dica: "Veículo automotor projetado para transportar cargas." },
  { palavra: "FOGUETE", dica: "Veículo propulsionado para navegação espacial." },
  { palavra: "DINOSSAURO", dica: "Grupo extinto de répteis de grande porte." },
  { palavra: "ELEFANTE", dica: "Maior animal terrestre atual, com presas de marfim." },
  { palavra: "GIRAFA", dica: "Mamífero herbívoro de pescoço extremamente longo." },
  { palavra: "MACACO", dica: "Primata ágil, com hábitos arbóreos." },
  { palavra: "PANTANAL", dica: "Maior planície alagável do mundo." },
  { palavra: "SEREIA", dica: "Ser mitológico ligado à água, com canto hipnótico." },
  { palavra: "FADA", dica: "Entidade mágica frequentemente associada a encantamentos." },
  { palavra: "BRUXA", dica: "Figura folclórica ligada à feitiçaria e mitos antigos." },
  { palavra: "CASTELO", dica: "Construção fortificada usada por nobres na Idade Média." },
  { palavra: "LABIRINTO", dica: "Estrutura complexa com múltiplos caminhos e desvios." },
  { palavra: "CHOCOLATE", dica: "Derivado do cacau usado em confeitaria." },
  { palavra: "PIZZA", dica: "Prato de origem italiana, frequentemente circular." },
  { palavra: "LASANHA", dica: "Prato composto por camadas intercaladas de massa e recheio." },
  { palavra: "CAVALO", dica: "Animal de montaria domesticado há milênios." },
  { palavra: "AVIÃO", dica: "Meio de transporte aéreo com asas fixas." },
  { palavra: "NAVIO", dica: "Embarcação de grande porte usada em navegação marítima." },
  { palavra: "TREM", dica: "Veículo que percorre trilhos em série de vagões." },
  { palavra: "ESPADA", dica: "Arma branca de lâmina longa e afiada." },
  { palavra: "ZUMBI", dica: "Ser reanimado, geralmente presente em narrativas de terror." },
  { palavra: "ROBÔ", dica: "Mecanismo programável com autonomia parcial ou total." },
  { palavra: "DESERTO", dica: "Região árida com baixa pluviosidade." },
  { palavra: "VULCAO", dica: "Estrutura geológica que expele magma." },
  { palavra: "NEVE", dica: "Precipitação sólida formada por cristais de gelo." },
  { palavra: "CHUVA", dica: "Precipitação líquida proveniente de nuvens." },
  { palavra: "ARCO-IRIS", dica: "Fenômeno óptico atmosférico multicolorido." },
  { palavra: "CÉU", dica: "Abóbada aparente acima da Terra." },
  { palavra: "ESTRELA", dica: "Corpo celeste que emite luz própria." },
  { palavra: "LUA", dica: "Satélite natural da Terra visível à noite." },
  { palavra: "SOL", dica: "Astro-rei que fornece energia ao planeta." },
  { palavra: "PLANETA", dica: "Corpo celeste que orbita uma estrela." },
  { palavra: "pneumoultramicroscopicossilicovulcanoconiose", dica: "Doença gerada por restos expelidos por formaçoes rochosas narturais" }
];


let palavraSecreta = "";
let dicaAtual = "";
let letrasCorretas = [];
let letrasErradas = [];
const maxErros = 6;

const elPalavra = document.getElementById("palavra");
const elErradas = document.getElementById("letrasErradas");
const elMensagem = document.getElementById("mensagem");
const partesBoneco = document.querySelectorAll(".parte");
const teclado = document.getElementById("teclado");

function gerarTeclado() {
  const alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-ã";
  teclado.innerHTML = "";

  for (let letra of alfabeto) {
    const botao = document.createElement("button");
    botao.textContent = letra;
    botao.onclick = () => verificarLetra(letra, botao);
    teclado.appendChild(botao);
  }
}

//seleciona de forma aleatoria uma palavra e uma dica dentro da const palavrasForca 
function escolherPalavra() {
  const sorteada = palavrasForca[Math.floor(Math.random() * palavrasForca.length)];
  palavraSecreta = sorteada.palavra.toUpperCase();
  dicaAtual = sorteada.dica;

  letrasCorretas = [];
  letrasErradas = [];
  atualizarTela();
  esconderBoneco();
  gerarTeclado();
  elMensagem.textContent = "";
  document.getElementById("dica").textContent = dicaAtual;
}

function atualizarTela() {
  const exibida = palavraSecreta
    .split("")
    .map(letra => letrasCorretas.includes(letra) ? letra : "_")
    .join(" ");
  elPalavra.textContent = exibida;
  elErradas.textContent = letrasErradas.join(" ");
}

function verificarLetra(letra, botao) {
  botao.disabled = true;

  if (palavraSecreta.includes(letra)) {
    letrasCorretas.push(letra);
  } else {
    letrasErradas.push(letra);
    mostrarParteBoneco(letrasErradas.length);
  }

  atualizarTela();
  verificarFim();
}

function mostrarParteBoneco(erro) {
  const ids = ["cabeca", "corpo", "bracoE", "bracoD", "pernaE", "pernaD"];
  if (erro <= ids.length) {
    document.getElementById(ids[erro - 1]).style.display = "none";
  }
}

function esconderBoneco() {
  partesBoneco.forEach(parte => parte.style.display = "block");
}

function verificarFim() {
  const venceu = palavraSecreta.split("").every(letra => letrasCorretas.includes(letra));
  if (venceu) {
    elMensagem.textContent = "voce ganhou";
    desativarTeclado();
  } else if (letrasErradas.length >= maxErros) {
    elMensagem.textContent = `voce perdeu, a palavra era: ${palavraSecreta}`;
    desativarTeclado();
  }
}

function desativarTeclado() {
  teclado.querySelectorAll("button").forEach(botao => botao.disabled = true);
}

function reiniciar() {
  escolherPalavra();
}

escolherPalavra();