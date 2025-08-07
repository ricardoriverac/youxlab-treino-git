import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import styles from "./Tabela.module.css";
import Button from "@mui/material/Button";
import VisibilityIcon from "@mui/icons-material/Visibility";
import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import { useState } from "react";
import CloseIcon from "@mui/icons-material/Close";
import Stack from "@mui/material/Stack";
import { styled } from "@mui/material/styles";

function createData(isbn, livro, autor, data, sinopse) {
  return { isbn, livro, autor, data, sinopse };
}

const rows = [
  createData("9788711982457", "O Príncipe Cruel", "Holly Black", "18/01/2018", "Em O Príncipe Cruel, Jude é uma humana criada no mundo das fadas, onde enfrenta desprezo e perigo constante. Determinada a conquistar poder e respeito, ela se envolve em jogos políticos e conspirações. No centro de tudo está o arrogante Príncipe Cardan, seu maior inimigo — e talvez algo mais."),
  createData(
    "9788555343346",
    "A Rainha Vermelha",
    "Victoria Aveyard",
    "12/03/2019",
    "Em A Rainha Vermelha, de Victoria Aveyard, Mare Barrow vive em um mundo dividido pela cor do sangue: vermelhos são comuns, prateados têm poderes e governam. Quando Mare, uma vermelha, descobre que possui uma habilidade especial, é forçada a viver entre os prateados, fingindo ser uma deles. Envolvida em mentiras, rebeliões e conflitos, ela precisa lutar por justiça sem perder quem realmente é."),
  createData("9780062085481", "Estilhaça-me", "Tahereh Mafi", "30/01/2020", "Em Estilhaça-me, de Tahereh Mafi, Juliette tem um toque mortal — qualquer pessoa que ela encoste sente uma dor terrível e pode até morrer. Aprisionada por ser considerada perigosa, ela é usada como arma por um governo autoritário. Mas Juliette começa a descobrir sua força e luta para recuperar sua liberdade, enfrentando escolhas difíceis, paixões intensas e um mundo em colapso."),
  createData("9780007466696", "A Seleção", "Kiera Cass", "25/06/2023", "Em A Seleção, de Kiera Cass, America Singer vive em uma sociedade dividida por castas e é escolhida para participar de uma competição onde 35 garotas disputam o coração do príncipe Maxon. Apesar de não querer a coroa, America entra no palácio por obrigação — e aos poucos, se vê dividida entre um amor do passado e a possibilidade de um futuro inesperado."),
  createData(
    "9781408857878",
    "Corte de Espinhos e Rosas",
    "Sarah J.Mass",
    "17/05/2021",
    "Em Corte de Espinhos e Rosas, de Sarah J. Maas, Feyre, uma jovem caçadora humana, mata um lobo na floresta e, como punição, é levada para o reino feérico por uma criatura misteriosa chamada Tamlin. Lá, ela descobre um mundo mágico repleto de segredos, maldições e perigos. Conforme se envolve com Tamlin, Feyre percebe que seu destino está ligado a uma ameaça muito maior que pode destruir tudo o que ama."),
];

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 400,
  bgcolor: "background.paper",
  border: "2px solid #000",
  boxShadow: 24,
  p: 4,
  height: 500,
};

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: "#fff",
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: "center",
  color: (theme.vars ?? theme).palette.text.secondary,
  ...theme.applyStyles("dark", {
    backgroundColor: "#1A2027",
  }),
}));

