import Group from "../imagem/Group 149.png";
import "./Sobre.css";
import fotoLabers from "../imagem/fotoLabers.svg";

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
          O Conexão Literária foi o projeto desenvolvido como desafio técnico
          dos Labers no YouX Lab em 2024. Diante das dificuldades identificadas
          na gestão dos acervos literários nas bibliotecas de escolas públicas,
          os Labers desenvolveram um sistema com o objetivo de facilitar a
          administração e o controle desses acervos. Para isso, a equipe
          realizou jornadas de descoberta, conduzindo entrevistas com os
          envolvidos e identificando as principais dores e necessidades. Além
          disso, trabalharam aspectos de usabilidade e acessibilidade, evoluindo
          até chegar a um protótipo funcional e navegável, capaz de atender de
          forma eficaz às demandas dos usuários. Com esse protótipo, os Labers
          desenvolveram este produto digital real, aprendendo, na prática, como
          é trabalhar em um projeto de tecnologia e gerando uma contribuição
          positiva a espaços que dedicaram tanto ao crescimento deles - as
          escolas.
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
