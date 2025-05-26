package desafiobanco;

public class ContaAplicacao {
    public static void main(String[] args) {
        ContaBancaria conta1 = new ContaBancaria(1222, "Miguel", 100.2);
        ContaBancaria conta2 = new ContaBancaria(3444, "Pedro Henrique", 350);
        ContaBancaria conta3 = new ContaBancaria(5612, "Maria", 1000);

        BancoKev banco = new BancoKev();

        banco.adicionarConta(conta1);
        
        banco.adicionarConta(conta2);
        banco.adicionarConta(conta3);

        banco.exibirConta(1222);
        System.out.println("=======================");
        

        banco.transferir(1222, 5612, 100);

        System.out.println("=======================");
        conta1.mostrarConta();

        System.out.println("=======================");
        conta3.mostrarConta();
        
        System.out.println("=======================");


        
    }
}
