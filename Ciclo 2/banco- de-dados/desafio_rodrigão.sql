select
	nmc.nome as 
		nome_do_usuario,
			dnu.nome
from aluno
left outer join
	turma on aluno.id_turma=turma.id
left outer join
	rel_disciplina_turma as dsc on dsc.id_turma = turma.id
left outer join
	disciplina as dnu on dsc.id_disciplina = dnu.id 
left outer join
	professor as prof on dnu.id_professor = prof.id
left outer join
	usuario as nmc on prof.id_usuario = nmc.id
where
	aluno.id = 10