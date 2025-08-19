package execucao;

import entities.Employee;

import java.io.BufferedReader;   // Leitor de texto com buffer
import java.io.FileReader;       // Leitor de arquivo
import java.io.IOException;      // Exceção para erro de leitura
import java.util.ArrayList;      // Lista dinâmica
import java.util.Collections;    // Utilitário para ordenar listas
import java.util.List;           // Interface de lista

public class Programa {
    public static void main(String[] args) {
        // Cria uma lista de funcionários
        List<Employee> list = new ArrayList<>();

        // Caminho do arquivo
        String path ="/home/youx/youxlab-treino-git/Java_estudo/aula175InterfaceComparable/meuDeus";

        // Bloco para tentar ler o arquivo
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {

            // Lê a primeira linha do arquivo
            String employeeCsv = br.readLine();

            // Enquanto ainda houver linhas no arquivo
            while (employeeCsv != null) {
                // Divide os dados separados por vírgula
                String[] fields = employeeCsv.split(",");

                // Cria e adiciona um novo funcionário à lista
                list.add(new Employee(fields[0], Double.parseDouble(fields[1])));

                // Lê a próxima linha
                employeeCsv = br.readLine();
            }

            // Ordena a lista com base no que estiver definido na classe Employee
            Collections.sort(list);

            // Exibe os funcionários ordenados
            for (Employee emp : list) {
                System.out.println(emp.getName() + ", " + emp.getSalary());
            }

        } catch (IOException e) {
            // Caso dê erro ao ler o arquivo
            System.out.println("Erro: " + e.getMessage());
        }
    }
}

