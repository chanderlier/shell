import base64

with open('picturename.jpg', 'rb') as f:
    f = base64.b64encode(f.read())

print(f)
