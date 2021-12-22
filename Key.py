from Crypto.PublicKey import RSA

kunci_baru = RSA.generate(4096, e=65537)

kunci_private = kunci_baru.exportKey("PEM") #untuk mengeirimkan kunci_private dalam bentuk baru disetiap py dijalankan dalam bentuk PEM

kunci_publik = kunci_baru.publickey().exportKey("PEM") #untuk mengeirimkan kunci_private dalam bentuk baru disetiap py dijalankan dalam bentuk PEM

print(kunci_private) #untuk menghasilkan kunci_private.pem
fd = open("kunci_private.pem", "wb")
fd.write(kunci_private)
fd.close()

print(kunci_publik) #untuk menghasilkan kunci_publik.pem
fd = open("kunci_publik.pem", "wb")
fd.write(kunci_publik)
fd.close()
