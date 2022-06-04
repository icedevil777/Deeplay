fp = open('log.txt')
ip = '10.1.192.38'

for i in fp:
    if ip in i:
        print(i.split('sid=/')[1].split('/&type')[0])
