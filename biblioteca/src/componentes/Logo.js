import './BibliotecaVirtual.module.css'
import LogoutIcon from '@mui/icons-material/Logout';
import BookIcon from '@mui/icons-material/Book';
import { Link, useLocation } from 'react-router-dom';
import Tabela from '../tabela/Tabela';

function Logo(){
    const location = useLocation()
    const nome = location.state?.nome || "usuário"
    return(
    <nav>
        <BookIcon sx={{
            color: 'white', 
            marginTop: '8px'
        }}/>

        <h1>Biblioteca Virtual</h1>

        <h3>Olá, {nome}</h3>

        <Link to={'/'}>
            <LogoutIcon sx={{
                color: 'white', 
                marginLeft: 'auto', 
                justifyContent: 'center',
                marginTop: '8px'
            }}/>
        </Link>
        <br/>
        <Tabela/>
    </nav>

    )
}

export default Logo
