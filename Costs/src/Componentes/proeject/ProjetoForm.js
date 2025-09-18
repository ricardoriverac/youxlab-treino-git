import styles from "./ProjetoForm.module.css";
import Input from "../Form/input";
import Select from "../Form/select";

function ProjetoForm() {
  return (
    <form className={styles.form}>
      <Input
        type="text"
        text="Nome do projeto"
        name="name"
        placeholder="insira o nome do projeto"
      />
      <div>
        <Input
        type="text"
        text="Nome do projeto"
        name="budget"
        placeholder="insira o orçamento do projeto"
      />
      </div>
      <div>
       <Select name="category_id" text="Selecione a categoria"/>
      </div>
      <div>
        <input type="submit" value="Criar projeto" />
      </div>
    </form>
  );
}

export default ProjetoForm;
