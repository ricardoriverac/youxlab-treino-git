const funcionarios = [ 
  { nome: "Ana", salario: 2500, cargo: "Assistente" }, 
  { nome: "Bruno", salario: 4200, cargo: "Analista" }, 
  { nome: "Carlos", salario: 3800, cargo: "Analista" }, 
  { nome: "Diana", salario: 1800, cargo: "Estagiario" }, 
  { nome: "Edu", salario: 6000, cargo: "Gerente" }, 
  { nome: "Fernanda", salario: 7200, cargo: "Gerente" }, 
  { nome: "Guilherme", salario: 3100, cargo: "Desenvolvedor" }, 
  { nome: "Helena", salario: 2950, cargo: "Desenvolvedor" }, 
  { nome: "Igor", salario: 4600, cargo: "Analista" }, 
  { nome: "Julia", salario: 2300, cargo: "Assistente" }, 
  { nome: "Kaique", salario: 8000, cargo: "Diretor" }, 
  { nome: "Larissa", salario: 5400, cargo: "Coordenador" }, 
  { nome: "Marcos", salario: 1500, cargo: "Estagiario" }, 
  { nome: "Natalia", salario: 3800, cargo: "Desenvolvedor" }, 
  { nome: "Otavio", salario: 3900, cargo: "Desenvolvedor" }, 
  { nome: "Paula", salario: 2400, cargo: "Assistente" }, 
  { nome: "Rafael", salario: 6700, cargo: "Gerente" }, 
  { nome: "Sofia", salario: 3300, cargo: "Analista" }, 
  { nome: "Tiago", salario: 4800, cargo: "Analista" }, 
  { nome: "Vanessa", salario: 8500, cargo: "Diretora" } 
];

let juniores = [];
let plenos = [];
let seniores = [];
let especialistas = [];

for (let funcionario of funcionarios) {
  let { nome, salario, cargo } = funcionario;

  if (salario <= 2500) {
    juniores.push(`${nome}, ${cargo} - Salário: R$${salario.toFixed(2).replace('.', ',')}`);
  } else if (salario <= 4000) {
    plenos.push(`${nome}, ${cargo} - Salário: R$${salario.toFixed(2).replace('.', ',')}`);
  } else if (salario <= 6000) {
    seniores.push(`${nome}, ${cargo} - Salário: R$${salario.toFixed(2).replace('.', ',')}`);
  } else {
    especialistas.push(`${nome}, ${cargo} - Salário: R$${salario.toFixed(2).replace('.', ',')}`);
  }
}

console.log("Funcionários juniores:");
console.log(juniores.join('\n'));
console.log("\nFuncionários plenos:");
console.log(plenos.join('\n'));
console.log("\nFuncionários seniores:");
console.log(seniores.join('\n'));
console.log("\nFuncionários especialistas:");
console.log(especialistas.join('\n'));
