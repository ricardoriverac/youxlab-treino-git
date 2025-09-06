import java.util.Locale;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        // int y = 32;
        // double x = 10.53784;
        // System.out.println(y);
        // System.out.println(x);
        // System.out.println("Bom Dia!");
        // System.out.println("Olá mundo!");


        // String product1 = "Computer";
        // String product2 = "Office Desk";
        // int age = 30;
        // int code = 5290;
        // char gender = 'F';
        // double price1 = 2100.0;
        // double price2 = 650.50;
        // double measure = 53.234567;

        // System.out.println("Products:");

        //  System.out.print(product1);

        //   System.out.println(", Which price is $ 2100,00");

        //    System.out.print(product2);


        //  System.out.print(age);

        //  System.out.print(" years old, code ");

        //  System.out.print(code);

        //  System.out.print(" and gender:");

        //  System.out.println( gender);

        //  System.out.print("Measue with eight decimal places: ");

        //  System.out.println(measure);

        //  System.out.print("Rouded (three decimal places): ");

        //  System.out.printf("%.3f\n", measure);

        //  System.out.print("US decimal point: ");

        //  System.out.printf("%.3f\n", measure);

        //  System.out.println(price1);

        //  System.out.println(price2);

        //  double b, B, h, area;
        //  b = 6.0;

        //  B = 8.0;

        //  h = 5.0;

        //  area = (b + B) / 2.0 * h;

        //  System.out.println(area);

        // int a, b;
        // double resultado;

        // a = 5;
        // b = 2;

        // resultado = (double) a / b;

        // System.out.println(resultado);

//        double a;
//
//        int b;
//
//        a = 5.0;
//        b = (int) a;
//
//        System.out.println(b);
//
//        Scanner sc = new Scanner(System.in);
//        String x;
//        x = sc.next();
//        System.out.println("Voce digitou: " + x);
//
//
//        sc.close();

//        Scanner sc = new Scanner(System.in);
//        int x;
//        x = sc.nextInt();
//        System.out.println("Voce digitou: " + x);
//
//
//        sc.close();

//        Locale.setDefault(Locale.US);
//        Scanner sc = new Scanner(System.in);
//        double x;
//        x = sc.nextDouble();
//        System.out.println("Voce digitou: " + x);
//        sc.close();

//        Scanner sc = new Scanner(System.in);
//        char x;
//        x = sc.next().charAt(0);
//        System.out.println("Voce digitou: " + x);
//
//
//        sc.close();

//
//
//        Scanner sc = new Scanner(System.in);
//        String x;
//        int y;
//        float z;
//
//        x = sc.next();
//        y = sc.nextInt();
//        z = sc.nextFloat();
//
//        System.out.println("Seu nome: " + x );
//        System.out.println("Seu número: " + y );
//        System.out.println("Sua idade (pode incluir meses): " + z );
//
//
//        sc.close();


//        Scanner sc = new Scanner(System.in);
//        int x;
//        String s1,s2,s3;
//        x = sc.nextInt();
//        sc.nextLine();
//        s1 = sc.nextLine();
//        s2 = sc.nextLine();
//        s3 = sc.nextLine();
//
//
//
//        System.out.println("Dados digitados:");
//        System.out.println(x);
//        System.out.println(s1);
//        System.out.println(s2);
//        System.out.println(s3);
//
//        sc.close();
//
//        double x = 3.0;
//        double y = 4.0;
//        double z = -5.0;
//        double A, B, C;
//        A = Math.sqrt(x);
//        B = Math.sqrt(y);
//        C = Math.sqrt(25.0);
//        System.out.println("Raiz quadrada de " + x + " = " + A);
//        System.out.println("Raiz quadrada de " + y + " = " + B);
//        System.out.println("Raiz quadrada de 25 = " + C);
//        A = Math.pow(x, y);
//        B = Math.pow(x, 2.0);
//        C = Math.pow(5.0, 2.0);
//        System.out.println(x + " elevado a " + y + " = " + A);
//        System.out.println(x + " elevado ao quadrado = " + B);
//        System.out.println("5 elevado ao quadrado = " + C);
//        A = Math.abs(y);
//        B = Math.abs(z);
//        System.out.println("Valor absoluto de " + y + " = " + A);
//        System.out.println("Valor absoluto de " + z + " = " + B);

        //Exercícios:

        //01:
//        Scanner sc = new Scanner(System.in);
//        int x;
//        int y;
//
//        x = sc.nextInt();
//        y = sc.nextInt();
//
//        System.out.print("Soma = ");
//        System.out.println(x+y);

        //02:
