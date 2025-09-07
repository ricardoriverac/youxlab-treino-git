package io.garcia.arquiteturaspring;

import io.garcia.arquiteturaspring.todos.MailSender;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;

public class ConfiguracaoAcessoEmail {
    @Autowired
    private AppPropertis propertis;

    @Bean
    public MailSender mailSender(){
        return null;
    }
}
