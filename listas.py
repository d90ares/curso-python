import time

# print(("Bem vindo(a) a calculadora de IMC"))
# print("Para começar digite sua altura: ")
# altura = float(input())
# print("Digite seu peso: ")
# peso = float(input())

# print("Calculando...")
# print("==============")
# time.sleep(1)
# print("Seu IMC é {:.2f}".format(peso / altura**2))

# nome_completo = input("Qual o seu nome Completo? \n")

# primeiro_nome = nome_completo.split()
# print("Olá {}".format(primeiro_nome[0]))

# print("Olá, digite o seu e-mail")
# email_completo = str(input())
# dominio = email_completo.split("@")
# print("Estamos extraindo o seu domínio")
# print("==============================")
# time.sleep(1)
# print("O seu domínio é:")
# print("{}".format(dominio[1]))

# print("Bem vindo(a) a loja de tintas online!")
# print("Para começar informe a área em m² que deseja pintar (não é necessário acrescentar o ²): ")
# m_quadrados = float(input())
# volume_necessario = m_quadrados / 3
# latas = int(volume_necessario / 18)
# custo = latas * 80

# if latas < 1:
#     latas = 1
#     custo = latas * 80
#     print("Você precisará de {} lata e ela custará R$ {}".format(latas, custo))
# else:
#     print("Você precisará de {} latas e elas custarão R$ {}".format(latas, custo))

print("Olá, seja bem vindo a calculadora de holerite online")
print("Para começar, digite o seu salário por hora:")
valor_hora = float(input())

print("Digite quantas horas trabalhou no mês:")
horas_trabalhadas = int(input())
print("Calculando...")
print("==============================")

salario_bruto = valor_hora * horas_trabalhadas
irpf = salario_bruto * 0.11
pg_inss = (salario_bruto - irpf) * 0.08
sindicato = (salario_bruto - irpf - pg_inss) * 0.05
salario_liquido = salario_bruto - pg_inss - irpf - sindicato
print("salário bruto: {:.2f}".format(salario_bruto, 2))
print("INSS: {:.2f}".format(pg_inss, 2))
print("Sindicato: {:.2f}".format(sindicato, 2))
print("Salário líquido: {:.2f}".format(salario_liquido, 2))
