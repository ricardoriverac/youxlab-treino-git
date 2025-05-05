const pessoa = {
    nome: "Maria",
    idade: 23,
    cidade: "São Paulo",
    habilidade: ["HTML", "CSS", "JavaScript"]
};

const jsonString = JSON.stringify(pessoa);
console.log(jsonString);