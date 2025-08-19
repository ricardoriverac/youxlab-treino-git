package io.github.nicolasgabrielfernandesmm.arquiteturaspring.controller;

import io.github.nicolasgabrielfernandesmm.arquiteturaspring.service.EscolaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/escola")
public class EscolaController {

    @Autowired
    private EscolaService escolaService;

    @GetMapping("/pegarAlunos")
    public String getAlunos() {
       return escolaService.pegarAlunos();
    }
}
