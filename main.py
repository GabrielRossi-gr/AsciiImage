


#import pywhatkit as KT

#KT.image_to_ascii_art("C:/Users/gabri/Downloads/IMG_20221031_183903_824 (2).jpg","C:/Users/gabri/Downloads/IMG_20221031_183903_824 (2).txt")


from PIL import Image # type: ignore

#palmeiras
imagem = Image.open("/Users/gabrielrossi/Downloads/kkk1.png")




#medio: 
largura, altura = 80 , 50 

#largo: largura, altura = 480 , 300
#pequeno:largura, altura = 200 , 100 

imagem = imagem.resize((largura, altura))
imagem = imagem.convert("L")

caracteres_ascii = [" ", ".", "-", "*", ":", "=", "+", "#", "%", "@"]
# caracteres_ascii = ["°", "/", "*", ";", "=", "+", "#", "%", "@"]         ##    !@#$%¨&*(_+=´

pixels = imagem.load()
ascii_image = ""

for y in range(altura):
    for x in range(largura):
        pixel = pixels[x, y]
        ascii_char = caracteres_ascii[int((pixel/255)*(len(caracteres_ascii)-1))]
        ascii_image += ascii_char
    ascii_image += "\n"

print(ascii_image)
