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


lido = ler_csv('aula-5/enrollments.csv')
errors = 0

for linha in lido:
        data = parse_date(linha['cancel_date'])
        cancelado = linha['is_canceled']

        if data is None:
                if cancelado == 'True':
                        errors += 1
        elif cancelado == 'True':
                if data is None:
                        errors += 1

print 'Numero de erros achado onde existe data de cancelamento mas nao esta cancelado realmente ou alcontrario: ' + str(errors)

