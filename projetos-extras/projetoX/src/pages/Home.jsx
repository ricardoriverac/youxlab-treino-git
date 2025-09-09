import Tabela from "../layout/Tabela";
import "./Home.css";

function Home() {
  return (
    <div>
      <div className="divTotalizador">
        <div className="totalizador">Total de produtos</div>
        <div className="totalizador">Preço total</div>
        <div className="totalizador">3</div>
      </div>
      <Tabela />
    </div>
  );
}

export default Home;
