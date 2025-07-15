package POO;

public class RegistraAluno {
       private String nome;
       private String endereco;
       private int idade;
       private double notap;
       private double notam;
       private double notag;
        private static int contadorEstudante;

        public String getNome(){
            return nome;
        }
        public void setNome(String temp){
            nome = temp;
        }

    public String getEndereco(){
        return endereco;
    }
        public void setEndereco(String temp){
            endereco = temp;
        }

    public int getIdade(){
        return idade;
    }
        public int setEndereco(int temp) {
            idade = temp;
            return idade;
        }
            public void setNotam(double temp){
            notam = temp;
            }
                public void setnotap(double temp){
                notap = temp;
                }
                    public void setnotag(double temp){
                    notag = temp;
                    }
        public double getMedia(){
            double resultado = 0;
            resultado = (notag + notap + notam) / 3;
            return resultado;
        }
        public static int getQuantidadeAlunos(){
            return contadorEstudante;
        }


    }
