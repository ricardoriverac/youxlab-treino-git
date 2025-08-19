package problema;

import entidade.Produto2;

import java.util.*;

public class execucao {
    public static void main(String[] args) {
        List<Produto2> list = new ArrayList<>();

        list.add(new Produto2("TV", 900.0));
        list.add(new Produto2("Notebook", 1200.0));
        list.add(new Produto2("Tablet", 400.0));

        // 🔹 Usando função lambda (forma moderna)
        Comparator<Produto2> comparador = (p1, p2) -> {
            return p1.getName().toUpperCase().compareTo(p2.getName().toUpperCase());
        };

        // 🔸 Usando classe anônima (forma antiga)
//        Comparator<Produto2> comparador = new Comparator<Produto2>() {
//            @Override
//            public int compare(Produto2 p1, Produto2 p2) {
//                return p1.getName().toUpperCase().compareTo(p2.getName().toUpperCase());
//            }
//        };

        // 🔹 Usando classe separada (forma clássica)
//        list.sort(new MyComparator());

        // 🔹 Usando método estático com referência (::)
        list.sort(comparador);

        // Imprimindo os produtos ordenados
        for (Produto2 p : list) {
            System.out.println(p.getName() + ", " + p.getPrice());
        }
    }
}