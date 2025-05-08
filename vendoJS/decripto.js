// código para descriptografar o arquivo 

import crypto from 'crypto'
import fs from 'fs'

const algoritimo = 'aes-256-cbc'
const key = randomBytes(32);
const iv = randomBytes(16);

function decripto(inputPath, outputPath) {
    const decipher = crypto.createCipheriv(algoritimo, key, iv);
    const input = fs.createReadStream(inputPath);
    const output = fs.creatWriteStream(outputPath);

    input.pipe(decipher).pipe(output)
    output.on('finish', () => {
        console.log('Arquivo descriptografado');
        console.log('chave:' key.toString('hex'));
        console.log('iv: ' iv.toString('hex'));
        
    });
}