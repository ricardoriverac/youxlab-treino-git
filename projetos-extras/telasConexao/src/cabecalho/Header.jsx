import "./Header.css";
import loogHeader from "../img/logoHeader.svg";
import { useState, useEffect } from "react";
import iconRelogio from "../img/iconRelogio.svg";

function Header() {
  const [horaAtual, setHoraAtual] = useState(new Date());

  useEffect(() => {
    const intervalo = setInterval(() => {
      setHoraAtual(new Date());
    }, 1000);

    return () => clearInterval(intervalo);
  }, []);

  function formatarData(data) {
    return data
      .toLocaleDateString("pt-BR", {
        day: "2-digit",
        month: "short",
        year: "numeric",
      })
      .replace(/\bde\b/gi, "")
      .replace(/\s+/g, " ")
      .trim();
  }

  function formatarHora(data) {
    return data.toLocaleTimeString("en-US", {
      hour: "2-digit",
      minute: "2-digit",
      hour12: true,
    });
  }

  return (
    <div className="div_header">
      <div className="conexao_literaria">
        <span className="tittle">
          <img src={loogHeader} alt="Conexão Literária" />
        </span>
      </div>

      <div className="hora_data">
        <span className="hora_atual">
          {formatarData(horaAtual)}
          <img
            src={iconRelogio}
            alt="Ícone Relógio"
            style={{
              width: 15,
              marginLeft: 15,
              marginRight: 15,
            }}
          />
          {formatarHora(horaAtual)}
        </span>
      </div>
    </div>
  );
}

export default Header;
