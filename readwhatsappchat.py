import re

kontak = ''
file = open('D:\Doc\chat.txt', encoding='utf-8')
chat = file.read()
list = []

variation = ['? ', ' ?']

ad = re.findall(r'- Praditya Irgy:(.+?)\n', chat + '\n')
ktk = re.findall(r'- #kontak#:(.+?)\n', chat + '\n')

def run(subjek):
    for i in range(0,len(variation)):
        member = str(subjek).count(variation[i])
        list.append(int(member))

run(ad)
run(ktk)
print(f'{sum(list)}')