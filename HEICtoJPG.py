from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()


img = Image.open('C:\\Users\\pedro.ivo\\Desktop\\6292\\IMG_1376.HEIC')
img.save('C:\\Users\\pedro.ivo\\Desktop\\6292\\IMG_1376.JPG', format='JPEG')

print(f"A imagem HEIC '{Image.open}' foi convertida para JPG '{img.save}' com sucesso. Qualidade: Alta.")
