package io.github.nicolasgabrielfernandesmm.arquiteturaspring.service;

import org.springframework.stereotype.Service;

@Service
public class EscolaService {

    public String pegarAlunos(){
        String nomeAluno = "joao";
        String nota = "0";

        if(nomeAluno.equals("joao")){
            nota = "6";
        }

        return nomeAluno + nota;
    }

}
