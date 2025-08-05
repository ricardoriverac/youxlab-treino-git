package com.garcia.exercicioJander;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class ExercicioJanderApplication {

	@GetMapping("/hello-word")
	public String helloword(){
		return "Hello word!";
	}

	public static void main(String[] args) {
		SpringApplication.run(ExercicioJanderApplication.class, args);
	}


}
