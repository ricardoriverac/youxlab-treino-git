package aplicacao;

public class Projeto {
    public static void main(String[] args) {
        String[] exercicio = new String[]{"Maria","Bob","Alex"};

        for(int contador=0;contador< exercicio.length;contador++) {
            System.out.println(exercicio[contador]);

        }
        System.out.println("----------------------");
        for (String a : exercicio){
            System.out.println(a);
        }
    }
}
