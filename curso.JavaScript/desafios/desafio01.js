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
]

let junior = []
let pleno = []
let senior = []
let especialista = []

for (n of funcionarios){
    if (n.salario <= 2500){
        junior.push(n)
    }else if(n.salario >= 2501 && n.salario <= 4000 ){
        pleno.push(n)
    }else if (n.salario >= 4001 && n.salario <= 6000){
        senior.push(n)
    }else if(n.salario > 6000){
        especialista.push(n)
    }
}

console.log("Funcionário juniores: ")
for(pessoa of junior){
    console.log(pessoa.nome + ', ' + pessoa.cargo + ' - R$' + pessoa.salario)
}
console.log('------------------------------------------------')
console.log("Funcionário plenos: ")
for(pessoa of pleno){
    console.log(pessoa.nome + ', ' + pessoa.cargo + ' -R$' + pessoa.salario)
}
console.log('------------------------------------------------')
console.log("Funcionários sêniores: ")
for (pessoa of senior){
    console.log(pessoa.nome + ' ,' + pessoa.cargo + ' -R$' + pessoa.salario)
}
console.log('------------------------------------------------')
console.log("Funcionários especialistas: ")
for (pessoa of especialista){
    console.log(pessoa.nome + ' ,' + pessoa.cargo + ' -R$' + pessoa.salario)
}