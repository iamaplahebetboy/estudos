#Inserção de peso
peso = float(input("Informe seu peso em quilogramas: "))
altura = float(input("Informe sua altura em metros: "))

#Calculo de IMC
imc = peso / (altura ** 2)


print(f"Seu IMC é: {imc:.2f}")

#Maior que e menor que do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 24.9:
    print("Seu peso está na faixa saudável.")
elif imc >= 25 and imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")

