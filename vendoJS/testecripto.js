
const crypto = require('crypto');
const fs = require('fs');

const algoritimo = 'aes-256-cbc'
const chave = crypto.randomBytes(32);
const vetor = crypto.randomBytes(16);

function criptografar(inputPath, outputPath){
    const cifra = crypto.createCipheriv(algoritimo, chave, vetor);
    const output = fs.createWriteStream(outputPath);
    const input = fs.createReadStream(inputPath);

    input.pipe(cifra).pipe(output)

    output.on('finish', () =>{
        console.log('arquivo criptografado com sucesso')
        console.log('chave: ', chave.toString('hex'))
        console.log('vetor: ', vetor.toString('hex'))
    })
}

criptografar('teste_msg.txt', 'teste_msg.txt')