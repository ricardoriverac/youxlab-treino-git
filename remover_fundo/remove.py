from rembg import remove
from PIL import Image
import io

def remover_fundo(input_path, output_path):
    """
    Remove o fundo de uma imagem e salva o resultado.
    
    Parâmetros:
        input_path (str): Caminho da imagem de entrada
        output_path (str): Caminho para salvar a imagem sem fundo
    """
    try:
        # Abrir a imagem
        with open(input_path, "rb") as input_file:
            input_image = input_file.read()
        
        # Remover o fundo
        output_image = remove(input_image)
        
        # Salvar a imagem resultante
        with open(output_path, "wb") as output_file:
            output_file.write(output_image)
            
        print(f"Fundo removido com sucesso! Imagem salva em: {output_path}")
        
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Exemplo de uso
if __name__ == "__main__":
    imagem_entrada = "input.jpg"
    imagem_saida = "output.png"
    
    remover_fundo(imagem_entrada, imagem_saida)
