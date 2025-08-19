package io.garcia.arquiteturaspring;

import org.springframework.boot.Banner;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.core.env.ConfigurableEnvironment;

@SpringBootApplication
public class ArquiteturaspringApplication {

	public static void main(String[] args) {
		SpringApplicationBuilder builder =
				new SpringApplicationBuilder(ArquiteturaspringApplication.class); // <-- aqui
		builder.bannerMode(Banner.Mode.OFF);
		builder.profiles("producao, homologacao"); // melhor colocar ANTES do run()

		ConfigurableApplicationContext applicationContext = builder.run(args);

		ConfigurableEnvironment environment = applicationContext.getEnvironment();
		String applicationName = environment.getProperty("spring.application.name");
		System.out.println("Nome da application: " + applicationName);
	}
}
