import { useState } from "react";

import styles from "./Formulario.module.css";

import Input from "./Input";

function Formulario() {
  return (
    <form className={styles.form}>
      <Input text="Nome" type="text" name="nome" placeholder="Digite o nome" />
      <Input text="CPF" type="number" name="cpf" placeholder="Digite o CPF" />
      <Input
        text="Data de nascimento"
        type="date"
        name="data de nascimento"
        placeholder="Digite a data de nascimetno"
      />
      <div>
        <button className={styles.btnSalvar}>Salvar</button>
      </div>
    </form>
  );
}

export default Formulario;
