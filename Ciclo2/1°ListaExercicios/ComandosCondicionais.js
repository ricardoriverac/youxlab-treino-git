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
{ nome: "Vanessa", salario: 8500, cargo: "Diretora" }]

console.log('Funcionários Juniores:')
for( let salary2500 of funcionarios){
    if(salary2500.salario<=2500){
        console.log(salary2500.nome+','+salary2500.cargo+' - Salário:'+salary2500.salario)
    }
}
console.log('\n')

console.log('Funcionários Plenos:')
for( let salary4000 of funcionarios){
    if((salary4000.salario>=2501)&&(salary4000.salario<=4000)){
        console.log(salary4000.nome+','+salary4000.cargo+' - Salário:'+salary4000.salario)
    }
}
console.log('\n')

console.log('Funcionários Sênior:')
for( let salary6000 of funcionarios){
    if((salary6000.salario>=4001)&&(salary6000.salario<=6000)){
        console.log(salary6000.nome+','+salary6000.cargo+' - Salário:'+salary6000.salario)
    }
}
console.log('\n')

console.log('Funcionários Especialistas:')
for( let salary6001 of funcionarios){
    if(salary6001.salario>6000){
        console.log(salary6001.nome+','+salary6001.cargo+' - Salário:'+salary6001.salario)
    }
}
console.log('\n')
