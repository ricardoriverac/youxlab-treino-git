package davisales07.com.github.arquitetraSpringDavi.montadora;

import davisales07.com.github.arquitetraSpringDavi.montadora.api.CarroStatus;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TesteFabricaController {

@Autowired
    private Motor motor;

@PostMapping
    public CarroStatus ligarCarro(@RequestBody Chave chave){
        var carro = new HondaHRV(motor);
        carro.darIgnicao(chave);
    }

}
