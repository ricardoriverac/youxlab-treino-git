package com.youxlab.cursodespring.applicacaospring;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class AplicacaoSpringApplication {

	@GetMapping("/hello-word")
	public String helloword(){
		return "Hello word!";
	}

	public static void main(String[] args) {
		SpringApplication.run(AplicacaoSpringApplication.class, args);
	}


}
