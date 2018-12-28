import fun

lido = fun.ler_csv('aula-6/enrollments.csv')
errors = 0
p_sairam = 0
p_n_sairam = 0

for linha in lido:

        # verifica quantas pessoas não sairam do curso
        cancelado = linha['is_canceled']
        if cancelado == 'False':
                p_n_sairam += 1

        # verifica quantas pessoas que sairam do curso
        if cancelado == 'True':
                p_sairam += 1

        # verifica se existe erros em cancelamentos
        data = fun.parse_date(linha['cancel_date'])
        if data is None:
                if cancelado == 'True':
                        errors += 1
        elif cancelado == 'True':
                if data is None:
                        errors += 1


# Colocando resultados no console
print str(lido.__len__()) + ' linhas encontras.'
print str(errors) + ' linhas com erro encontradas.'
print ' '
print str(p_n_sairam) + ' pessoas que estão cursando.'
print str(p_sairam) + ' pessoas que sairam do curso.'

