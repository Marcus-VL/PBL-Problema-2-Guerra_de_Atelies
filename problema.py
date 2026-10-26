import os

def limpar():
	os.system('cls')
lista = []

while True:
	modobot = input("Selecione o modo do BOT [Normal - Veterano]: ")
	modobot = modobot.lower()

	if modobot in ("normal", "veterano"):
		break
	else:
		print("Entrada incorreta.")

try:
	grade = int(input("Tamanho da grade: "))
except:
	print("Entrada Inválida.")

nelmos = 2*(int((grade - 1) / 4)) # 2 ELMOS A CADA 4 UNIDADES APÓS 1
narmadura = int(grade/5) # 1 ARMADURA A CADA 5 UNIDADES
ncapas = int(grade/3) # 1 CAPA A CADA 3 UNIDADES
nasas = int(grade/8) # 1 PAR DE ASAS A CADA 8 UNIDADES

for i in range(grade):
	lista.append(["n"]*grade)

preenchidos = []


def verifpreenchimento(numcasas, sentido):
	japreenchido = False
	if numcasas < 4:
		for i in range(numcasas):
			if sentido == 1:
				if lista[linha-1+i][coluna-1] in ("@", "#", "$", "%"):
					japreenchido = True
			elif sentido == 2:
				
				if lista[linha-1][coluna-1+i] in ("@", "#", "$", "%"):
					japreenchido = True
	else:
		for i in range(4):
			if i-2 < 0:
				if lista[linha-1+i][coluna-1] in ("@", "#", "$", "%"):
					japreenchido = True
			else:
				if lista[linha-1+i-2][coluna] in ("@", "#", "$", "%"):
					japreenchido = True

	return japreenchido

def preencher(linha, coluna, elemento, sentido, numcasas):
	global lista
	global nelmos, narmadura, ncapas, nasas
	japreenchido = False
	elemento_preenchido = linha + coluna/10


	if ((sentido == 1 and linha+numcasas-1 > grade) or (sentido == 2 and coluna+numcasas-1 > grade)) or (linha == 0 or coluna == 0):
		#SE O ULTIMO ELEMENTO FOR MAIOR OU MENOR QUE AS BORDAS, NÃO EXECUTE
		print("POSIÇÃO INVÁLIDA! LIMITE DA BANCADA ATINGIDO OU ULTRAPASSADO")
	else:
		#SE O ULTIMO ELEMENTO NÃO FOR MAIOR OU MENOR QUE AS BORDAS, EXECUTE
		match elemento:
			#ELMO
			case "@":
				japreenchido = verifpreenchimento(numcasas, sentido)
				if japreenchido == False:
					lista[linha-1][coluna-1] = elemento
					elemento_preenchido*=10
					nelmos -= 1
					print(elemento_preenchido)

			#CAPA
			case "#":
				if sentido in (1, 2):
					elemento_preenchido = linha + coluna/10
					if sentido == 1:

						japreenchido = verifpreenchimento(numcasas, sentido)
						if japreenchido == False:
							lista[linha-1][coluna-1] = elemento
							lista[linha][coluna-1] = elemento
							elemento_preenchido += (linha+1)/100 + (coluna)/1000
							ncapas -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elif sentido == 2:

						japreenchido = verifpreenchimento(numcasas, sentido)

						if japreenchido == False:
							lista[linha-1][coluna-1] = elemento
							lista[linha-1][coluna] = elemento
							elemento_preenchido += (linha)/100 + (coluna+1)/1000
							ncapas -= 1
						else:
							print("O espaço selecionado já está ocupado")

					elemento_preenchido *= 1000
					print(elemento_preenchido)
						
				else:
					print("Entrada de sentido inválida")

			#ARMADURA
			case "$":
				if sentido in (1, 2):
					elemento_preenchido = linha + (coluna/10)
					if sentido == 1:
						japreenchido = verifpreenchimento(numcasas, sentido)

						if japreenchido == False:
							lista[linha-1][coluna-1] = elemento
							lista[linha][coluna-1] = elemento
							lista[linha+1][coluna-1] = elemento
							elemento_preenchido += (linha+1)/100 + (coluna)/1000 + (linha+2)/10000 + (coluna)/100000
							narmadura -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elif sentido ==2:
						japreenchido = verifpreenchimento(numcasas, sentido)

						if japreenchido == False:
							lista[linha-1][coluna-1] = elemento
							lista[linha-1][coluna] = elemento
							lista[linha-1][coluna+1] = elemento
							elemento_preenchido += (linha/100) + (coluna+1)/1000 + (linha/10000)+(coluna+2)/100000
							narmadura -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elemento_preenchido *= 100000
					print(elemento_preenchido)
				else:
					print("Entrada de sentido inválida")

			#PAR DE ASAS
			case "%":
				if sentido in (1, 2):
					elemento_preenchido = linha + (coluna/10)
					if sentido == 1:
						japreenchido = verifpreenchimento(numcasas, sentido)

						if japreenchido == False:
							lista[linha-1][coluna-1] = elemento
							lista[linha][coluna-1] = elemento
							lista[linha+1][coluna-1] = elemento
							lista[linha+2][coluna-1] = elemento
							elemento_preenchido += (linha+1)/100 + (coluna)/1000 + (linha+2)/10000 + (coluna)/100000 + (linha+3)/1000000 + (coluna)/10000000
							nasas -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elif sentido ==2:
						japreenchido = verifpreenchimento(numcasas, sentido)

						if japreenchido == False:
							lista[linha-1][coluna-1] = elemento
							lista[linha-1][coluna] = elemento
							lista[linha-1][coluna+1] = elemento
							lista[linha-1][coluna+2] = elemento
							elemento_preenchido += (linha/100) + (coluna+1)/1000 + (linha/10000)+(coluna+2)/100000 + (linha/1000000)+(coluna+3)/10000000
							nasas -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elemento_preenchido *= 10000000
					print(elemento_preenchido)
				else:
					print("Entrada de sentido inválida")

		if japreenchido == False:
			if elemento in ("@", "#", "$", "%"):
				preenchidos.append(elemento_preenchido)
				print(preenchidos)
			else:
				print("Elemento Inválido")
		
