import re
import pandas as pd
import numpy as np

def Algo(chat):
    chat = open(chat, encoding='utf-8').read()
    df = pd.DataFrame()
    data = re.findall(r'(.+?), (.+?) - (.+?): (.+?)\n', chat+'\n')

    req = ['? ', ' ?', '?\n']

    for j in range(len(data)):
        data[j] = list(data[j])
        if (req[0] not in data[j][3]) and (req[1] not in data[j][3]) and (req[2] not in data[j][3]):
            data[j][3] = 'NaN'

    tanggal = []; nama=[]; pesan=[]
    for i in data:
        tanggal.append(i[0]); nama.append(i[2]); pesan.append(i[3])

    df['date'] = tanggal
    df['name'] = nama
    df['message'] = pesan
    return df