package execucao;

import java.util.Map;
import java.util.TreeMap;

public class Programa {
    public static void main(String[] args) {
        Map<String, String> cookies = new TreeMap<>();

        cookies.put("usarname", "Maria");
        cookies.put("email", "maria@gmail.com");
        cookies.put("phone", "991711122");
        System.out.println(cookies.get("phone"));
        System.out.println(cookies.get("email"));

        System.out.println("Contem a chave phone?: "+ cookies.containsKey("phone"));

        System.out.println("Quantidade de elementos: "+ cookies.size());

        System.out.println("ALL COOKIES: ");
       for (String key: cookies.keySet()){
            System.out.println(key + ":" + cookies.get(key));
        }
    }
}
