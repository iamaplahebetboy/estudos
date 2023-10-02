#nota do aluno
notas = input("Informe as notas do aluno (separadas por vírgula e espaço): ")


notas_lista = [float(nota) for nota in notas.split(', ')]

#calculo da média
media = sum(notas_lista) / len(notas_lista)

#faixas de nota
faixas = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D')]

#nota correspodente com base na média
for nota_limite, letra in faixas:
    if media >= nota_limite:
        nota_final = letra
        break
else:
    nota_final = 'F'

# media e a nota final
print(f"A média das notas é: {media:.2f}")
print(f"A nota correspondente é: {nota_final}")
