import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

class Usuario{
    private String nome;
    private String email;
    private String senha;

    public Usuario(String nome, String email, String senha){
        this.nome = nome;
        this.email = email;
        this.senha = senha;        
    }

    @Override
    public String toString(){
        return "{" + nome + email + senha + "}";
    }

}
public class teste2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        List<Usuario> pessoas = new ArrayList<>();
        while (true){
            System.out.print("Digite seu nome: ");
            String nome = input.nextLine();
            
            System.out.print("Digite seu email: ");
            String email = input.nextLine();

            System.out.print("Defina sua senha: ");
            String senha = input.nextLine();

            pessoas.add(new Usuario(nome, email, senha));
            System.out.println("Digite (N) para parar");
            String pare = input.nextLine();
            if(pare == "N"){
                break;
            }

        
        }

        
    }
}
