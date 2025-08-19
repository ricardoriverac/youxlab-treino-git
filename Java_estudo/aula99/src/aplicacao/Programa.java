package aplicacao;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Programa {
    public static void main(String[] args) {
        List<String> listaNome = new ArrayList<String>();

        listaNome.add("Maria");
        listaNome.add("Alex");
        listaNome.add("Bob");
        listaNome.add("Anna");
        listaNome.add(2,"Marco");
        System.out.println(listaNome.size());

        for (String x : listaNome){
            System.out.println(x);
        }
        System.out.println("---------------------------------");
        listaNome.removeIf(x ->x.charAt(0) == 'M');
        for (String x: listaNome){
            System.out.println(x);
        }
        System.out.println("--------------------------------------");
        System.out.println("Index og Bob: "+ listaNome.indexOf("Bob"));
        System.out.println("----------------------------------------");

        List<String> listaNova = listaNome.stream().filter(x ->x.charAt(0) == 'A').collect(Collectors.toList());
        for (String x: listaNova){
            System.out.println(x);
        }
        System.out.println("----------------------------------");
        String nome = listaNome.stream().filter(x ->x.charAt(0) == 'A').findFirst().orElse(null);
        System.out.println(nome);
    }
}
