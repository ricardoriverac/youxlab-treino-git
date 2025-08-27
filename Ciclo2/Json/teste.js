const objetos = [
  {
    nome: "Sophia",
    idade: 16,
    esta_estuda: true,
    detalhes_estudo: {
      estudando: "Json",
      curso: "Hora de Codar",
    },
    hobies: ["treinar", "correr", "cantar"],
  },
  {
    nome: "Sarah",
    idade: 19,
    esta_estuda: false,
    detalhes_estudo: {
      estudando: null,
      curso: null,
    },
    hobies: ["Academia", "nadar"],
  },
];

console.log(objetos);

//JSON
//converter objeto para json: 

const jsonDados= JSON.stringify(objetos)

console.log(jsonDados);
console.log(typeof jsonDados);

//converter json para objetos:

const objetosDados = JSON.parse(jsonDados)

console.log(objetosDados);
console.log(typeof objetosDados);


// busca um dado desses elementos: 

objetosDados.map((pessoa) => {
    console.log(pessoa.nome);
})

