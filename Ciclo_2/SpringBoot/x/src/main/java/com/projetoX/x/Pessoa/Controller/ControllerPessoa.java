package com.projetoX.x.Pessoa.Controller;

import com.projetoX.x.Pessoa.Model.ModelPessoa;
import com.projetoX.x.Pessoa.Service.ServicePessoa;
import com.projetoX.x.Pessoa.Controller.dto.PessoaDto;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RequiredArgsConstructor
@RestController
@RequestMapping("/pessoasX")
@CrossOrigin(origins = "*")
public class ControllerPessoa {

    private final ServicePessoa servicePessoa;

    @PostMapping("/salvar")
    public ModelPessoa salvar(@RequestBody ModelPessoa modelPessoa){
        return servicePessoa.salvar(modelPessoa);
    }

    @GetMapping("/buscar/{id}")
    public ModelPessoa buscar(@PathVariable("id") Integer id){
        return servicePessoa.buscarPorId(id);
    }

    @DeleteMapping("deletar/{id}")
    public void deletar(@PathVariable("id") Integer id){
        servicePessoa.deletarPorId(id);
    }

    @PutMapping("atualizar/{id}")
    public void atualizarPessoa(@PathVariable("id") Integer id, @RequestBody ModelPessoa pessoa){
        pessoa.setId(id);
        servicePessoa.atualizarPessoa(pessoa);
    }

    @PostMapping("/login")
    public ResponseEntity<Boolean> loginUsuario(@RequestBody PessoaDto request) {
        boolean autenticado = servicePessoa.login(request.getEmail(), request.getSenha());
        return ResponseEntity.ok(autenticado);
    }
}
