package Seção18.PipeLIne;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ExemploPipeline {
    public static void main(String[] args) {
        List<String> nomes = Arrays.asList("Ana", "João", "Pedro", "Amanda", "Carlos");

        List<String> resultado = nomes.stream() // 1. Fonte de dados
                .filter(n -> n.startsWith("A"))     // 2. Intermediária
                .map(String::toUpperCase)           // 2. Intermediária
                .sorted()                           // 2. Intermediária
                .collect(Collectors.toList());      // 3. Terminal

        System.out.println(resultado); // [AMANDA, ANA]
    }
}
