package io.github.nicolasgabrielfernandesmm.arquiteturaspring.configuration;

import io.github.nicolasgabrielfernandesmm.arquiteturaspring.montadora.Motor;
import io.github.nicolasgabrielfernandesmm.arquiteturaspring.montadora.TipoMotor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

@Configuration
public class MontadoraConfiguration {

    @Bean(name = "motorEletrico")
    public Motor motorEletrico() {
        var motor = new Motor();
        motor.setCavalos(220);
        motor.setCilindros(4);
        motor.setModelo("TH-40");
        motor.setLitragem(2.0);
        motor.setTipo(TipoMotor.ELETRICO);
        return motor;
    }

    @Bean(name = "motorAspirado")
    @Primary
    public Motor motorAspirado() {
        var motor = new Motor();
        motor.setCavalos(110);
        motor.setCilindros(3);
        motor.setModelo("MX-70");
        motor.setLitragem(1.5);
        motor.setTipo(TipoMotor.ASPIRADO);
        return motor;
    }

    @Bean(name = "motorTurbo")
    public Motor motorTurbo() {
        var motor = new Motor();
        motor.setCavalos(330);
        motor.setCilindros(6);
        motor.setModelo("HK-10");
        motor.setLitragem(3.5);
        motor.setTipo(TipoMotor.TURBO);
        return motor;
    }

}