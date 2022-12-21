import sys

def contador():
    fich = open('contador.txt','r')
    fich.seek(0)
    contenido = fich.read()

    if len(contenido)==0:
        contenido='0'
        fich.write(contenido)
        fich.close()
    try:
        contenido = int(contenido)
        if len(sys.argv)==2:
            if sys.argv[1]=='inc':
                contador+=1
            elif sys.argv[1]=='dec':
                contador-=1
            fich.write(str(contenido))
    except ValueError:
        return 'Error: Fichero corrupto'
    fich.close()
    return contenido