import unicodecsv
from datetime import datetime

def ler_csv(caminho):
    with open(caminho, 'rb') as f:
        r = unicodecsv.DictReader(f)
        return list(r)

def parse_date(date):
        if date == '':
                return None
        else:
                return datetime.strptime(date, '%Y-%m-%d')


lido = ler_csv('aula-1/enrollments.csv')

for linha in lido:
        print parse_date(linha['cancel_date'])
