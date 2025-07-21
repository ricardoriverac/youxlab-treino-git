//package ProblemaExemplo.aplication;
//
//import java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.entities.AlturaEnt;
//
//import java.util.Locale;
//import java.util.Scanner;
//
//public class AlturaApp {
//    public static void main(String[] args) {
//        Locale.setDefault(Locale.US);
//        Scanner input = new Scanner(System.in);
//
//        double somaAltura = 0;
//        double count16anos = 0;
//
//        System.out.print("How many people will be included? ");
//        int amount = input.nextInt();
//
//        AlturaEnt[] vect = new AlturaEnt[amount];
//
//        for (int i = 0; i < amount; i ++ ){
//            System.out.println("Date of " + (i + 1) + "ª people: ");
//
//           // COLETA O NOME
//           System.out.print("Name?: ");
//           input.nextLine();
//           String name = input.nextLine();
//
//
//            // COLETA A IDADE
//            System.out.print("Age?: ");
//            int age = input.nextInt();
//
//            // SE A IDADE FOR MENOR QUE 16 ELE CONTA + 1
//            if (age < 16){
//                count16anos += 1;
//            }
//
//            // COLETA A ALTURA
//            System.out.print("Height?: ");
//            double heigth = input.nextDouble();
//
//            // CALCULA A MEDIA DE ALTURA
//            somaAltura += heigth;
//
//            vect[i] = new AlturaEnt(name, age, heigth);
//
//        }
//
//        double mediaAltura = somaAltura / amount;
//        double porcentagem16anos = count16anos / amount;
//
//
//        System.out.printf("Heigth media: %.2f", mediaAltura);
//        System.out.println();
//        System.out.println("Percentage under 16 years of age: " + (porcentagem16anos * 100) + "%");
//        for (int i = 0; i < amount; i++){
//            if (vect[i].getAge() < 16){
//                System.out.println(vect[i].getName());
//            }
//        }
//    }
//}
