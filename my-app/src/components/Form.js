import { useState } from "react"

function Form () {

    function cadastrarUsuario (e){
        e.preventDefault() // Impede o comportamento padrão de um evento, permitindo ações personalizadas em vez da ações padrões do navegador
        console.log(`Usuário ${name} foi cadastrado com a senha ${password}`)
    }

    const [name, setName] = useState()
    const [password, setPassword] = useState()

    return (
        <div>
            <h1>Meu cadastro</h1>
            <form onSubmit = {cadastrarUsuario}>
                <div>
                    <label htmlFor="name">Nome:</label>
                    <input 
                        type = "text" 
                        id="name" 
                        name="name" 
                        placeholder = "Digite o seu nome"
                        onChange={(e) => setName(e.target.value)} // Cada letra que digita dentro desse campo modifica o valor do UseState
                        />
                </div>

                 <div>
                    <label htmlFor="password">Senha:</label>
                    <input 
                        type = "password" 
                        id="password" 
                        name="password" 
                        placeholder = "Digite a sua senha"
                        onChange={(e) => setPassword(e.target.value)} // Cada letra que digita dentro desse campo modifica o valor do UseState
                    />
                </div>

                <div>
                    <input type = "submit" value = "Cadastrar"/>
                </div>
            </form>
        </div>
    )
}

export default Form
