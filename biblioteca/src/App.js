import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'

import './App.css';
import TelaLogin from './componentes/TelaLogin';
import TelaEntrar from './componentes/TelaEntrar';
import BibliotecaVirtual from './componentes/BibliotecaVirtual';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
            <Route path='/' element={<TelaLogin/>}></Route>
            <Route path='/criarconta' element={<TelaEntrar/>}></Route>
            <Route path='/bibliotecavirtual' element={<BibliotecaVirtual/>}></Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
