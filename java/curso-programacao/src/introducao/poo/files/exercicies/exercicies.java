package introducao.poo.files.exercicies;

// /home/youx/workspace-git/youxlab-treino-git/java/curso-programacao/src/introducao/poo/files/exercicies
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class exercicies {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        //home/youx/workspace-git/youxlab-treino-git/java/curso-programacao/src/introducao/poo/files/exercicies

        // Criando o arquivo.csv com o conteudo dentro
        System.out.print("Entre com o caminho: ");
        String caminho = input.nextLine();
        System.out.println("Entre com o nome do arquivo: ");
        String nome = input.nextLine();
        System.out.println(caminho + nome);
        // File separator e o mesmo de eu colocar "/"
        File file = new File(caminho + File.separator + nome);
        boolean arquivocsv = file.createNewFile();
        System.out.println("deu: " + arquivocsv);

        // Colocando conteúdo dentro do arquivo
        Product product  = new Product("Tv" , 1200.00 , 2 );
        Product product1  = new Product("Balco" , 1500.00 , 1);
        Product product2 = new Product("Falco" , 1100.00 , 3);
        Product product3 = new Product("Falco" , 1100.00 , 3);
        FileWriter fileWriter = new FileWriter(file , true);
        fileWriter.write(product.getNome() + "," + product.getPrice() + "," + product.getQnt() + "\n");
        fileWriter.write(product1.getNome() + "," + product1.getPrice() + "," + product1.getQnt() + "\n");
        fileWriter.write(product2.getNome() + "," + product2.getPrice() + "," + product2.getQnt() + "\n");
        fileWriter.close();
        System.out.println(file);

        //Parte do out
        File pastaout = new File(caminho + "/out");
        boolean foi = pastaout.mkdir();
        System.out.println("foi = "+ foi);
        File out = new File(pastaout + "/summary.csv");
        boolean foi1 = out.createNewFile();
        System.out.println("Arquivo summary" + foi1);
        FileWriter fwout = new FileWriter(out);
        fwout.write(product.getNome() + "," + product.getPrice() * product.getQnt() + "\n");
        fwout.write(product1.getNome() + "," + product1.getPrice() * product1.getQnt() + "\n");
        fwout.write(product2.getNome() + "," + product2.getPrice() * product2.getQnt() + "\n");
        fwout.close();
        input.close();
    }
}


