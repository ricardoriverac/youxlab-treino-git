import { useState } from "react"

function Escolha() {

   const [email, setEmail] = useState()
   const [userEmail, setUserEmail] = useState()


   function enviarEmail(e) {
      e.preventDefault()
      setUserEmail(email)
      console.log('Testando')
   }

   function limparEmail() {
         setUserEmail(" ")
      }


   return (
      <div>
         <h2>Coloque seu Email:</h2>
         <form>
            <input type="email" placeholder="Digite o seu email..." 
            onChange={(e) => setEmail(e.target.value)}/>
            <button onClick={enviarEmail}>
               Enviar Email
            </button>
            {userEmail && (
               <div>
                  <p>O e-mail do usuario e:{userEmail}</p>
                  <button onClick={limparEmail}>Limapar </button>
               </div>
            )}
         </form>
      </div>
   )

}

export default Escolha