package io.garcia.arquiteturaspring.todos;

import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

@Component
public class TodoService {

    private TodoRepository repository;
    private TodoValidator validator;
    private Email



    public TodoService(TodoRepository repository) {
        this.repository = repository;
    }

    public TodoEntity salvar(TodoEntity novoTodo){
        return repository.save(novoTodo);
    }

    public void atualizarStatus(TodoEntity todo){
        repository.save(todo);
    }

    public TodoEntity buscarPorId(Integer id){
        return repository.findById(id).orElse(null);
    }
}
