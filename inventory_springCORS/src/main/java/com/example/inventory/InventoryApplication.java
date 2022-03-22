package com.example.inventory;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@SpringBootApplication
public class InventoryApplication {

	public static void main(String[] args) {

		SpringApplication.run(InventoryApplication.class, args);
	}


//	this also didnt work for cors error method #2: https://spring.io/guides/gs/rest-service-cors/
//	@Bean
//	public WebMvcConfigurer corsConfigurer() {
//		return new WebMvcConfigurer() {
//			@Override
//			public void addCorsMappings(CorsRegistry registry) {
////				greeting-javaconfig
//				registry.addMapping("/items").allowedOrigins("http://localhost:8080");
//			}
//		};
//	}

}
