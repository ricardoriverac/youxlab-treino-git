package io.github.nicolasgabrielfernandesmm.arquiteturaspring.todos;

import io.github.nicolasgabrielfernandesmm.arquiteturaspring.todos.TodoEntity;
import io.github.nicolasgabrielfernandesmm.arquiteturaspring.todos.TodoRepository;
import org.springframework.stereotype.Service;

@Service
public class TodoService {

    private final TodoRepository repository;

    public TodoService(TodoRepository repository) {
        this.repository = repository;
    }

    public TodoEntity salvar(TodoEntity todo){
        return repository.save(todo);
    }

    public TodoEntity atualizarStatus(Integer id, Boolean concluido) {
        TodoEntity todoExistente = repository.findById(id)
                .orElseThrow(() -> new RuntimeException("Todo não encontrado"));
        todoExistente.setConcluido(concluido);
        return repository.save(todoExistente);
    }
}
