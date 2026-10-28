# Declaração de autoria
# Nome: Marcus Vinícius Leite dos Santos
# Declaro que este código foi desenvolvido por mim, com base no meu próprio
# entendimento e esforço. Não houve plágio ou cópia integral de terceiros.
# Ferramentas de IA, quando utilizadas, foram apenas como apoio ao aprendizado
# e não para a geração integral deste código.

import os, random

def limpar():
	os.system('cls')
bancadaplayer = []
bancadabot = []

def exibirbancada(bancada):
	print("  ", end="")
	for i in range(1, grade+1):
		print("  ", i, end="")
	print()

	for i in range(grade):
		x = bancada[i]
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


def verifpreenchimento(numcasas, sentido, matriz):
	japreenchido = False
	if ((sentido == 1 and linha+numcasas-1 > grade) or (sentido == 2 and coluna+numcasas-1 > grade)) or (linha == 0 or coluna == 0):
		pass
	else:
		for i in range(numcasas):
			if sentido == 1:
				if matriz[linha-1+i][coluna-1] in ("@", "#", "$", "%"):
					japreenchido = True
			elif sentido == 2:
				if matriz[linha-1][coluna-1+i] in ("@", "#", "$", "%"):
					japreenchido = True
				

	return japreenchido

def preencher(linha, coluna, elemento, sentido, numcasas, matriz, listapreenchidos, jogador="player"):
	global nelmos, narmadura, ncapas, nasas, limite
	japreenchido = False
	elemento_preenchido = linha + coluna/10

	limite = False
	if (((sentido == 1 and linha+numcasas-1 > grade) or (sentido == 2 and coluna+numcasas-1 > grade)) or (linha == 0 or coluna == 0)):
		#SE O ULTIMO ELEMENTO FOR MAIOR OU MENOR QUE AS BORDAS, NÃO EXECUTE
		limite = True
		if jogador == "player":
			print("POSIÇÃO INVÁLIDA! LIMITE DA BANCADA ATINGIDO OU ULTRAPASSADO")
	else:
		#SE O ULTIMO ELEMENTO NÃO FOR MAIOR OU MENOR QUE AS BORDAS, EXECUTE
		match elemento:
			#ELMO
			case "@":
				japreenchido = verifpreenchimento(numcasas, sentido, matriz)
				if japreenchido == False:
					matriz[linha-1][coluna-1] = elemento
					elemento_preenchido*=10
					nelmos -= 1

			#CAPA
			case "#":
				if sentido in (1, 2):
					elemento_preenchido = linha + coluna/10
					if sentido == 1:

						japreenchido = verifpreenchimento(numcasas, sentido, matriz)
						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha][coluna-1] = elemento
							elemento_preenchido += (linha+1)/100 + (coluna)/1000
							ncapas -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elif sentido == 2:

						japreenchido = verifpreenchimento(numcasas, sentido, matriz)

						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha-1][coluna] = elemento
							elemento_preenchido += (linha)/100 + (coluna+1)/1000
							ncapas -= 1
						else:
							print("O espaço selecionado já está ocupado")

					elemento_preenchido *= 1000
						
				else:
					print("Entrada de sentido inválida")

			#ARMADURA
			case "$":
				if sentido in (1, 2):
					elemento_preenchido = linha + (coluna/10)
					if sentido == 1:
						japreenchido = verifpreenchimento(numcasas, sentido, matriz)

						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha][coluna-1] = elemento
							matriz[linha+1][coluna-1] = elemento
							elemento_preenchido += (linha+1)/100 + (coluna)/1000 + (linha+2)/10000 + (coluna)/100000
							narmadura -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elif sentido ==2:
						japreenchido = verifpreenchimento(numcasas, sentido, matriz)

						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha-1][coluna] = elemento
							matriz[linha-1][coluna+1] = elemento
							elemento_preenchido += (linha/100) + (coluna+1)/1000 + (linha/10000)+(coluna+2)/100000
							narmadura -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elemento_preenchido *= 100000
				else:
					print("Entrada de sentido inválida")

			#PAR DE ASAS
			case "%":
				if sentido in (1, 2):
					elemento_preenchido = linha + (coluna/10)
					if sentido == 1:
						japreenchido = verifpreenchimento(numcasas, sentido, matriz)

						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha][coluna-1] = elemento
							matriz[linha+1][coluna-1] = elemento
							matriz[linha+2][coluna-1] = elemento
							elemento_preenchido += (linha+1)/100 + (coluna)/1000 + (linha+2)/10000 + (coluna)/100000 + (linha+3)/1000000 + (coluna)/10000000
							nasas -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elif sentido ==2:
						japreenchido = verifpreenchimento(numcasas, sentido, matriz)

						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha-1][coluna] = elemento
							matriz[linha-1][coluna+1] = elemento
							matriz[linha-1][coluna+2] = elemento
							elemento_preenchido += (linha/100) + (coluna+1)/1000 + (linha/10000)+(coluna+2)/100000 + (linha/1000000)+(coluna+3)/10000000
							nasas -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elemento_preenchido *= 10000000
				else:
					print("Entrada de sentido inválida")

		if japreenchido == False:
			if elemento in ("@", "#", "$", "%"):
				listapreenchidos.append(elemento_preenchido)
				print(listapreenchidos)
			else:
				print("Elemento Inválido")

