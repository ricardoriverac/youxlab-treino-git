function Saudacao({ nome }) {

function gerarSaudacao(algumNome){
    return `Olá, ${algumNome}, tudo bem?`
}

  return (
    <>
      {nome && <p>{gerarSaudacao(nome)}</p>}  {/* Se tiver nome gera parágrafo */}
    </>
  );
}

export default Saudacao;
