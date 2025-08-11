function Saudacao({nome}){

    function PararSaudacao(algumnome){
           
        return `ola, ${algumnome} tudo bem`  
    }

    return(
        <>
          {nome && <p>{PararSaudacao(nome)}</p>}
        </>
    )
}

export default Saudacao