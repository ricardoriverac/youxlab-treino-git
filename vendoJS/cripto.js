const crypto = require('crypto');
const fs = require('fs');

const algoritimo = 'aes-256-cbc'
const key = crypto.randomBytes(32);
const iv = crypto.randomBytes(16);

function criotografar(inputPath, outputPath) {
    const cipher = crypto.createCipheriv(algoritimo, key, iv);
    const input = fs.createReadStream(inputPath);
    const output = fs.createWriteStream(outputPath);

    input.pipe(cipher).pipe(output)

    output.on('finish', () => {
        console.log(`Arquivo criptografado com sucesso`)
        console.log('chave', key.toString('hex'))
        console.log('iv', iv.toString('hex'))
    })
}

criotografar('mensagem.txt', 'mensagem.txt')

