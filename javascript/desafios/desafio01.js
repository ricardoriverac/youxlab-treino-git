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

let junior = []  
let pleno = []
let senior = []
let especialista = []
    
for (funcionario of funcionarios){
    if (funcionario.salario < 2500)   {
        junior.push(funcionario)
    }

    if  (funcionario.salario > 2500 && funcionario.salario < 4000){
        pleno.push(funcionario)
    }

    if (funcionario.salario > 4001 && funcionario.salario < 6000){
        senior.push(funcionario)
    }

    if (funcionario.salario > 6000){
        especialista.push(funcionario)
    }
}

console.log("Funcionários juniores: ")
for (pessoa of junior){
    console.log(pessoa.nome, pessoa.cargo + " - Salário: R$" + pessoa.salario )

}

console.log("\nFuncionários plenos: ")
for (pessoa of pleno){
    console.log(pessoa.nome, pessoa.cargo + " - Salário: R$" + pessoa.salario )
}

console.log("\nFuncionários seniores: ")
for (pessoa of senior){
    console.log(pessoa.nome, pessoa.cargo + " - Salário: R$" + pessoa.salario )
}

console.log("\nFuncionários especialistas: ")
for(pessoa of especialista){
    console.log(pessoa.nome, pessoa.cargo + " - Salário: R$" + pessoa.salario )
}

// console.log("Funcionários Juniores:")
// console.log(junior)
// console.log("Funcionários Plenos:")
// console.log(pleno)
// console.log("Funcionários Seniores:")
// console.log(senior)
// console.log("Funcionários Especialistas:")
// console.log(especialista)
