f = open('Uploads\\barron.txt', 'r')
b = open('OUT.txt', 'a')
i = 0

for x in f.readlines():
    data = str(i)+'. '+x.strip('\n')+'.'
    print(data)
    b.write(data+'\n')
    i += 1