package execucao;

import Entidades.BolsaNinja;
import Entidades.Kunai;
import Entidades.Pergaminho;
import Entidades.Shuriken;

public class Programa {
    public static void main(String[] args) {
        BolsaNinja<Shuriken> bolsaShuriken = new BolsaNinja<>();
        bolsaShuriken.adicionarFerramenta(new Shuriken("Shuriken Tripla", 12));
        bolsaShuriken.adicionarFerramenta(new Shuriken("Shuriken Simples", 8));
        bolsaShuriken.mostrarNomes();

        System.out.println();

        BolsaNinja<Kunai> bolsaKunai = new BolsaNinja<>();
        bolsaKunai.adicionarFerramenta(new Kunai("Kunai Explosiva", "Explosão"));
        bolsaKunai.adicionarFerramenta(new Kunai("Kunai Silenciosa", "Silêncio"));
        bolsaKunai.mostrarNomes();

        System.out.println();

        BolsaNinja<Pergaminho> bolsaPergaminho = new BolsaNinja<>();
        bolsaPergaminho.adicionarFerramenta(new Pergaminho("Pergaminho de Fogo", "Jutsu Katon"));
        bolsaPergaminho.adicionarFerramenta(new Pergaminho("Pergaminho de Selamento", "Tecnica de selar"));
        bolsaPergaminho.mostrarNomes();
    }
}
