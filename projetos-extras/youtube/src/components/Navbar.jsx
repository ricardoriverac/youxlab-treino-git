import { MdOutlineMenu } from "react-icons/md";
import logo from '../img/logo.png'
import lupa from '../img/lupa.png'
import "./Navbar.css";

function Navbar() {
  return (
    <div className="container">
      <div className="menu_logo">
        <button>
          <MdOutlineMenu />
        </button>
        <img src={logo} alt="Página inicial do Youtube" />
      </div>
      <div className="pesquisar">
        <div>
            <input type="search" placeholder="Pesquisar" className="input-com-icone" />
        </div>
      </div>
    </div>
  );
}

export default Navbar;
