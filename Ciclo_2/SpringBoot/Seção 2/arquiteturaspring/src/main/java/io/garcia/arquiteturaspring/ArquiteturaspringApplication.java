package io.garcia.arquiteturaspring;

import org.springframework.boot.Banner;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.core.env.ConfigurableEnvironment;

@SpringBootApplication
@EnableConfigurationProperties
public class ArquiteturaspringApplication {

	public static void main(String[] args) {
		SpringApplicationBuilder builder =
				new SpringApplicationBuilder(ArquiteturaspringApplication.class); // <-- aqui
		builder.bannerMode(Banner.Mode.OFF);
		builder.profiles("producao");
//        builder.lazyInitialization(true);

		ConfigurableApplicationContext applicationContext = builder.run(args);

		ConfigurableEnvironment environment = applicationContext.getEnvironment();
		String applicationName = environment.getProperty("spring.application.name");
		System.out.println("Nome da application: " + applicationName);

        ExemploValue value = applicationContext.getBean(ExemploValue.class);
        value.imprimirVariavel();

        AppPropertis propertis = applicationContext.getBean(AppPropertis.class);
        System.out.println(propertis.getValor1());

	}
}