//        Locale.setDefault(Locale.US); // para usar ponto como separador decimal
//        Scanner sc = new Scanner(System.in);
//
//        double raio = sc.nextDouble();
//        double area = 3.14159 * raio * raio;
//
//        System.out.printf("A=%.4f%n", area);
//
//        sc.close();


        //03:
//        Scanner sc = new Scanner(System.in);
//        int A = sc.nextInt();
//        int B = sc.nextInt();
//        int C = sc.nextInt();
//        int D = sc.nextInt();
//
//        int diferenca = (A * B) - (C * D);
//
//        System.out.println("DIFERENCA = " + diferenca);
//
//        sc.close();

        //4:
//        Locale.setDefault(Locale.US);
//        Scanner sc = new Scanner(System.in);
//        System.out.println("fale o seu número, o seu número de horas trabalhadas e o valor recebido por horas");
//        int A = sc.nextInt();
//        int B = sc.nextInt();
//        double C = sc.nextDouble();
//        System.out.print("Number = ");
//        System.out.println(A);
//        System.out.print("SALARY = U$ ");
//        System.out.println(B * A / 4.51);

        //5:
//        Locale.setDefault(Locale.US);
//        Scanner sc = new Scanner(System.in);
//        int A = sc.nextInt();
//        int B = sc.nextInt();
//        double C = sc.nextDouble();
//        int D = sc.nextInt();
//        int E = sc.nextInt();
//        double F = sc.nextDouble();
//        double somado1 = ((A + B + C) + (D + E +F));
//        System.out.println("Valor a pagar: " + somado1);


        //6:
//        Scanner sc = new Scanner(System.in);
//        float A = sc.nextFloat();
//        float B = sc.nextFloat();
//        float C = sc.nextFloat();
//        float triangulo = ( A + C );
//        double pi = (3.14159);
//
//
//        System.out.println("Triângulo: "+triangulo);
//        System.out.println("Circulo "+C * pi);
//        System.out.println("Trapézio: "+(A + B) * C);
//        System.out.println("Quadrado: "+B);
//        System.out.println("Retângulo: "+ A + B);
        //Fim dos desafios.

        //desafio plus paim:

//        System.out.println("Digite o raio do cone: ");
//        float raio = sc.nextFloat();
//
//        System.out.println("Digite a altura do cone: ");
//        float altura = sc.nextFloat();
//
//        double geratriz = Math.sqrt(Math.pow(raio, 2) + Math.pow(altura, 2));
//
//        double volume = (1.0 / 3) * Math.PI * Math.pow(raio, 2) * altura;
//
//        System.out.println("Geratriz do cone: " + geratriz);
//        System.out.println("Volume do cone: " + volume);
        //fim do desafio.


        //expressão comparativas:
        //operadores comparativos:
        //> maior
        //< menor
        //>= maior ou igual
        //<= menor ou igual
        //== igual
        //!= diferente

//        Exemplos de expressões comparativas
//        int x = 5;
//        X > 0 Resultado: V
//        X == 3 Resultado: F
//        10 <= 30 Resultado: V
//        X != 2 Resultado: V

        //Operadores lógicos:
//        && = E
//        || = OU
//        ! = NÃO


        //Exemplos de expressões lógicas com o E (&&):
//        (suponha x igual a 5)

//        X <= 20 && X == 10 = Resultado: F

//        X > 0 && X != 3 = Resultado: V

//        X <= 20 && X == 10 && X != 3 Resultado: F


//        Exemplos de expressões lógicas com o OU (||):
//        (suponha x igual a 5)
//        X > 0 || X != 3
//        V         V
//        Resultado: V

//        X == 10 || X <= 20
//        F             V
//        Resultado: V

//        X <= 0 || X != 3 || X != 5
//        F             V       F
//        Resultado: V


//        Exemplos de expressões lógicas com o NÃO (!):

//        (suponha x igual a 5)
//        !(X == 10)
//            F
//        Resultado: V

//        !(X >= 2)
//            V
//        Resultado: F


//        Exemplos de expressões lógicas com o NÃO (!):
//        (suponha x igual a 5)

//        !(X <= 20 && X == 10)
//            V            F
//                   F
//             V
//        Resultado: V


//        Conceito:

//        Estrutura condicional:

