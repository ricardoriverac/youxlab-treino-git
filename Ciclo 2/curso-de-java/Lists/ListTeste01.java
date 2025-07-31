package Lists;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ListTeste01 {
    public static void main(String[] args) {
        List<String> pessoas = new ArrayList();
        pessoas.add("Maria");
        pessoas.add("Felipe");
        pessoas.add("Davi");
        pessoas.add("Breno");
        pessoas.add("João");
        pessoas.add(2, "Edson");
        for(String pessoa : pessoas) {
            System.out.println(pessoa);
        }

        System.out.println("Indef of bob " + pessoas.indexOf("Bob"));
        System.out.println("Indef of marco " + pessoas.indexOf("Marco"));
        System.out.println("====================================");

        for(Object pessoa : (List)pessoas.stream().filter((nome) -> nome.charAt(0) == 'M').collect(Collectors.toList())) {
            System.out.println(pessoa);
        }

        String name = (String)pessoas.stream().filter((nome) -> nome.charAt(0) == 'A').findFirst().orElse((String) null);
        System.out.println(name);
    }
}