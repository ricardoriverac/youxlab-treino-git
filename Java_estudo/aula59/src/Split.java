public class Split {
    public static void main(String[] args) {
        String s = "azul amarelo roxo preto";

        String[] vect = s.split(" ");

        System.out.println(vect[0]);
        System.out.println(vect[1]);
        System.out.println(vect[2]);
        System.out.println(vect[3]);

    }
}
