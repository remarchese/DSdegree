# Exemplo de rodar um programa em .py

# aprovado -> média tem que ser maior ou igual a 6 E a frequencia tem que ser maior ou igual a 0.75

media = float(input('Digite a média do aluno :'))
freq = float(input('Digite a frequencia do aluno :'))

print('Media:', media, '\nFrequencia:', freq)

aprovado = media >= 6.0 and freq >= 0.75

print('Aluno aprovado:', aprovado)

print('Aluno aprovado: {}'.format(aprovado))

print(f'Aluno aprovado: {aprovado}')
