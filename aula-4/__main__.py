import unicodecsv
from datetime import datetime

def ler_csv(caminho):
    with open(caminho, 'rb') as f:
        r = unicodecsv.DictReader(f)
        return list(r)


lido = ler_csv('aula-1/enrollments.csv')

unique_enrolled_students = set()
for enrollment in lido:
    unique_enrolled_students.add(enrollment['account_key'])


print(unique_enrolled_students)