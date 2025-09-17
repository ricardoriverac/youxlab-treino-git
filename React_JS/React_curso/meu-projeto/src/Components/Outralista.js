function OutraLista({itens}){
    return(
        <>
        <h3>Lista de coisas boas: </h3>
        {itens.length > 0 ?(                    // se tiver mais de 0 itens na lista
            itens.map((item, index)=>(
                <p key={index}>{item}</p>
            ))) : (                             // se não
                <p>Não há itens na lisa!</p>
            )
        }   
        </>
    )
}

export default OutraLista


