import { useState, useEffect } from 'react'

import Input from '../form/Input'
import Select from '../form/Select'
import SubmitButton from '../form/SubmitButton'

import styles from './ProjectForm.module.css'

function ProjectForm({btnText}) {
    const [categories, setCategories] = useState([])

    useEffect(() => {
        fetch("http://localhost:5000/categories", {
            method: "GET",
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then((resp) => resp.json())
            .then((data) => {
                setCategories(data)
            })
            .catch((err) => console.log(err))
    }, [])

    return (
        <form className={styles.form}>
            <Input 
                type="text"
                text="Nome do projeto"
                name="name"
                placeholder="Insira o nome do projeto"
            />

             <Input 
                type="number"
                text="Orçamento do projeto"
                name="budget"
                placeholder="Insira o orçamento total"
            />
            <Select
                name="category_id" 
                text="Selecione a categoria"
                options={categories}
            />

            <SubmitButton text={btnText}/>
        </form>
    )
}

// <Select>: Uma caixinha de opções onde um usuário pode escolher uma opção
// <option disabled>: Essa é uma opção que aparece primeiro, tipo um título ou instrução, porém não pode ser selecionada
// Disabled não deixa a pessoa enviar o formulário se não escolher nada de verdade

export default ProjectForm
