const caixaCursos=document.querySelector('#caixaCursos')
const btn_c=[...document.querySelectorAll('.curso')]
const c1_2=document.querySelector('#c1_2') 
const cursos = ['HTML', 'CSS', 'JavaScript', 'PHP', 'React', 'Python', 'MySQL']
const btnCursoSelecionado=document.getElementById('btnCursoSelecionado')
const btnRemoverCursos=document.getElementById('btnRemoverCursos')
const btnAdicionarNovosCursos = document.getElementById('btnAdicionarNovosCursos')
const btnAdicionarAntes = document.getElementById('btnAdicionarAntes')
const btnAdicionarDepois = document.getElementById('btnAdicionarDepois')


cursos.map((el, chave)=>{
    const novoElemento=document.createElement('div')
    novoElemento.setAttribute('id', 'c'+chave)
    novoElemento.setAttribute('class', 'curso c1')
    novoElemento.innerHTML=el


    const comandos =document.createElement('div')
    comandos.setAttribute('class', 'comandos')

    const rb= document.createElement('input')
    rb.setAttribute('type', 'radio')
    rb.setAttribute('name', 'rb_curso')

    comandos.appendChild(rb)

    novoElemento.appendChild(comandos)

    caixaCursos.appendChild(novoElemento)
})

const radioSelecionado=()=>{
    const todosRadios=[...document.querySelectorAll('input[type=radio]')]
    let radioSelecionado = todosRadios.filter((ele, ind, arr)=>{
        return ele.checked
    })
    return radioSelecionado[0]

}
    
btnCursoSelecionado.addEventListener('click', (evt)=>{
    const rs=radioSelecionado()
    console.log(rs)
    if(rs!=undefined){
        const cursoSelecionado = rs.parentNode.previousSibling.textContent
        alert('Curso selecionado: ' + cursoSelecionado) 
   }else {
        alert('Selecione o curso.') 
   }  
    
})

btnRemoverCursos.addEventListener('click', (evt)=>{
    const rs=radioSelecionado()
    if(rs!=undefined){
        const cursoSelecionado = rs.parentNode.parentNode
        cursoSelecionado.remove()
    }else{
        alert('Selecione o curso.')
    }
})

btnAdicionarNovosCursos.addEventListener('click', (evt)=>{
    const novoCurso =document.getElementById('nomeCurso').value
    const novoElementos = document.createElement('div')
    novoElementos.setAttribute('class', 'curso c1')
    novoElementos.innerHTML=novoCurso
    const comandos =document.createElement('div')
    comandos.setAttribute('class', 'comandos')

    const rb= document.createElement('input')
    rb.setAttribute('type', 'radio')
    rb.setAttribute('name', 'rb_curso')

    comandos.appendChild(rb)

    novoElementos.appendChild(comandos)

    caixaCursos.appendChild(novoElementos)
})

btnAdicionarAntes.addEventListener('click', (evt)=>{
   const novoCurso =document.getElementById('nomeCurso').value
    const novoElementos = document.createElement('div')
    novoElementos.setAttribute('class', 'curso c1')
    novoElementos.innerHTML=novoCurso
    const rs=radioSelecionado()
    console.log(rs)
    if(rs!=undefined){
        const cursoSelecionado = rs.parentNode.previousSibling.textContent
        console.log(caixaCursos)
        caixaCursos.insertBefore(novoCurso, cursoSelecionado)
   }else {
        
    alert('adicione o curso')
   }  
    const comandos =document.createElement('div')
    comandos.setAttribute('class', 'comandos')

    const rb= document.createElement('input')
    rb.setAttribute('type', 'radio')
    rb.setAttribute('name', 'rb_curso')

    comandos.appendChild(rb)

    novoElementos.appendChild(comandos)

    caixaCursos.insertBefore(novoElementos, cursoSelecionado)

    // caixaCursos.insertBefore(cursoSelecionado)
})

btnAdicionarDepois.addEventListener('click', (evt)=>{
   const novoCurso =document.getElementById('nomeCurso').value
    const novoElementos = document.createElement('div')
    novoElementos.setAttribute('class', 'curso c1')
    novoElementos.innerHTML=novoCurso
    const comandos =document.createElement('div')
    comandos.setAttribute('class', 'comandos')

    const rb= document.createElement('input')
    rb.setAttribute('type', 'radio')
    rb.setAttribute('name', 'rb_curso')

    comandos.appendChild(rb)

    novoElementos.appendChild(comandos)

    caixaCursos.insertBefore(novoCurso, cursoSelecionado, nextSibling)

    // caixaCursos.insertBefore(cursoSelecionado)
})