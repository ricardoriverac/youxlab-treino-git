package entidades;

import java.util.Date;

public class Banco {
   private String nome;
   private Integer cep;
   private ContaBancaria contaBancaria;

   public Banco(){
   }
   public Banco (String nome, Integer cepQueVaiChegar, ContaBancaria contaBancariaQueEstaChegando) {
        this.nome = nome;
        this.cep = cepQueVaiChegar;
        this.contaBancaria = contaBancariaQueEstaChegando;
   }

   public void setNome(String nome){
       this.nome = nome;
   }

   public String getNome(){
       return this.nome;
   }
   public void setCep(Integer cep){
       this.cep = cep;
   }
   public Integer getCep(){
       return this.cep;
   }
   public void setContaBancaria(ContaBancaria cb) {
       this.contaBancaria = cb;
   }

    public ContaBancaria getContaBancaria() {
        return contaBancaria;
    }

    @Override
    public String toString() {
        return "Banco{" +
                "nome='" + nome + '\'' +
                ", cep=" + cep +
                ", contaBancaria=" + contaBancaria +
                '}';
    }
}