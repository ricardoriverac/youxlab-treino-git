import { useState } from "react"

function Condicional(){
    const [email, setEmail] = useState()
    const [userEmail, setUserEmail] = useState()

    function enviarEmail(e){
        e.preventDefault()
        setUserEmail(email)
    }

    function limparEmail(){
        setUserEmail('')
    }

    return(
        <div>
            <h2>Cadastre o seu e-mail:</h2>
            <form>
                <input 
                    type="email" 
                    placeholder="Digite o seu e-mail..."
                    onChange={(e) => setEmail(e.target.value)} // Sempre o valor do elemento é modificado pelo usuário é utilizado o evento onchange que é usado para definir uma função que será executada sempre que esse evento ocorrer
                />
                <button type="submit" onClick={enviarEmail}>Enviar-email</button>
                {userEmail && ( // Quando o userEmail estiver preenchido essa div aparece
                    <div>
                        <p>O e-mail do usuário é: {userEmail}</p>
                        <button onClick={limparEmail}>Limpar e-mail</button>
                    </div>
                )}
            </form>
        </div>
    )

}

export default Condicional
