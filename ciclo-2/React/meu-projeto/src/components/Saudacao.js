function Saudacao({nome}){
    function gerarSaudacao(algumNome){
        return `Olá, ${algumNome}, tudo bemmm?`
    }
return <>{nome && <p> {gerarSaudacao(nome)}</p>}</>;
    
}

export default Saudacao