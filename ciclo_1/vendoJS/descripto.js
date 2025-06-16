const crypto = require('crypto');
const fs = require('fs');

const algoritimo = 'aes-256-cbc'
const chave = '3212368a07038dcec5c5a2c53d4448d6c6d08e1919cdb74ce74b6de4770f0b5f';
const vetor = 'd44be703cdd350b8ef3033842480d039';


function decriptografar(inputPath, outputPath){
    const decripto = crypto.createDecipheriv(algoritimo, chave, vetor)
    const input = fs.createReadStream(inputPath);
    const output = fs.createWriteStream(outputPath);

    input.pipe(decripto).pipe(output)
    
    output.on('finish', () =>{
        console.log('Arquivo descriptografado com sucesso')
    })

}

decriptografar('teste_msg', 'teste_msg_decriptado')