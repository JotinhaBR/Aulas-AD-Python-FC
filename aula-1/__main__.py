import unicodecsv

enrollments = []
f = open('aula-1/enrollments.csv', 'rb')
reader = unicodecsv.DictReader(f)

for row in reader:
    enrollments.append(row)
    print(row)

f.close()