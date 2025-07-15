function SeuNome({setNome}){
    return(
    <>
    <p>Digite o seu nome:
        <input type="text" placeholder="Qual é o seu nome?"  onChange={(e)=> setNome(e.target.value)}/></p></>
    )
}
export default SeuNome