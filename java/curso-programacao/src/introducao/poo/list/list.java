package introducao.poo.list;

import java.util.ArrayList;
import java.util.List;

public class list {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();

        // Adicionando elementos a lista
        list.add("Maria");
        list.add("João");
        list.add("Pedro");
        list.add("Júlio");
        for (String x : list){
            System.out.println(x);
        }
        // Removendo elementos da lista
        System.out.println("------------");
        // Removendo pelo indices da lista
        list.remove(2);
        list.remove("João");
        for (String x : list){
            System.out.println(x);
        }
        // Saber o tamanho da lista
        System.out.println("-----------");
        System.out.println("Tamanho da lista " + list.size());
        // Predicados de uma lista
        System.out.println("--------------");
        list.add("Marvel");
        list.add("Marco");
        // Removi todos aqueles que tem a letra 'M'
        list.removeIf(y -> y.charAt(0) == 'M');
        for (String x : list){
            System.out.println(x);
        }
        // Pegando os indices dos elementos da lista
        System.out.println("-----------");
        // Se não existir esse elemento dará como -1
        System.out.println("Index de bob " + list.indexOf("João"));
        System.out.println("Index de Julio " + list.indexOf("Júlio"));
        System.out.println("------------");
        // Filtrando a lista
        list.add("Jaco");
        list.add("Jose");
        list.add("Julia");
        list.add("Maria");
        // Filtrei aquele que tem o primeiro caractere "M" maiusculo
        List<String> result = list.stream().filter(y -> y.charAt(0) == 'M').toList();
        for (String x : result){
            System.out.println(x);
        }
        System.out.println("-------------");
        // Filtrei a primeira pessoa que começa com a letra J , se não tiver será nulo
        String nome = list.stream().filter(z ->  z.charAt(0) == 'J').findFirst().orElse(null);
        System.out.println(nome);
    }
}
