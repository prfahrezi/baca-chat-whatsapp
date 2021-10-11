import matplotlib.pyplot as pl
import random

x = []
y = []

for i in range(13,25):
    tgl = f'({i} Mar)'
    x.append(tgl)

for i in range(0, len(x)):
    rdm = random.choice(range(50,100))
    y.append(rdm)

pl.plot(x, y)
pl.xlabel('Tanggal pesan dikirim (Maret 2021)')
pl.ylabel('JUmlah pertanyaan diajukan')
pl.title('Whatsapp Chat')

pl.show()