//        É uma estrutura de controle
//        que permite definir que um
//        certo bloco de comandos
//        somente será executado
//        dependendo de uma condição


        //Sintaxe da estrutura condicional simples:

        //if ( <condição> ) {
        //<comando 1>
        //<comando 2>
        //}

        //Importante:
        //Repare na endentação!

        //REGRA:
        //V: executa o bloco de comandos
        //F: pula o bloco de comandos


        //Sintaxe da estrutura condicional Composta:
        //REGRA:
        //V: executa somente o bloco do if
        //F: executa somente o bloco do else

        //if ( <condição> ) {
        //<comando 1>
        //<comando 2>
        //}

        //else {
        //<comando 3>
        //<comando 4>
        //}

        //Encadeamento de estruturas condicionais:

        //if ( condição 1 ) {
        //comando 1
        //comando 2
        //}

        //else {
        //if ( condição 2 ) {
        //comando 3
        //comando 4
        //}
        //else {
        //comando 5
        //comando 6
        //}
//  }

        //Exercícios Estrutura Condicional (if-else):

//        01:
//        Scanner ab = new Scanner(System.in);
//        int a = ab.nextInt();
//        if (a <= -1) {
//            System.out.println("Negativo");
//        }
//        else {
//                System.out.println("Não negativo");
//            }

            //02:
//        Scanner ab = new Scanner(System.in);
//        int a = ab.nextInt();
//        if (a % 2 == 0) {
//            System.out.println("Par");
//        }
//        else {
//                System.out.println("ímpar");
//            }


            //03:
//        Scanner ab = new Scanner(System.in);
//        int a = ab.nextInt();
//        int b = ab.nextInt();
//        if (a % b == 0   || b % a == 0) {
//            System.out.println("São Múltiplos");
//        }
//        else {
//                System.out.println("Não são Múltiplos");
//            }


            //04:
//        Scanner ab = new Scanner(System.in);
//        int a = ab.nextInt();
//        int b = ab.nextInt();
//        int duracao;
//        if (a < b)
//               duracao = b - a;
//        else {
//            duracao = 24 - a + b;
//                    System.out.println("o jogo durou " + duracao +" horas.");
//        }
        //05:
//        Scanner sc = new Scanner(System.in);
//        int codigo = sc.nextInt();
//        int quantidade = sc.nextInt();
//
//        double total = 0.0;
//
//        if (codigo == 1) {
//            total = quantidade * 4.00;
//        } else if (codigo == 2) {
//            total = quantidade * 4.50;
//        } else if (codigo == 3) {
//            total = quantidade * 5.00;
//        } else if (codigo == 4) {
//            total = quantidade * 2.00;
//        } else if (codigo == 5) {
//            total = quantidade * 1.50;
//        } else {
//            System.out.println("Código inválido.");
//            sc.close();
//            return;
//        }
//
//        System.out.printf("Total: R$ %.2f%n", total);
//
//        sc.close();

            //06:
//         Scanner sc = new Scanner(System.in);
//                double valor = sc.nextDouble();
//
//        if (valor >= 0.0 && valor <= 25.0) {
//            System.out.println("Intervalo [0,25]");
//        }
//        else if (valor > 25.0 && valor <= 50.0) {
//            System.out.println("Intervalo (25,50]");
//        }
//        else if (valor > 50.0 && valor <= 75.0) {
//            System.out.println("Intervalo (50,75]");
//        }
//        else if (valor > 75.0 && valor <= 100.0) {
//            System.out.println("Intervalo (75,100]");
//        }
//        else {
//            System.out.println("Fora de intervalo");
//        }
//
//        sc.close();


        //07:
//        Locale.setDefault(Locale.US);
//        Scanner sc = new Scanner(System.in);
//
//        double x = sc.nextDouble();
//        double y = sc.nextDouble();
//
//        if (x == 0.0 && y == 0.0) {
//            System.out.println("Origem");
//        }
//        else if (x == 0.0) {
//            System.out.println("Eixo Y");
//        }
//        else if (y == 0.0) {
//            System.out.println("Eixo X");
//        }
//        else if (x > 0.0 && y > 0.0) {
//            System.out.println("Q1");
//        }
//        else if (x < 0.0 && y > 0.0) {
//            System.out.println("Q2");
//        }
//        else if (x < 0.0 && y < 0.0) {
//            System.out.println("Q3");
//        }
//        else {
//            System.out.println("Q4");
//        }
//
//        sc.close();




//            08:
//        Locale.setDefault(Locale.US);
//        Scanner sc = new Scanner(System.in);
//        double salario = sc.nextDouble();
//        sc.close();
//
//        double imposto = 0.0;
//
//        if (salario > 4500.00) {
//            imposto += (salario - 4500.00) * 0.28;
//            salario = 4500.00;
//        }
//        if (salario > 3000.00) {
//            imposto += (salario - 3000.00) * 0.18;
//            salario = 3000.00;
//        }
//        if (salario > 2000.00) {
//            imposto += (salario - 2000.00) * 0.08;
//        }
//
//        if (imposto == 0.0) {
//            System.out.println("Isento");
//        } else {
//            System.out.printf("R$ %.2f%n", imposto);
//        }


