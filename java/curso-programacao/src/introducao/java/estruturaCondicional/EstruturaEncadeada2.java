package introducao.java.estruturaCondicional;

public class EstruturaEncadeada2 {
    public static void main(String[] args) {
        // idade < 15 caterogoria infantil
        // idade >= 15 && idade < 19 caterigoria juvenil
        // idade >= 18 caterigoria adulto

        int idade = 12;
        String categoria;

        if (idade < 15){
            categoria = "Categoria infaltil";

        }else if(idade >= 15 && idade < 18){
            categoria = "Categoria Juvenil";

        }else {
            categoria = "Categoria Adulta";

        }

        System.out.println(categoria);
    }
}
