import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;

// /home/youx/workspace-git/youxlab-treino-git/java/MapExercicio/src/candidato.csv
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        Map<String , Integer> candidatoQuantidade = new LinkedHashMap<>();
        String pathname = input.nextLine();
        BufferedReader bw = new BufferedReader(new FileReader(pathname));
        String line = bw.readLine();
        while (line != null){
            String[] campos = line.split(",");
            String name = campos[0];
            int quant = Integer.parseInt(campos[1]);

            if (candidatoQuantidade.containsKey(name)) {
                int quantvotos = candidatoQuantidade.get(name);
                candidatoQuantidade.put(name , quant + quantvotos);
            }
            else {
                candidatoQuantidade.put(name , quant);
            }
            line = bw.readLine();
        }
        for (String key : candidatoQuantidade.keySet()){
            System.out.println(key + ": " + candidatoQuantidade.get(key));
        }
    }
}