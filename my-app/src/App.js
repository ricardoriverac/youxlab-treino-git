import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom'
import Home from './pages/Home'
import Empresa from './pages/Empresa'
import Contato from './pages/Contato'
import Navbar from './components/layout/Navbar'
import Footer from './components/layout/Footer'

function App () {

  return(
    // Router ativa o sistema de rotas
    <Router> 
      <Navbar/>
      <Routes>
        <Route exact path='/' element={<Home/>}/>
        <Route path='/empresa' element={<Empresa/>}/>
        <Route path='/contato' element={<Contato/>}/>
      </Routes>
      <Footer/>
    </Router>
  )
}

export default App
