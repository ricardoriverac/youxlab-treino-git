package entidade;

public class Pergaminho {
    private String conteudo;

    public Pergaminho(String conteudo) {
        this.conteudo = conteudo;
    }

    public String getConteudo() {
        return conteudo;
    }

    public void setConteudo(String conteudo) {
        this.conteudo = conteudo;
    }

    @Override
    public String toString() {
        return "Pergaminho{" +
                "conteudo='" + conteudo + '\'' +
                '}';
    }
}

