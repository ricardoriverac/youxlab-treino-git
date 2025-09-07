package io.garcia.arquiteturaspring.todos;

import org.springframework.stereotype.Service;

@Service
public class TodoService {

    private TodoRepository repository;
    private TodoValidator validator;
    private MailSender mailSender;


    public TodoService(TodoRepository repository, TodoValidator validator, MailSender mailSender) {
        this.repository = repository;
        this.validator = validator;
        this.mailSender = mailSender;
    }

    public TodoService(TodoRepository repository) {
        this.repository = repository;
    }

    public TodoEntity salvar(TodoEntity novoTodo){
        return repository.save(novoTodo);
    }

    public void atualizarStatus(TodoEntity todo){
        repository.save(todo);
        String status = todo.getConcluido() == Boolean.TRUE ? "Concluido" : "Não Concluido";
        mailSender.enviar("Todo " + todo.getDescricao() + "foi atualizado para " + status );
    }

    public TodoEntity buscarPorId(Integer id){
        return repository.findById(id).orElse(null);
    }
}
