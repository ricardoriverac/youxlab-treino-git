import os
import requests
import subprocess

def download_discord_installer():
    url = "https://discord.com/api/download?platform=linux&format=deb"
    temp_file = "/tmp/discord.deb"
    
    print("Baixando o instalador do Discord...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(temp_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print("Download concluído.")
        return temp_file
    else:
        print("Erro ao baixar o arquivo.")
        return None

def install_discord(deb_file):
    if deb_file and os.path.exists(deb_file):
        print("Instalando o Discord...")
        subprocess.run(["sudo", "dpkg", "-i", deb_file], check=True)
        print("Instalação concluída.")
        os.remove(deb_file)
    else:
        print("Arquivo .deb não encontrado.")

def main():
    deb_file = download_discord_installer()
    install_discord(deb_file)

if __name__ == "__main__":
    main()