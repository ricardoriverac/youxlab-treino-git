import Group from "../img/Group.png";
import "./Sobre.css";
import fotoLabers from "../img/foto_labers.png";

export default function Sobre() {
  return (
    <div className="container_sobre">
      <h1>Sobre o Instituto YouX</h1>
      <div className="caixa_texto_img">
        <span>
          Fundado em 12 de abril de 2024, na cidade de Lavras/MG, o Instituto
          YouX nasceu a partir da iniciativa da YouX com o propósito de{" "}
          <strong>
            promover a cidadania ativa e a construção de um futuro sustentável
          </strong>
          . Desde então, o Instituto YouX tem atuado para criar oportunidades de
          aprendizado e crescimento profissional, ajudando a moldar uma geração
          de talentos aptos a enfrentar os desafios do cenário digital.
        </span>

        <div>
          <img src={Group} alt="Logo Instituto YouX" />
        </div>
      </div>

      <h1>Sobre o YouX Lab</h1>
      <div className="caixa_sobre_lab">
        <div>
          <p>
            O YouX Lab é um programa social de desenvolvimento de jovens
            talentos que tem como propósito transformar vidas por meio da
            tecnologia e da inovação. Para isso, desenvolvemos uma metodologia
            de ensino inovadora para capacitar e desenvolver talentos do ensino
            médio, oferecendo-lhes a oportunidade de se inserirem no mercado de
            trabalho.
          </p>
          <span>
            O YouX Lab é <strong>totalmente gratuito</strong> e todos os
            participantes do programa, “os Labers”,{" "}
            <strong>recebem todo o apoio necessário</strong> para darem
            continuidade ao seu desenvolvimento no Lab e na escola,{" "}
            <strong>
              como bolsa mensal, auxílio transporte, equipamentos e alimentação
            </strong>{" "}
            no local durante toda a jornada de aprendizado. Além disso, por meio
            de uma parceria com a Fagammon, os participantes do programa ainda
            recebem bolsas de estudos para estimular sua inserção no Ensino
            Superior, exercitando assim o Lifelong Learning.
          </span>
        </div>
        <p>
          O programa YouX Lab tem cerca de 10 meses de duração e é dividido em
          três ciclos de forma que os Labers possam desenvolver habilidades
          socioemocionais, culturais e técnicas por meio de atividades práticas.
          Essa abordagem promove autoconhecimento, inteligência emocional,
          liderança, pensamento crítico e criatividade, além, é claro, de
          capacitar jovens para atuarem nas mais diversas áreas de
          desenvolvimento de soluções digitais, para um futuro promissor,
          gerando impacto positivo em suas vidas e comunidades. Ao final do
          programa, os próprios Labers desenvolvem um produto digital real que
          é, então, doado à sociedade.
        </p>
      </div>

      <h1>Sobre a Conexão Literária</h1>
      <div className="caixa_sobre_conexao">
        <p>
          O Conexão Literária foi lançado como desafio técnico dos Labers no
          YouX Lab em 2024 e, desde então, não parou de evoluir. A partir das
          dificuldades identificadas na gestão dos acervos literários nas
          bibliotecas de escolas públicas, os Labers criaram um sistema para
          facilitar a administração e o controle desses acervos. Em 2025, o
          <b> Conexão Literária ganhou novas funcionalidades </b> para tornar a
          experiência dos alunos ainda mais completa. Agora, cada estudante pode
          acessar seu <b> próprio perfil personalizado </b>, acompanhar seu
          histórico de leitura e explorar recomendações exclusivas. Além disso,
          o sistema incorporou recursos de gamificação, permitindo que os alunos
          participem de desafios literários, conquistem pontos e desbloqueiem
          conquistas, transformando a leitura em uma jornada interativa e
          motivadora. Assim como em sua primeira versão, a evolução do Conexão
          Literária foi construída a partir de jornadas de descoberta:
          entrevistas com educadores e estudantes, identificação das principais
          necessidades e aprimoramentos em usabilidade e acessibilidade. O
          resultado é um produto digital robusto, funcional e pensado para
          ampliar o acesso à leitura e fortalecer o vínculo dos jovens com o
          universo literário.
        </p>
        <p className="p_negrito">
          O Conexão Literária é, e sempre será, GRATUITO para todas as escolas
          públicas.
        </p>
      </div>
      <div className="img_labers">
        <img src={fotoLabers} alt="Foto Labers" />
      </div>
    </div>
  );
}
