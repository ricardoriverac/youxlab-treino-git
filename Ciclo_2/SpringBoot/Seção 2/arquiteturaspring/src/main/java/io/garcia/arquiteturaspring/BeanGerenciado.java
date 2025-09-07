package io.garcia.arquiteturaspring;

import io.garcia.arquiteturaspring.todos.TodoValidator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

@Component
@Scope(BeanDefinition.SCOPE_SINGLETON)
public class BeanGerenciado {

    @Autowired
    private TodoValidator validator;

    @Autowired
    public BeanGerenciado(TodoValidator validator) {
        this.validator = validator;
    }

}
