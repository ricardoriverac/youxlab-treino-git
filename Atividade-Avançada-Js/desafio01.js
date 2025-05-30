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
]

let junior = []
let pleno = []
let senior = []
let especialista = []


for (pessoa of funcionarios) {
   if (pessoa.salario < 2500 )
    junior.push(pessoa)
   if ( pessoa.salario >= 2501 && pessoa.salario <= 4000) 
    pleno.push(pessoa)
   if (pessoa.salario >= 4001 && pessoa.salario <= 6000)
    senior.push(pessoa)
   if (pessoa.salario >= 6000)
    especialista.push(pessoa)
}

console.log(junior)
console.log(pleno)
console.log(senior)
console.log(especialista)




















