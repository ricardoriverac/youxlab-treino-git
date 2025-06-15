public class Main {

    public static void main(String[] args) {
        String product1 = "Computador";
        String product2 = "Office desk";

        int age = 30;
        int code = 5290;
        char gender = 'F';

        double price1 = 2100.0;
        double price2 = 650.50;
        double mesure = 53.234567;

        System.out.printf("%s,which price is %.2f%n",product1,price1);
        System.out.printf("%s,which price is R$ %.2f%n",product2,price2);
        System.out.printf("Record:%d years old,code 5290 and gender:%s%n ",age,gender);

        System.out.printf("Measue with eight decimal places %.2f",mesure);


    }
}