package introducao.java.estruturaCondicional;

public class ExpressaoCondicionalTermica {
    public static void main(String[] args) {
        double preco = 47.5;
        double desconto = (preco < 5) ? preco * 2 : preco * 1.5;
        System.out.println("Desconto ficou" + desconto);
        // Doar se salario > 5000

        double salario = 6000;
        String mensagemDoar = "Eu vou doar 500 pro jander";
        String mensagemNaoDoar = "Ainda não tenho dinheiro";
        // (condicao) ? verdadeiro : falso ;

        String resultado = salario > 5000 ? mensagemDoar : mensagemNaoDoar ;
        System.out.println(resultado);
    }
}
