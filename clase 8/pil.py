from PIL import Image
im = Image.open("gato.jpeg")

# im.show()
# print(im.size, im.format, im.mode)

# im.rotate(45, fillcolor="red", expand=True).show()

im.resize((100, 100)).show()

input("Presione nombre:")