export default function BasicTable() {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const [livro, setLivro] = useState({});

  return (
    <TableContainer
      sx={{
        width: "800px",
        boxShadow: "1px 1px 8px 1px #AA60C8",
        margin: "auto",
        marginTop: "30px",
        padding: "10px 30px",
      }}
      component={Paper}
    >
      <tr>
        <th className={styles.tituloTabela}>Livros Disponíveis</th>
      </tr>
      <Table
        sx={{
          minWidth: 650,
          size: "small",
          width: "800px",
          justifyContent: "center",
          margin: "auto",
        }}
        aria-label="simple table"
      >
        <TableHead>
          <TableRow>
            <TableCell sx={{ fontWeight: "bold" }}>ISBN</TableCell>
            <TableCell sx={{ fontWeight: "bold" }}>Nome do Livro</TableCell>
            <TableCell sx={{ fontWeight: "bold" }}>Nome do Autor</TableCell>
            <TableCell sx={{ fontWeight: "bold" }}>Data de Cadastro</TableCell>
            <TableCell sx={{ fontWeight: "bold" }}>Ações</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.isbn}
              </TableCell>
              <TableCell>{row.livro}</TableCell>
              <TableCell>{row.autor}</TableCell>
              <TableCell>{row.data}</TableCell>
              <TableCell>
                <Button
                  onClick={() => {
                    setLivro(row);
                    handleOpen();
                  }}
                  variant="contained"
                  sx={{
                    bgcolor: "#AA60C8",
                    fontSize: "small",
                    "&:hover": {
                      transform: "scale(1.05)",
                      bgcolor: "#a24dc4",
                    },
                  }}
                >
                  <VisibilityIcon />
                  Visualizar
                </Button>
                <Modal
                  open={open}
                  onClose={handleClose}
                  aria-labelledby="modal-modal-title"
                  aria-describedby="modal-modal-description"
                >
                  <Box sx={style}>
                    <button onClick={handleClose} className={styles.close}>
                      <CloseIcon />
                    </button>
                    <Typography
                      sx={{
                        fontWeight: "bold",
                        bgcolor: "#AA60C8",
                        color: "white",
                      }}
                      id="modal-modal-title"
                      variant="h6"
                      component="h2"
                    >
                      Informações do Livro
                    </Typography>

                    <div className={styles.divInfo}>
                      <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                        <p className={styles.info}>ISBN</p>
                        <Stack
                          sx={{ marginTop: "30px" }}
                          direction="row"
                          spacing={2}
                        >
                          <Item
                            sx={{
                              padding: "10px",
                              border: "2px solid #D69ADE",
                              width: "150px",
                            }}
                          >
                            {livro?.isbn}
                          </Item>
                        </Stack>
                      </Typography>

                      <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                        <p className={styles.info}>Nome do Livro</p>
                        <Stack
                          sx={{ marginTop: "30px" }}
                          direction="row"
                          spacing={2}
                        >
                          <Item
                            sx={{
                              padding: "10px",
                              border: "2px solid #D69ADE",
                              width: "150px",
                            }}
                          >
                            {livro?.livro}
                          </Item>
                        </Stack>
                      </Typography>
                    </div>

                     <div className={styles.divInfoDois}>
                      <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                        <p className={styles.info}>Nome do Autor</p>
                        <Stack
                          sx={{ marginTop: "30px" }}
                          direction="row"
                          spacing={2}
                        >
                          <Item
                            sx={{
                              padding: "10px",
                              border: "2px solid #D69ADE",
                              width: "150px",
                            }}
                          >
                            {livro?.autor}
                          </Item>
                        </Stack>
                      </Typography>

                      <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                        <p className={styles.info}>Data de Cadastro</p>
                        <Stack
                          sx={{ marginTop: "30px" }}
                          direction="row"
                          spacing={2}
                        >
                          <Item
                            sx={{
                              padding: "10px",
                              border: "2px solid #D69ADE",
                              width: "150px",
                            }}
                          >
                            {livro?.data}
                          </Item>
                        </Stack>
                      </Typography>
                    </div>

                     <div className={styles.divInfoSinopse}>
                      <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                        <p className={styles.info}>Sinopse</p>
                        <Stack
                          sx={{ marginTop: "30px" }}
                          direction="row"
                          spacing={2}
                        >
                          <Item
                            sx={{
                              padding: "10px",
                              border: "2px solid #D69ADE",
                              width: "400px",
                              height: "auto",
                            }}
                          >
                            {livro?.sinopse}
                          </Item>
                        </Stack>
                      </Typography>
                    </div>

                    {/* <Typography id="modal-modal-description" sx={{ mt: 2}}>
                      <p className={styles.info}>Nome do Autor</p>
                      <Stack  sx={{marginTop: '30px'}}direction="row" spacing={2}>
                        <Item sx={{padding: '10px', border: '2px solid #D69ADE'}}>{livro.autor}</Item>
                      </Stack>
                    </Typography> */}
                  </Box>
                </Modal>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

// export default function Tabela() {
//   const [ISBN, setISBN] = useState("");
//   const [nomeLivro, setNomeLivro] = useState("");
//   const [nomeAutor, setNomeAutor] = useState("");
//   const [data, setData] = useState("");

//   return (
//     <div className={styles.div}>
//       <table className={styles.tabela}>
//         <tr>
//           <th className={styles.tituloTabela}>Livros Disponíveis</th>
//         </tr>

//         <tr className={styles.tr}>
//           <th className={styles.th}>ISBN</th>
//           <th className={styles.th}>Nome do Livro</th>
//           <th className={styles.th}>Nome do Autor</th>
//           <th className={styles.th}>Data de Cadastro</th>
//           <th className={styles.th}>Ações</th>
//         </tr>

//         <tr className={styles.livros}>
//           <td>9788711982457</td>
//           <td>O Príncipe Cruel</td>
//           <td>Holly Black</td>
//           <td>02/01/2018</td>
//           <td>
//             <Button
//               variant="contained"
//               sx={{
//                 width: "150px",
//                 margin: "25px",
//                 bgcolor: "#AA60C8",
//                 fontSize: "small",
//                 "&:hover": {
//                  transform: 'scale(1.05)',
//                  bgcolor: '#a24dc4'
//                 },
//               }}>
//               <VisibilityIcon />
//               Visualizar
//             </Button>

//           </td>
//         </tr>
//       </table>
//     </div>
