import {Container, Box, TextField} from "@mui/material"
import './TelaEntrar.module.css'
import Titulo from "./Titulo"
import Button from '@mui/material/Button';
import Divider from '@mui/material/Divider';
import Chip from '@mui/material/Chip';
import LoginIcon from '@mui/icons-material/Login';
import PersonAddIcon from '@mui/icons-material/PersonAdd';
import { useNavigate } from "react-router-dom";
import Condicoes from "./Condicoes";
import { useState } from "react";

function TelaEntrar(){
    const navigate = useNavigate()

    function RotaFazerLogin(){
        return navigate('/')
    }

    const [nome, setNome] = useState("")
    const [email, setEmail] = useState("")
    const [senha, setSenha] = useState("")
    const [senhaConfirmada, setSenhaConfirmada] = useState("")

    function conta(){
        if(!email.includes("@") || !email.includes(".com")){
            alert("O email deve conter @ e .com")
            return
        }

        if(senha.length < 6){
            alert("A senha deve conter no mínimo 6 caracteres")
            return
        }

        if(senha !== senhaConfirmada){
            alert("A senha confirmada não está correta")
            return
        }

        fetch(`http://localhost:3000/usuarios?email=${email}`).then((resp) => resp.json()).then((data)=>{
            if(data.length > 0){
                alert("Email já está cadastrado")
                return
            }else{
                navigate('/bibliotecavirtual',{
                    state:{
                        nome: nome
                    }
                })
            }
        })


        fetch("http://localhost:3000/usuarios", {
            method: "POST", // Envia dados para esse servidor
            headers: { "Content-type": "application/json" }, // Fala pro servidor que o conteúdo que está sendo enviado está no formado json
            body: JSON.stringify({ // Pega os dados e transforma eles um em texto json
                nome: nome,
                senha: senha,
                email: email
            })
        })
        .then((resp) => resp.json()) // "then": quando o pedido chegar no servidor transforma a resposta do servidor em um objeto JavaScript
        .then((data) => { // data é a resposta do servidor
            console.log("Usuário: ", data)
            setNome("")
            setEmail("")
            setSenha("")
            setSenhaConfirmada("")
        })
        .catch((err) => {
            console.error("Erro", err)
        })
    }

    return(
        <Container maxWidth="sm" sx={{
            justifyContent: 'center', 
            display: 'flex', 
            alignItems: 'center', 
            margin: 'auto', 
            marginTop: '50px'
            }}>

            <Box component="section" sx={{
                height: '90vh',
                boxShadow: '1px 1px 8px 1px #AA60C8',
                display: 'flex',
                flexDirection: 'column',
                marginTop: '-25px',
                bgcolor: '#fff'
            }} >
                <Titulo titulo="Criar Conta" label="Preencha os dados para criar sua conta"/>

                <TextField onChange={(e) => setNome(e.target.value)} id="nome-basic" label="Nome Completo *" variant="outlined" sx={{
                    width: '500px',
                    justifyContent: 'center',
                    margin: 'auto',
                    marginTop: '10px'
                    }}
                />

                <TextField onChange={(e) => setEmail(e.target.value)} id="nome-basic" label="Email *" variant="outlined" sx={{
                    width: '500px',
                    justifyContent: 'center',
                    margin: 'auto',
                    marginTop: '10px'
                    }}
                />
                <Condicoes
                    label="Deve conter @ e terminar com .com"
                />

                <TextField  onChange={(e) => setSenha(e.target.value)} id="senha-basic" label="Senha *" variant="outlined" type="password" sx={{
                    width: '500px',
                    justifyContent: 'center',
                    margin: 'auto',
                    marginTop: '10px'
                    }}
                />
                 <Condicoes
                    label="Mínimo 6 caracteres"
                />

                <TextField onChange={(e) => setSenhaConfirmada(e.target.value)} id="senha-basic" label="Confirmar Senha *" variant="outlined" type="password" sx={{
                    width: '500px',
                    justifyContent: 'center',
                    margin: 'auto',
                    marginTop: '10px'
                    }}
                />
                
                <Button onClick={conta} variant="contained" sx={{
                    width: '500px', 
                    margin: '25px', 
                    bgcolor: "#AA60C8",
                    }}>
                        <PersonAddIcon/>
                        Criar Conta
                    </Button>

                <Divider>
                    <Chip label="Ou" size="small" />
                </Divider>

                <Button variant="outlined" onClick={RotaFazerLogin} sx={{
                    width: '500px',
                    margin: '25px',
                    color: '#AA60C8',
                    border: '1px solid #AA60C8'
                    }}>
                        <LoginIcon/>
                        Fazer Login
                    </Button>
            </Box>
        </Container>
    )
    
}

export default TelaEntrar
