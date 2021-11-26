import qrcode
img = qrcode.make('https://www.bigqueries.com/')
type(img)  # qrcode.image.pil.PilImage
img.save("simple.png")