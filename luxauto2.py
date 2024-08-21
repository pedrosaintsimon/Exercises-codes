from PIL import Image

# Nomes das imagens (substitua pelos seus nomes reais)
input_filename = "minha_imagem.heic"
output_filename = "minha_imagem.jpg"

try:
    # Abre a imagem HEIC
    with Image.open(input_filename) as img:
        # Converte e salva como JPG
        img.save(output_filename, "JPEG")

    print(f"Conversão concluída com sucesso! A imagem '{input_filename}' foi convertida para '{output_filename}'.")
except Exception as e:
    print(f"Erro durante a conversão: {e}")