def cantada(linha, coluna, matriz, espelho):
	global preenchidos, preenchidosbot
	if matriz[linha-1][coluna-1] in ("@", "#", "$", "%"):
		espelho[linha-1][coluna-1] = "x"
		elemento_acerto = matriz[linha-1][coluna-1]
		acerto = True
	else:
		espelho[linha-1][coluna-1] = "o"
		acerto = False

	return acerto


menu = True

while menu:
	print("|MENU - GUERRA ATELIÊ|\
	     \n1 - Jogar nova partida\
	     \n2 - Sair")

	while True:
		try:
			opcao = int(input("Escolha uma opção: "))
			break
		except:
			print("Entrada inválida.")

	match opcao:
		case 1:
			
			while True:
				modobot = input("Selecione o modo do BOT [Normal - Veterano]: ")
				modobot = modobot.lower()

				if modobot in ("normal", "veterano"):
					break
				else:
					print("Entrada incorreta.")

			try:
				grade = int(input("Tamanho da grade[n]\n(Ex.: n = 3, logo Grade 3x3 - Tamanho Máximo: 9x9)\nInsira tamanho da grade: "))
			except:
				print("Entrada Inválida.")

			nelmos = nelmosbot = 2*(int((grade - 1) / 4)) # 2 ELMOS A CADA 4 UNIDADES APÓS 1
			narmadura = narmadurabot = int(grade/5) # 1 ARMADURA A CADA 5 UNIDADES
			ncapas = ncapasbot = int(grade/3) # 1 CAPA A CADA 3 UNIDADES
			nasas = nasasbot = int(grade/8) # 1 PAR DE ASAS A CADA 8 UNIDADES

			pecasbot = (nelmos+ncapas+narmadura+nasas)

			for i in range(grade):
				bancadaplayer.append(["n"]*grade)
				bancadabot.append(["n"]*grade)

			preenchidos = []
			preenchidosbot = []

					
			limpar()


			print("|GINCANA DOS ATELIÊS - JOGO CONTRA TOTEM\n")
			print(f"Peças restantes para posicionar: \n Elmos[@]: {nelmos}; Capas[#]: {ncapas}; Armaduras[$]: {narmadura};  Asas[%]: {nasas}")
			exibirbancada(bancadaplayer)
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
						

					preencher(linha,coluna,elemento,sentido, numcasas, bancadaplayer, preenchidos)
				else:
					print("Sem exemplares disponíveis para posicionar essa peça.")

				#limpar()
				
				print("|GINCANA DOS ATELIÊS - JOGO CONTRA TOTEM\n")
				print(f"Peças restantes para posicionar: \n Elmos[@]: {nelmos}; Capas[#]: {ncapas}; Armaduras[$]: {narmadura};  Asas[%]: {nasas}")


				exibirbancada(bancadaplayer)

				print()
				pecas = (nelmos+ncapas+narmadura+nasas)
				if pecas == 0:
					print("MONTAGEM DA BANCADA FINALIZADA.\n")
					montagembancada = False

			#BOT FORMANDO
			while pecasbot > 0:
				while nelmosbot > 0:
					numcasas = sentido = 1
					posicaovalida = False
					while posicaovalida == False:
						linha = random.randint(1, grade)
						coluna = random.randint(1, grade)
						if verifpreenchimento(numcasas, sentido, bancadabot) == False:
							posicaovalida = True
					preencher(linha, coluna, "@", sentido, numcasas, bancadabot, preenchidosbot, "bot")
					if limite == True:
								nelmosbot += 1
					nelmosbot -= 1
				while ncapasbot > 0:
					numcasas = 2
					posicaovalida = False
					while posicaovalida == False:
						linha = random.randint(1, grade)
						coluna = random.randint(1, grade)
						sentido = random.randint(1, 2)
						if verifpreenchimento(numcasas, sentido, bancadabot) == False:
							posicaovalida = True
					preencher(linha, coluna, "#", sentido, numcasas, bancadabot, preenchidosbot, "bot")
					if limite == True:
								ncapasbot += 1
					ncapasbot -= 1
				while narmadurabot > 0:
					numcasas = 3
					posicaovalida = False
					while posicaovalida == False:
						linha = random.randint(1, grade)
						coluna = random.randint(1, grade)
						sentido = random.randint(1, 2)
						if verifpreenchimento(numcasas, sentido, bancadabot) == False:
							posicaovalida = True

					preencher(linha, coluna, "$", sentido, numcasas, bancadabot, preenchidosbot, "bot")
					if limite == True:
								narmadurabot += 1
					narmadurabot -= 1
				while nasasbot > 0:
					
					numcasas = 4
					posicaovalida = False
					while posicaovalida == False:
						linha = random.randint(1, grade)
						coluna = random.randint(1, grade)
						sentido = random.randint(1, 2)
						if verifpreenchimento(numcasas, sentido, bancadabot) == False:
							posicaovalida = True
					preencher(linha, coluna, "%", sentido, numcasas, bancadabot, preenchidosbot, "bot")
					if limite == True:
						nasasbot += 1
					nasasbot -= 1
					
				pecasbot = (nelmos+ncapas+narmadura+nasas)


			#Fase de Ataques
			print("|FASE DE CANTADAS DE POSIÇÕES|")

			bancbot_espelho = []
			bancply_espelho = []
			jogadas_bot = []
			for i in range(grade):
				bancbot_espelho.append(["n"]*grade)
				bancply_espelho.append(["n"]*grade)

			ataquesbancadas = True
			while ataquesbancadas:
				#RODADA DO PLAYER
				while True:
					try:
						linha_canto= int(input("Número da linha que deseja canta: "))
						if linha_canto < 0 and linha_canto > grade:
							print("Linha fora da bancada. Tente de novo.")
						else:
							break
					except:
						print("Entrada Inválida.")

				while True:
					try:
						coluna_canto= int(input("Número da coluna que deseja canta: "))
						if coluna_canto < 0 and coluna_canto > grade:
							print("Coluna fora da bancada. Tente de novo.")
						else:
							break
					except:
						print("Entrada Inválida.")

				acerto_ply = cantada(linha_canto, coluna_canto, bancadabot, bancbot_espelho)

				#RODADA DO BOT
				cantada_valida = False
				while cantada_valida == False:
					linbot_canto = random.randint(1, grade)
					colbot_canto = random.randint(1, grade)
					if ((linbot_canto*10)+colbot_canto) not in jogadas_bot:
						cantada_valida = True

				acerto_bot = cantada(linbot_canto, colbot_canto, bancadaplayer, bancply_espelho)

				#EXIBIÇÃO DAS BANCADAS

				exibirbancada(bancbot_espelho)

				print("--" * 20)

				exibirbancada(bancply_espelho)

		case 2:
			menu = False
		case _:
			print("Opção Incorreta")