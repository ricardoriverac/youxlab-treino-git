function Form(){

      function cadastraUsuario(e) {
        e.preventDefault()
        console.log("Cadastrou")
      }


      return(
        <div>
            <h1>
                <form onSubmit={cadastraUsuario}>
                    <div>
                        <input type="text" placeholder="Digite o seu nome"/>
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