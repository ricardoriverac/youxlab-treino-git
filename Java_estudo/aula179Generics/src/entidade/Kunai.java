package entidade;

    public class Kunai {
        private String habilidade;

        public Kunai(String habilidade) {
            this.habilidade = habilidade;
        }

        public String getHabilidade() {
            return habilidade;
        }

        public void setHabilidade(String habilidade) {
            this.habilidade = habilidade;
        }

        @Override
        public String toString() {
            return "Kunai{" +
                    "habilidade='" + habilidade + '\'' +
                    '}';
        }
    }
