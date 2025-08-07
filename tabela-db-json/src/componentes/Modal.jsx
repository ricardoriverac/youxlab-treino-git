import * as React from "react";
import { useState, useEffect } from "react";
import styles from "./Modal.module.css";
import Form from "./Form";
import { editarUser } from '../service/api'

function Modal({ pessoa, abrirModal, fecharModal }) {
  const [nomeEdit, setNomeEdit] = useState('');
  const [idadeEdit, setIdadeEdit] = useState('');
  const [estadoCivilEdit, setEstadoCivilEdit] = useState('');
  const [cpfEdit, setCpfEdit] = useState('');

  useEffect(() => {
    if(pessoa){
      setNomeEdit(pessoa.nome)
      setEstadoCivilEdit(pessoa.estadoCivil)
      setIdadeEdit(pessoa.idade)
      setCpfEdit(pessoa.cpf)
    }
  },[pessoa])

  const handleChangeName = (e) => {
    setNomeEdit(e.target.value);
  };

  const handleChangeIdade = (e) => {
    setIdadeEdit(e.target.value);
  };

  const handleChangeEstadoCivil = (e) => {
    setEstadoCivilEdit(e.target.value);
  };

  const handleChangeCpf = (e) => {
    setCpfEdit(e.target.value);
  };

  const montarObjeto = () => {
    let pessoaSalvar = {
      nome: nomeEdit,
      idade: idadeEdit,
      estadoCivil: estadoCivilEdit,
      cpf: cpfEdit
    }
    editarUser(pessoa.id, pessoaSalvar)
    fecharModal()
  }

  return (
    <>
      <div className={styles.modal}>
        {abrirModal && (
          <div className={styles.modal_edit}>
            <div className={styles.modal_cont}>
              <h2 className={styles.title}>Atualizar Cadastro</h2>

              <Form
                text="Nome"
                type="text"
                name="name"
                value={nomeEdit}
                onChange={handleChangeName}
              />

              <Form text="Idade" type="number" name="name" value={idadeEdit} onChange={handleChangeIdade}/>

              <Form
                text="Estado Civil"
                type="text"
                name="name"
                value={estadoCivilEdit}
                onChange={handleChangeEstadoCivil}
              />

              <Form text="CPF" type="number" name="name" value={cpfEdit} onChange={handleChangeCpf}/>

              <div className={styles.btn_info}>
                <button className={styles.btn_salvar} onClick={montarObjeto}>Salvar</button>
                <button className={styles.btn_fechar} onClick={fecharModal}>
                  Fechar
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </>
  );
}

export default Modal;