limpar()


print("|GINCANA DOS ATELIÊS - JOGO CONTRA TOTEM\n")
print(f"Elmos: {nelmos}; Armaduras: {narmadura}; Capas: {ncapas}; Asas: {nasas}")

montagembancada = True
while montagembancada:
	sentido=1


	while True:
		try:
			linha= int(input("Número da linha que deseja preencher: "))
			break
		except:
			print("Entrada Inválida.")

	while True:
		try:
			coluna= int(input("Número da coluna que deseja preencher: "))
			break
		except:
			print("Entrada Inválida.")
	
	valido = False
	while valido == False:
		elemento=input("Digite o simbolo do elemento: ")

		qtelemento_validez = True #BOOLEANO QUE CONFERE SE AINDA TEM UMA QUANTIDADE DE ELEMENTOS MAIOR QUE ZERO
		if elemento not in("@", "#", "$", "%", "encerrar"):
			print("Entrada Inválida.")
		else:
			match elemento:
				case "@":
					if nelmos == 0:
						qtelemento_validez = False
					numcasas = 1
				case "#":
					if ncapas == 0:
						qtelemento_validez = False
					numcasas = 2
				case "$":
					if narmadura == 0:
						qtelemento_validez = False
					numcasas = 3
				case "%":
					if nasas == 0:
						qtelemento_validez = False
					numcasas = 4
			valido = True

	if elemento == "encerrar":
		print("Programa Encerrado")
		break

	if qtelemento_validez == True:
		if elemento not in ("@", "encerrar"):
			sentido=int(input("Defina o sentido(Vertical [1] Horizontal[2]):"))
			

		preencher(linha,coluna,elemento,sentido, numcasas)
	else:
		print("Sem exemplares disponíveis para posicionar essa peça.")

	#limpar()
	
	print("|GINCANA DOS ATELIÊS - JOGO CONTRA TOTEM\n")
	print(f"Elmos: {nelmos}; Armaduras: {narmadura}; Capas: {ncapas}; Asas: {nasas}")

	print("  ", end="")
	for i in range(1, grade+1):
		print("  ", i, end="")
	print()

	for i in range(grade):
		x = lista[i]
		if i < 9:
			print(i+1, " |", end="")
		else:
			print(i+1, "|", end="")

		for j in range(grade):
			if x[j] == "n":
				print("   ", end=" ")
			else:
				print(f" {x[j]} ", end=" ")
		print("|")

	print()

	if (nelmos+ncapas+narmadura+nasas) == 0:
		montagembancada = False

#BOT FORMANDO
pecas = (nelmos+ncapas+narmadura+nasas)
while pecas > 0:
	pass

#Fase de Ataques
print("|FASE DE CANTADAS DE POSIÇÕES|")
ataquesbancadas = True
while ataquesbancadas:
	#RODADA DO PLAYER

	#RODADA DO BOT

	#EXIBIÇÃO DAS BANCADAS