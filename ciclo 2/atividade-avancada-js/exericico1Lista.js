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

const faixas = { Junior: [], Pleno: [],Senior: [], Especialista: []
};

for (const funcionario of funcionarios) {
  const salario = funcionario.salario;

  if (salario <= 2500) {
    faixas.Junior.push(funcionario);
  } else if (salario <= 4000) {
    faixas.Pleno.push(funcionario);
  } else if (salario <= 6000) {
    faixas.Senior.push(funcionario);
  } else {
    faixas.Especialista.push(funcionario);
  }
}

console.log("Funcionários Juniores:");

console.log("Funcionários Plenos:");

console.log("Funcionários Seniores:");

console.log("Funcionários Especialistas:");
