package io.github.nicolasgabrielfernandesmm.arquiteturaspring.todos;

import io.github.nicolasgabrielfernandesmm.arquiteturaspring.todos.TodoEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/todos")
public class TodoController {

    private final TodoService service;

    // Injeção via construtor
    public TodoController(TodoService service) {
        this.service = service;
    }

    // Cria um novo Todo
    @PostMapping
    public TodoEntity salvar(@RequestBody TodoEntity todo) {
        return service.salvar(todo);
    }

    // Atualiza o status (concluído) de um Todo existente
    @PutMapping("{id}")
    public TodoEntity atualizarStatus(@PathVariable("id") Integer id,
                                      @RequestBody TodoEntity todo) {
        return this.service.atualizarStatus(id, todo.getConcluido());
    }


}
