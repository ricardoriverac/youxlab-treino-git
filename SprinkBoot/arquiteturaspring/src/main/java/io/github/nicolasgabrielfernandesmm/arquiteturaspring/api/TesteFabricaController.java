package io.github.nicolasgabrielfernandesmm.arquiteturaspring.api;

import io.github.nicolasgabrielfernandesmm.arquiteturaspring.CarroStatus;
import io.github.nicolasgabrielfernandesmm.arquiteturaspring.montadora.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/carros")
public class TesteFabricaController {

    @Autowired
    @Aspirado
    private Motor motor;

    @PostMapping
    public CarroStatus ligarCarro(@RequestBody Chave chave){
        var carro = new HondaHRV(motor);
        return carro.darIgnicao(chave);
    }

}
