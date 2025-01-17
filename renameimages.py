import os

# Pasta onde as imagens estão localizadas
imgFold = input("Diretório:").replace('\\', '/')

# Palavra que você deseja remover dos nomes das imagens
wordToRemove = input("Palavra a ser removida:")

# Listar todos os arquivos na pasta das imagens
files = os.listdir(imgFold)

# Iterar sobre os arquivos
for file in files:
    # Verificar se o arquivo é uma imagem
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        # Obter o novo nome do arquivo removendo a palavra
        newName = file.replace(wordToRemove, "")
        
        # Caminho completo do arquivo original e do novo arquivo
        ogPath = os.path.join(imgFold, file)
        newPath = os.path.join(imgFold, newName)
        
        # Renomear o arquivo
        os.rename(ogPath, newPath)
        
        print(f"Renomeado: {file} -> {newName}")

        
