package Programa;

import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;

public class Programa {
    public class Program {
        public static void main(String[] args) {
            Set<String> set = new LinkedHashSet<>();

            set.add("Tv");
            set.add("Notebook");
            set.add("Tablet");

            set.removeIf(x -> x.length() >= 3);

            System.out.println(set.contains("Notebook"));

            for (String p : set) {
                System.out.println(p);
            }
        }
    }
}
