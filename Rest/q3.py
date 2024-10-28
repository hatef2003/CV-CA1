from PIL import Image
image = Image.open('Color.JPG')
print("size (resolution)= "+ str(image.size[0])+"*"+str(image.size[1]))
print("heder and bitstream : " +str(image.info))

if image.format_description:
    compression_status = "YES"
    compression_algorithm = image.format_description
else:
    compression_status = "NO"
    compression_algorithm = "N/A"
print("Is it compresed:", compression_status)
print("Compression Algorithm:", compression_algorithm)

