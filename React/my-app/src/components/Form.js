import { useState } from "react"


function Form(){

      function cadastraUsuario(e) {
        e.preventDefault()
        console.log(`O usuario ${name} foi  cadastrado com a senha ${password}`)
      }

      const [name, setName] = useState()
      const [password, setPassword] = useState()

      return(
        <div>
            <h1>
                <form onSubmit={cadastraUsuario}>
                    <div>
                        <label htmlFor="name">Nome:</label>
                        <input 
                        type="text" 
                        id="name" 
                        name="name" 
                        placeholder="Digite o seu nome"
                        onChange={(e) =>setName(e.target.value)}
                        />
                    </div>
                    <div>
                        <label htmlFor="password">Senha:</label>
                        <input 
                        type="password" 
                        id="password" 
                        name="passwoed" 
                        placeholder="Digite o sua senha"
                        onChange={(e) =>setPassword(e.target.value)}
                        />
                    </div>
                    <div>
                        <input  type="submit" value="Cadastrar"/>
                    </div>
                </form>
            </h1>
        </div>
      )
}


export default Form