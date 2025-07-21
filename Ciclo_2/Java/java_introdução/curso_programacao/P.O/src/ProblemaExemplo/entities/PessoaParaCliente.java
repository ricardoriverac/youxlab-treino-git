package ProblemaExemplo.entities;

public class PessoaParaCliente {

    public int id;
    public String name;
    public double salary;


    public PessoaParaCliente (int id, String name, double salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }


    @Override
    public String toString() {
        return "ID: " + id + ", Name: " + name + ", Salary: " + String.format("%.2f", salary);
    }

    public PessoaParaCliente() {
        return;
    }


    public int getId() {
        return id;
    }

    public double getSalary() {
        return salary;
    }

    public String getName() {
        return name;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public void setName(String name) {
        this.name = name;
    }
}
