package Seção16.DefaultMethods;

// Interface com operação matemática genérica
interface OperacaoMatematica {

    // Método abstrato - precisa ser implementado
    double executar(double a, double b);

    // Método default - já vem com implementação
    default void mostrarResultado(double a, double b) {
        double resultado = executar(a, b);
        System.out.println("Resultado da operação: " + resultado);
    }
}

// Classe que implementa soma
class Soma implements OperacaoMatematica {
    @Override
    public double executar(double a, double b) {
        return a + b;
    }
}

// Classe que implementa subtração
class Subtracao implements OperacaoMatematica {
    @Override
    public double executar(double a, double b) {
        return a - b;
    }
}

// Classe principal
public class Main {
    public static void main(String[] args) {
        // Criando instâncias das operações
        OperacaoMatematica soma = new Soma();
        OperacaoMatematica subtracao = new Subtracao();

        // Usando o método default para exibir resultados
        System.out.println("Soma:");
        soma.mostrarResultado(10, 5);        // Resultado: 15.0

        System.out.println("\nSubtração:");
        subtracao.mostrarResultado(10, 5);   // Resultado: 5.0
    }
}
