package introducao.poo.exercicios.entities;

public class Funcionario {
    private Integer id;
    private String nome;
    private Double salary;
    
    public void aumentoSalario(double porcertagem ){
        // 10
        this.salary += (this.salary * porcertagem/100);
    }

    public String getNome() {
        return nome;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    public Double getSalary() {
        return salary;
    }
}
