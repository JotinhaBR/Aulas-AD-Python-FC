import unicodecsv

def ler_csv(caminho):
    with open(caminho, 'rb') as f:
        r = unicodecsv.DictReader(f)
        return list(r)



lido = ler_csv('aula-1/enrollments.csv')

print(lido[0])
