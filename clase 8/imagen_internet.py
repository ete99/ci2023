import requests as rq

url = "https://ca-times.brightspotcdn.com/dims4/default/c3f4b96/2147483647/strip/true/crop/1970x1108+39+0/resize/1200x675!/quality/80/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F12%2Fa5%2F79e097ccf62312d18a025f22ce48%2Fhoyla-recuento-11-cosas-aman-gatos-top-001"

respuesta = rq.get(url)
print(respuesta.status_code)


with open("nuevo_gato.jpeg", "wb") as f:
    f.write(respuesta.content)