//        plus usando switch case:
//        Locale.setDefault(Locale.US);
//        Scanner sc = new Scanner(System.in);
//        double salarioInput = sc.nextDouble();
//        sc.close();
//
//        double imposto = 0.0;
//        int faixa;
//
//        // Determina em qual faixa a renda se encaixa
//        if (salarioInput > 4500.00) {
//            faixa = 3;
//        } else if (salarioInput > 3000.00) {
//            faixa = 2;
//        } else if (salarioInput > 2000.00) {
//            faixa = 1;
//        } else {
//            faixa = 0;
//        }
//
//        double resto = salarioInput;
//        switch (faixa) {
//            case 3:
//                imposto += (resto - 4500.00) * 0.28;
//                resto = 4500.00;
//            case 2:
//                imposto += (resto - 3000.00) * 0.18;
//                resto = 3000.00;
//            case 1:
//                imposto += (resto - 2000.00) * 0.08;
//                break;
//            case 0:
//                break;
//        }
//
//        if (imposto == 0.0) {
//            System.out.println("Isento");
//        } else {
//            System.out.printf("R$ %.2f%n", imposto);
//        }

        //fim dos desafios de estrutura condicional.

//        desafios de estrutura repetitiva:
            //01:
//        Locale.setDefault(Locale.US);
//        Scanner sc = new Scanner(System.in);
//
//        int x = sc.nextInt();
//
//        for (int i=1; i<=x; i++) {
//            if (i % 2 != 0) {
//                System.out.println(i);
//            }
//        }
//
//        sc.close();


                //02:
//        Locale.setDefault(Locale.US);
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//
//        int in = 0;
//        int out = 0;
//
//        for (int i=0; i<n; i++) {
//            int x = sc.nextInt();
//            if (x >= 10 && x <= 20) {
//                in = in + 1;
//            }
//            else {
//                out = out + 1;
//            }
//        }
//
//        System.out.println(in + " in");
//        System.out.println(out + " out");
//
//        sc.close();

        //03:
    //        Locale.setDefault(Locale.US);
//        Scanner sc = new Scanner(System.in);
//
//        int n = sc.nextInt();
//        int x = sc.nextInt();
//        double peso1 = 2.0;
//        double peso2 = 3.0;
//        double peso3 = 5.0;
//
//        double soma = (peso1 + peso2 + peso3);
//
//        for (int i=0; i<n; i++); {
//
//                double a = sc.nextDouble();
//                double b = sc.nextDouble();
//                double c = sc.nextDouble();
//
//                double media = (soma) / 10.0;
//
//                System.out.printf("%.1f%n",  media);
//        }


        //04:
//        Scanner sc = new Scanner(System.in);
//
//        int n = sc.nextInt();
//
//        for (int i=0; i<n; i++) {
//
//            int x = sc.nextInt();
//            int y = sc.nextInt();
//
//            if (y == 0) {
//                System.out.println("divisão impossivel");
//            }
//            else {
//                double div = (double) x / y;
//                System.out.printf("%.1f%n", div);
//            }
//        }
//
//        sc.close();



        //05:
//        Scanner sc = new Scanner(System.in);
//
//        int n = sc.nextInt();
//
//        int fatorial = 1;
//        for (int i=1; i<=n; i++) {
//            fatorial = fatorial * i;
//        }
//
//        System.out.println(fatorial);
//
//        sc.close();



            //06:
//        Scanner sc = new Scanner(System.in);
//
//        int n = sc.nextInt();
//
//        for (int i=1; i<=n; i++) {
//                if (n % i == 0 );
//                System.out.println(i);
//
//        }

            //07:
//        Scanner sc = new Scanner(System.in);
//
//        int n = sc.nextInt();
//
//        for (int i=1; i<=n; i++) {
//
//            int primeiro = i;
//            int segundo = i * i;
//            int terceiro = i * i * i;
//            System.out.printf("%d %d %d%n", primeiro, segundo, terceiro);
//        }
//
//        sc.close();
        //fim dos desafios de for.



//            programação orientada a objetos
//            Scanner sc = new Scanner(System.in);
//            Locale.setDefault(Locale.US);
//
//            double x = sc.nextDouble();
//            double k = sc.nextDouble();
//            double l = sc.nextDouble();
//
//            double p = (x+k+l / 2);
//
//            System.out.println("X é igual:" + p);
//
//        double a = sc.nextDouble();
//        double b = sc.nextDouble();
//        double c = sc.nextDouble();
//
//        double m = (a+b+c / 2);
//
//        System.out.println("Y é igual:" + m);







        }


        }








