function Form(){
    function cadastrarUsuario(e){
        e.preventDefault()
        console.log("Cadastrou o usuario")
    }
    return(
        <>
        <h1>Meu cadastro:</h1>
        <form onSubmit={cadastrarUsuario}> 
            <>
            <input type="text" placeholder="Qual é o seu nome?f" />
            </>
            <>
            <input type="submit"  value="Cadastrar"/>
            </>
        </form>
        </>
    )
}

export default Form