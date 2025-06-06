package introducao.java.tiposprimitivos;

public class TiposPrimitivos {
    public static void main(String[] args) {
        int idade = (int) 100000000000l;
        long nomeGrande = 100000000;
        double salarioDouble = 2000;
        float salarioFloat = (float) 2500;
        byte idadeByte = 10;
        short idadeShort = 10;
        boolean verdadeiro = true;
        boolean falso = false;
        char caractere = 'F';
        String nome = "Goku";
        System.out.println("A idade é "+idade+" Anos");
        System.out.println(falso);
        System.out.println("Char "+caractere);
        System.out.println("Oi meu nome é "+nome);
        // Valor em memoria
        System.out.println("idade");
        // Concatenando Elementos
        /*
            Tipos de Formatação:

        %s Tipo para concatenar strings
        %d numeros inteiros
        %f formatar números ou colocar números doubles

         */

        System.out.printf("Nome: %s idade: %d sexo: %s %n" , nome , idadeByte , caractere);
        // Sempre no final de print formatado quebre a linha com %n
        System.out.printf("Colando o valor em 2 casas decimais %.2f" , salarioFloat);

    }
}
