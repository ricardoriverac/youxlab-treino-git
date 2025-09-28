import React, { useEffect, useState } from "react";
import { infomacesToken } from "../services/api";
import Loading from "../utils/Loading";

export default function Dashboard() {
  const [idEscola, setIdEscola] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const id = infomacesToken()?.id_escola;
    if (id) {
      setIdEscola(id);
    } else {
      alert("Erro ao recuperar o ID da escola.");
    }
  }, []);

  useEffect(() => {
    if (idEscola) {
      setLoading(true); // Garante que o loading fique ativo enquanto o iframe carrega
    }
  }, [idEscola]);

  const dashboardUrl = `https://conexaoliteraria.youxgroup.com.br/dados/?id_escola=${idEscola}&embed=true`;

  return (
    <div>
      {idEscola && (
        <iframe
          title="Dashboard"
          src={dashboardUrl}
          style={{ width: "95vw", height: "94vh", border: "none" }}
          onLoad={() => setLoading(false)}
          onError={() => {
            setLoading(false);
            alert("Erro ao carregar o dashboard.");
          }}
        ></iframe>
      )}
    </div>
  );
}