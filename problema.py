# Declaração de autoria
# Nome: Marcus Vinícius Leite dos Santos
# Declaro que este código foi desenvolvido por mim, com base no meu próprio
# entendimento e esforço. Não houve plágio ou cópia integral de terceiros.
# Ferramentas de IA, quando utilizadas, foram apenas como apoio ao aprendizado
# e não para a geração integral deste código.

import os, random


def limpar():
	os.system('cls')


def exibirbancada(bancada):
	print("  ", end="")
	for i in range(1, grade+1):
		if i < 11:
			print("  ", i, end="")
		else:
			print(" ", i, end="")
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
		japreenchido = True
	else:
		for i in range(numcasas):
			if sentido == 1:
				if matriz[linha-1+i][coluna-1] in ("@", "#", "$", "%"):
					japreenchido = True
			elif sentido == 2:
				if matriz[linha-1][coluna-1+i] in ("@", "#", "$", "%"):
					japreenchido = True
				

	return japreenchido

def preencher(linha, coluna, elemento, sentido, numcasas, matriz, jogador):
	global nelmos, nelmosbot, narmadura, narmadurabot, ncapas, ncapasbot, nasas, nasasbot
	global nelmosrest, narmadurarest, ncapasrest, nasasrest
	global grade, posicionados, limite

	ultrapassou = False
	japreenchido = False
	limite = False
	if (((sentido == 1 and linha+numcasas-1 > grade) or (sentido == 2 and coluna+numcasas-1 > grade)) or (linha == 0 or coluna == 0)):
		#SE O ULTIMO ELEMENTO FOR MAIOR OU MENOR QUE AS BORDAS, NÃO EXECUTE
		limite = True
		if jogador == "player":
			ultrapassou = True
	else:
		#SE O ULTIMO ELEMENTO NÃO FOR MAIOR OU MENOR QUE AS BORDAS, EXECUTE
		match elemento:
			#ELMO
			case "@":
				japreenchido = verifpreenchimento(numcasas, sentido, matriz)
				if japreenchido == False:
					matriz[linha-1][coluna-1] = elemento
					if jogador == "player":
						posicionados["elmosply"].append((linha, coluna))
					elif jogador == "bot":
						posicionados["elmosbot"].append((linha, coluna))
					nelmosrest -=1


			#CAPA
			case "#":
				if sentido in (1, 2):
					if sentido == 1:

						japreenchido = verifpreenchimento(numcasas, sentido, matriz)
						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha][coluna-1] = elemento
							if jogador == "player":
								posicionados["capasply"].append([(linha, coluna), (linha+1, coluna)])
							elif jogador == "bot":
								posicionados["capasbot"].append([(linha, coluna), (linha+1, coluna)])
							ncapasrest -=1
							
						else:
							print("O espaço selecionado já está ocupado")
					elif sentido == 2:

						japreenchido = verifpreenchimento(numcasas, sentido, matriz)
						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha-1][coluna] = elemento
							if jogador == "player":
								posicionados["capasply"].append([(linha, coluna), (linha, coluna+1)])
							elif jogador == "bot":
								posicionados["capasbot"].append([(linha, coluna), (linha, coluna+1)])
							ncapasrest -=1

						else:
							print("O espaço selecionado já está ocupado")

				else:
					print("Entrada de sentido inválida")

			#ARMADURA
			case "$":
				if sentido in (1, 2):
					if sentido == 1:
						japreenchido = verifpreenchimento(numcasas, sentido, matriz)

						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha][coluna-1] = elemento
							matriz[linha+1][coluna-1] = elemento
							if jogador == "player":
								posicionados["armadurasply"].append([(linha, coluna), (linha+1, coluna), (linha+2,coluna)])
							elif jogador == "bot":
								posicionados["armadurasbot"].append([(linha, coluna), (linha+1, coluna), (linha+2,coluna)])
							narmadurarest -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elif sentido ==2:
						japreenchido = verifpreenchimento(numcasas, sentido, matriz)

						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha-1][coluna] = elemento
							matriz[linha-1][coluna+1] = elemento
							if jogador == "player":
								posicionados["armadurasply"].append([(linha, coluna), (linha, coluna+1), (linha, coluna+2)])
							elif jogador == "bot":
								posicionados["armadurasbot"].append([(linha, coluna), (linha, coluna+1), (linha, coluna+2)])
							narmadurarest -= 1
						else:
							print("O espaço selecionado já está ocupado")
				else:
					print("Entrada de sentido inválida")

			#PAR DE ASAS
			case "%":
				if sentido in (1, 2):
					if sentido == 1:
						japreenchido = verifpreenchimento(numcasas, sentido, matriz)

						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha][coluna-1] = elemento
							matriz[linha+1][coluna-1] = elemento
							matriz[linha+2][coluna-1] = elemento
							
							if jogador == "player":
								posicionados["asasply"].append([(linha, coluna), (linha+1, coluna), (linha+2,coluna), (linha+3, coluna)])
							elif jogador == "bot":
								posicionados["asasbot"].append([(linha, coluna), (linha+1, coluna), (linha+2,coluna), (linha+3, coluna)])					
							nasasrest -= 1
						else:
							print("O espaço selecionado já está ocupado")
					elif sentido == 2:
						japreenchido = verifpreenchimento(numcasas, sentido, matriz)

						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha-1][coluna] = elemento
							matriz[linha-1][coluna+1] = elemento
							matriz[linha-1][coluna+2] = elemento
							
							if jogador == "player":
								posicionados["asasply"].append([(linha, coluna), (linha, coluna+1), (linha, coluna+2), (linha, coluna+3)])
							elif jogador == "bot":
								posicionados["asasbot"].append([(linha, coluna), (linha, coluna+1), (linha, coluna+2), (linha, coluna+3)])
							nasasrest -= 1
						else:
							print("O espaço selecionado já está ocupado")
				else:
					print("Entrada de sentido inválida")

	return japreenchido, ultrapassou

def cantada(linha, coluna, matriz, espelho, jogador):
	global posicionados, pontos_player, pontos_bot
	global vencedor
	global acertosply, errosply
	global acertosbot, errosbot
	global completas_ply, completas_bot
	global cantadas_ply

	coordenada = (linha, coluna)
	pecacompleta = False
	if matriz[linha-1][coluna-1] in ("@", "#", "$", "%"):
		espelho[linha-1][coluna-1] = "X"
		elemento_acerto = matriz[linha-1][coluna-1]
		print(jogador, "ACERTOU UMA CASA COM PEÇA! + 10 PONTOS")

		if jogador == "PLAYER":
			pontos_player += 10
			acertosply += 1
			sufixo = "bot"
		elif jogador == "BOT":
			pontos_bot += 10
			acertosbot += 1
			sufixo = "ply"
		match elemento_acerto:
				#COOMPARA A COORDENADA DA CANTADA/ATAQUE COM CADA COORDENADA DE CADA ELEMENTO
				#PARA RETIRA-LO DOS ELEMENTOS AINDA NÃO DESCOBERTOS
			case "@":
				for coords_elmo in posicionados["elmos"+sufixo]:
					if coordenada == coords_elmo:
						posicionados["elmos"+sufixo].remove(coords_elmo)
						print(f"PEÇA COMPLETADA POR {jogador}: ELMO")
						pecacompleta = True
			case "#":

				for capa in posicionados["capas"+sufixo]:
					for coords_capa in capa:
						if coordenada == coords_capa:
							posicionados["capas"+sufixo][posicionados["capas"+sufixo].index(capa)][posicionados["capas"+sufixo][posicionados["capas"+sufixo].index(capa)].index(coords_capa)] = 0
					pecacompleta = True

					for verif_capa in capa:
						if verif_capa != 0:
							pecacompleta = False
					if pecacompleta == True:
						print(f"PEÇA COMPLETA POR {jogador}: CAPA")
						posicionados["capas"+sufixo].remove(capa)
			case "$":
				
				for armadura in posicionados["armaduras"+sufixo]:
					for coords_armadura in armadura:
						if coordenada == coords_armadura:
							posicionados["armaduras"+sufixo][posicionados["armaduras"+sufixo].index(armadura)][posicionados["armaduras"+sufixo][posicionados["armaduras"+sufixo].index(armadura)].index(coords_armadura)] = 0
					pecacompleta = True

					for verif_armadura in armadura:
						if verif_armadura != 0:
							pecacompleta = False
					if pecacompleta == True:
						print(f"PEÇA COMPLETA POR {jogador}: ARMADURA")
						posicionados["armaduras"+sufixo].remove(armadura)
			case "%":
				
				for asa in posicionados["asas"+sufixo]:
					for coords_asa in asa:
						if coordenada == coords_asa:
							posicionados["asas"+sufixo][posicionados["asas"+sufixo].index(asa)][posicionados["asas"+sufixo][posicionados["asas"+sufixo].index(asa)].index(coords_asa)] = 0
					pecacompleta = True

					for verif_asa in asa:
						if verif_asa != 0:
							pecacompleta = False
					if pecacompleta == True:
						print(f"PEÇA COMPLETA POR {jogador}: ASA")
						posicionados["asas"+sufixo].remove(asa)

						
		if pecacompleta == True:
			if jogador == "PLAYER":
				pontos_player += 50
				completas_ply += 1
			elif jogador == "BOT":
				pontos_bot += 50
				completas_bot += 1
			print("+50 PONTOS")
		acerto = True
	else:
		espelho[linha-1][coluna-1] = "O"
		print(jogador, " ERROU E A CASA CANTADA NÃO POSSUI PEÇA. -5 PONTOS")
		if jogador == "PLAYER":
			pontos_player -=5
			errosply += 1
		elif jogador == "BOT":
			pontos_bot -= 5
			errosbot += 1
		acerto = False

	if jogador == "PLAYER":
		cantadas_ply += 1

	if posicionados["elmosply"] == [] and posicionados["armadurasply"] == [] and posicionados["capasply"] == [] and posicionados["asasply"] == []:
		vencedor = "bot"
		pontos_bot += 200
	elif posicionados["elmosbot"] == [] and posicionados["armadurasbot"] == [] and posicionados["capasbot"] == [] and posicionados["asasbot"] == []:
		vencedor = "player"
		pontos_player += 200

	return (acerto, pecacompleta)

def olho_clinico(linha, coluna, matriz):
	contador = 0
	for i in range(3):
		for j in range(3):
			linha_verif = linha+i-1
			coluna_verif = coluna+j-1
			if (linha_verif< 1 or linha_verif > grade) or (coluna_verif<1 or coluna_verif> grade):
				pass
			else:
				if matriz[linha_verif-1][coluna_verif-1] in ("@", "#", "$", "%"):
					contador += 1
	print(f"Tem {contador} partes de peças em volta desse ponto.\n-30 PONTOS DEVIDO A USO DE OLHO CLÍNICO")

menu = True
num_partidas = 0
partidas = {
	"pontuacao":[],
	"bancada_escolhida":[],
	"modobot":[],
	"resultado":[],
	"num_rodadas":[]
}
while menu:
	print("|MENU - GUERRA ATELIÊ|\
	     \n1 - Jogar nova partida\
	     \n2 - Regras\
		 \n3 - Placar do dia\
	     \n4- Sair")

	while True:
		try:
			opcao = int(input("Escolha uma opção: "))
			break
		except:
			print("Entrada inválida.")

	match opcao:
		case 1:
			num_partidas += 1
			while True:
				modobot = input("Selecione o modo do BOT [Novato - Veterano]: ")
				modobot = modobot.lower()

				if modobot in ("novato", "veterano"):
					break
				else:
					print("Entrada incorreta.")

			while True:
				montagem = input("Selecione o modo de Montagem [Manual - Automatica]: ")
				montagem = montagem.lower()

				if montagem in ("manual", "automatica"):
					break
				else:
					print("Entrada incorreta.")

			try:
				grade = int(input("Tamanho da grade[n]\n(Ex.: n = 3, logo Grade 3x3 - Tamanho Máximo: 9x9)\nInsira tamanho da grade: "))
			except:
				print("Entrada Inválida.")

			nelmos = nelmosrest = nelmosbot = 2*(int((grade - 1) / 4)) # 2 ELMOS A CADA 4 UNIDADES APÓS 1
			narmadura = narmadurarest = narmadurabot = int(grade/5) # 1 ARMADURA A CADA 5 UNIDADES
			ncapas = ncapasrest = ncapasbot = int(grade/3) # 1 CAPA A CADA 3 UNIDADES
			nasas = nasasrest = nasasbot = int(grade/8) # 1 PAR DE ASAS A CADA 8 UNIDADES
			usos_olho = int(grade/2) # 1 OLHOS CLÍNICO A CADA 2 UNIDADES
			
			pecas = pecasbot = (nelmos+ncapas+narmadura+nasas)

			ultrapassou = False
			qtelemento_validez = True
			japreenchido = False
			

			bancadaplayer = []
			bancadabot = []
			for i in range(grade):
				bancadaplayer.append(["n"]*grade)
				bancadabot.append(["n"]*grade)
			
			#>>> dic['a'].append('a')

			posicionados = {
			"elmosply":[],
			"capasply":[], 
			"armadurasply":[],
			"asasply":[],

			"elmosbot":[], 
			"capasbot":[], 
			"armadurasbot":[], 
			"asasbot":[]
			}
					
					
			limpar()

			if montagem == "manual":
				montagembancada = True
				while montagembancada:
					sentido=1
					if ultrapassou == True:
						print("POSIÇÃO INVÁLIDA! LIMITE DA BANCADA ATINGIDO OU ULTRAPASSADO")
					if japreenchido == True:
						print("POSIÇÃO INVÁLIDA. JÁ PREENCHIDA")
					if qtelemento_validez == False:
						print("Sem exemplares disponíveis para posicionar essa peça.")
					print("|GINCANA DOS ATELIÊS - JOGO CONTRA TOTEM\n")
					print(f"Peças restantes para posicionar: \n Elmos[@]: {nelmosrest}; Capas[#]: {ncapasrest}; Armaduras[$]: {narmadurarest};  Asas[%]: {nasasrest}")


					exibirbancada(bancadaplayer)

					print()
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
									if nelmosrest == 0:
										qtelemento_validez = False
									numcasas = 1
								case "#":
									if ncapasrest == 0:
										qtelemento_validez = False
									numcasas = 2
								case "$":
									if narmadurarest == 0:
										qtelemento_validez = False
									numcasas = 3
								case "%":
									if nasasrest == 0:
										qtelemento_validez = False
									numcasas = 4
							valido = True

					if elemento == "encerrar":
						print("Programa Encerrado")
						break

					if qtelemento_validez == True:
						if elemento not in ("@", "encerrar"):
							sentido=int(input("Defina o sentido(Vertical [1] Horizontal[2]):"))
							

						japreenchido, ultrapassou = preencher(linha,coluna,elemento,sentido, numcasas, bancadaplayer, "player")
					else:
						print("Sem exemplares disponíveis para posicionar essa peça.")

					limpar()
					
					pecas = (nelmos+ncapas+narmadura+nasas)
					if pecas == 0:
						print("MONTAGEM DA BANCADA FINALIZADA.\n")
						montagembancada = False
			elif montagem == "automatica":
				while pecas > 0:
					while nelmos > 0:
						numcasas = sentido = 1
						posicaovalida = False
						while posicaovalida == False:
							linha = random.randint(1, grade)
							coluna = random.randint(1, grade)
							if verifpreenchimento(numcasas, sentido, bancadaplayer) == False:
								posicaovalida = True
						preencher(linha, coluna, "@", sentido, numcasas, bancadaplayer, "player")

						if limite == True:
									nelmos += 1
						nelmos -= 1
					while ncapas > 0:
						numcasas = 2
						posicaovalida = False
						while posicaovalida == False:
							linha = random.randint(1, grade)
							coluna = random.randint(1, grade)
							sentido = random.randint(1, 2)
							if verifpreenchimento(numcasas, sentido, bancadaplayer) == False:
								posicaovalida = True
						preencher(linha, coluna, "#", sentido, numcasas, bancadaplayer, "player")

						if limite == True:
									ncapas += 1
						ncapas -= 1
					while narmadura > 0:
						numcasas = 3
						posicaovalida = False
						while posicaovalida == False:
							linha = random.randint(1, grade)
							coluna = random.randint(1, grade)
							sentido = random.randint(1, 2)
							if verifpreenchimento(numcasas, sentido, bancadaplayer) == False:
								posicaovalida = True
	
						preencher(linha, coluna, "$", sentido, numcasas, bancadaplayer, "player")

						if limite == True:
							narmadura += 1
						narmadura -= 1
					while nasas > 0:
						
						numcasas = 4
						posicaovalida = False
						while posicaovalida == False:
							linha = random.randint(1, grade)
							coluna = random.randint(1, grade)
							sentido = random.randint(1, 2)
							if verifpreenchimento(numcasas, sentido, bancadaplayer) == False:
								posicaovalida = True
						preencher(linha, coluna, "%", sentido, numcasas, bancadaplayer, "player")

						if limite == True:
							nasas += 1
						nasas -= 1
						
					pecas = (nelmos+ncapas+narmadura+nasas)
					
					if pecas == 0:
						print("MONTAGEM AUTOMÁTICA DA BANCADA FINALIZADA.\n ")

				exibirbancada(bancadaplayer)
				input("Aperte qualquer botão para continuar")

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
					preencher(linha, coluna, "@", sentido, numcasas, bancadabot, "bot")
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
					preencher(linha, coluna, "#", sentido, numcasas, bancadabot, "bot")
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

					preencher(linha, coluna, "$", sentido, numcasas, bancadabot, "bot")
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
					preencher(linha, coluna, "%", sentido, numcasas, bancadabot, "bot")
					if limite == True:
						nasasbot += 1
					nasasbot -= 1
					
				pecasbot = (nelmosbot+ncapasbot+narmadurabot+nasasbot)

			#Fase de Ataques

			pontos_player = pontos_bot = 0
			acertosply = acertosbot = 0
			errosply = errosbot = 0
			completas_ply = completas_bot = 0
			cantadas_ply = 0

			bancbot_espelho = []
			bancply_espelho = []
			jogadas_bot = []
			for i in range(grade):
				bancbot_espelho.append(["n"]*grade)
				bancply_espelho.append(["n"]*grade)

			ataquesbancadas = True
			inicio = True
			rodadas = 0
			vencedor = None
			while ataquesbancadas:
				rodadas += 1
				print(f"RODADA {rodadas} PONTOS")
				#EXIBIÇÃO DAS BANCADAS
				print(f"SUA BANCADA - {pontos_player}: ")
				exibirbancada(bancbot_espelho)

				print("--" * 20)

				print(f"BANCANDA DO BOT - {pontos_bot} PONTOS: ")
				exibirbancada(bancply_espelho)
				#RODADA DO PLAYER
				op_valida = False
				while op_valida == False:
					op_valida = True
					print(f"|FASE DE CANTADAS DE POSIÇÕES|\
						\n1 - Cantar uma casa\
						\n2 - Usar Olho Clínico - {usos_olho} Usos restantes\
						\n3 - Desistir")
					while True:
						try:
							opcao_cantadas = int(input("Insira uma opção:"))
							break
						except:
							print("Entrada incorreta. Tente novamente.")

					match opcao_cantadas:
						case 1:
							while True:
								try:
									linha_canto= int(input("Número da linha que deseja cantar: "))
									if linha_canto < 0 and linha_canto > grade:
										print("Linha fora da bancada. Tente de novo.")
									else:
										break
								except:
									print("Entrada Inválida.")
			
							jaextendeu = False
							while True:
								try:
									coluna_canto= int(input("Número da coluna que deseja cantar: "))
									if coluna_canto < 0 and coluna_canto > grade:
										print("Coluna fora da bancada. Tente de novo.")
									else:
										break
								except:
									print("Entrada Inválida.")
							if bancbot_espelho[linha_canto-1][coluna_canto-1] in ("X", "O"):
								print("Já joguei nessa casa. Escolha outra")
								op_valida = False

							if op_valida:
								acerto_ply = cantada(linha_canto, coluna_canto, bancadabot, bancbot_espelho, "PLAYER")
						case 2:
							if usos_olho > 0:
								while True:
									while True:#INPUT LINHA
										try:
											linha_olho= int(input("Número da linha que deseja usar o olho clínico: "))
											if linha_olho < 0 or linha_olho > grade:
												print("Linha fora da bancada. Tente de novo.")
											else:
												break
										except:
											print("Entrada Inválida.")
									while True:#INPUT COLUNA
										try:
											coluna_olho= int(input("Número da coluna que deseja usar o olho clínico: "))
											if coluna_olho < 0 or coluna_olho > grade:
												print("Coluna fora da bancada. Tente de novo.")
											else:
												break
										except:
											print("Entrada Inválida.")
									olho_clinico(linha_olho, coluna_olho, bancadabot)
									pontos_player -=30
									usos_olho -=1
									break
							else:
								print("Sem usos de olho clínico disponíveis. Tente novamente outra opção.")
								op_valida = False
						case 3:
							print("DESISTÊNCIA.")
							vencedor = "bot"
						case _:
							print("Opção Inválida. Tente novamente")
							op_valida = False
			
				#RODADA DO BOT
				if modobot == "novato":
					cantada_valida = False
					while cantada_valida == False:
						linbot_canto = random.randint(1, grade)
						colbot_canto = random.randint(1, grade)
						if ((linbot_canto*10)+colbot_canto) not in jogadas_bot:
							cantada_valida = True

					acerto_bot = cantada(linbot_canto, colbot_canto, bancadaplayer, bancply_espelho, "BOT")

				elif modobot == "veterano":

					if inicio:
						linbot_canto = random.randint(1, grade)
						colbot_canto = random.randint(1, grade)

						acerto_bot, completa = cantada(linbot_canto, colbot_canto, bancadaplayer, bancply_espelho, "BOT")
						
						if acerto_bot:
							if completa:
								inicio = True
							else:
								inicio = False
								linha_partida = linbot_canto
								coluna_partida = colbot_canto
								extensao = False
								direcao = random.randint(1, 2)
								sentido = random.randint(1, 2)
								tentativas_direcao = 0
					else:
						if extensao == False:
							linbot_canto = linha_partida
							colbot_canto = coluna_partida

						if direcao == 1: #VERTICAL
							if sentido == 1:#CIMA
								linbot_canto -=1
							elif sentido == 2:#BAIXO
								linbot_canto += 1

						elif direcao == 2: #HORIZONTAL
							if sentido == 1:#ESQUERDA
								colbot_canto -=1
							elif sentido == 2:#DIREITA
								colbot_canto += 1
								
						acerto_bot, completa = cantada(linbot_canto, colbot_canto, bancadaplayer, bancply_espelho, "BOT")
                        
						if completa:
                            #VOLTA PARA AS CANTADAS ALEATORIAS
							inicio = True
							extensao = False
						else:
							if acerto_bot:
								extensao = True
							else:
								if extensao == True:
                                    # ACHOU O FIM DO LADO DE UMA PEÇA. INVERTE E SE EXTENDE PARA O OUTRO LADO
									extensao = False
									sentido = 2 if sentido == 1 else 1
								else:
									tentativas_direcao += 1
                                    
									if tentativas_direcao < 2:
										sentido = 2 if sentido == 1 else 1
									else:
										direcao = 2 if direcao == 1 else 1
										sentido = random.randint(1, 2)
										tentativas_direcao = 0

				if pontos_player < 0:
					pontos_player = 0
				if pontos_bot < 0:
					pontos_bot = 0


				if vencedor in ("player", "bot"):
					ataquesbancadas = False
					print("PARTIDA ENCERRADA.")

			#ESTATÍSTICAS
			if (acertosply+errosply) == 0:
				aproveitamento = 0
			else:
				aproveitamento = acertosply*100/(acertosply+errosply)

			partidas["pontuacao"].append(pontos_player)
			partidas["bancada_escolhida"].append(grade)
			partidas["modobot"].append(modobot)
			partidas["resultado"].append(vencedor)
			partidas["num_rodadas"].append(rodadas)

			print(f"|ESTATÍSTICAS|\
			      \nResultado - Vencedor: {vencedor}\
				  \nQuant. de rodadas: {rodadas}\
				  \nCasas cantadas - Jogador: {cantadas_ply}\
				  \n\
				  \nAcertos - Jogador: {acertosply}; Bot: {acertosbot}\
				  \nErros - Jogador: {errosply}; Bot: {errosbot}\
				  \n\
				  \nAproveitamento - Jogador: {aproveitamento}%\
				  \n\
				  \nPeças completadas - Jogador: {completas_ply}; Bot: {completas_bot}\
				  \n\
				  \nUsos do Olho Clínico gastos: {int(grade/2) - usos_olho}\
				  \n\
				  \nPontuação Final - Jogador: {pontos_player} pontos; Bot: {pontos_bot}")

			print("BANCADA DO BOT.")
			exibirbancada(bancadabot)

		case 2:
			print("|REGRAS DO JOGO|\
				  \n- O objetivo é descobrir todas as peças escondidas na bancada do adversário\n antes que ele descubra as suas.\
			    \n\n- A bancada é quadrada. O tamanho determina quantas peças cada jogador terá;\n no modo automático, elas são posicionadas aleatoriamente.\
			    \n\n- As peças ocupam casas consecutivas: @ ocupa 1 casa, # ocupa 2, $ ocupa 3 e % ocupa 4.\n Peças não podem se sobrepor nem ultrapassar os limites da bancada.\
			    \n\n- Em cada rodada, o jogador escolhe uma posição para tentar acertar.\n Depois, o bot também faz uma tentativa.\
			    \n\n- Cada acerto vale 10 pontos. Ao descobrir uma peça inteira, ganha-se mais 50 pontos.\n Cada erro desconta 5 pontos.\
			    \n\n- O Olho Clínico revela quantas partes de peças existem ao redor da posição escolhida.\n Cada uso custa 30 pontos e a quantidade de usos depende do tamanho da bancada.\
			    \n\n- A partida termina quando todas as peças de um dos lados forem descobertas.\n Quem ainda tiver peças escondidas vence. O jogador também pode desistir.\n")
		case 3:
			#SE EU FIZER « pontuacao_copia = partidas["pontuacao"] », pontuacao_copia vai ser uma referência
			#de partidas["pontuacao"]. Logo, ao alterar o valor de partidas["pontuacao"] também vai alterar pontuacao_copia.
			
			#COMO MEU OBJETIVO é guardar a lista pontuacao original para resubstituir depois, uso a função built-in .copy()
			#para literalmente copiar o valor de partidas["pontuacao"] e assim guardar um valor independente na memoria

			pontuacao_copia = partidas["pontuacao"].copy()
			if num_partidas == 0:
				print("\nSEM PARTIDAS REGISTRADAS AINDA.")
			else:
				for i in range(len(partidas["pontuacao"])):
					maior_indice = 0
					maior_pontuacao = 0
					for e in partidas["pontuacao"]:
						if e > maior_pontuacao:
							maior_indice = partidas["pontuacao"].index(e)
							maior_pontuacao = e
					print(f"{i+1}º PARTIDA - PONTUAÇÃO {partidas["pontuacao"][maior_indice]}\
					      \n>> BANCADA ESCOLHIDA - {partidas["bancada_escolhida"][maior_indice]}\
					      \n>> MODO DO ADVERSÁRIO - {partidas["modobot"][maior_indice].upper()}\
						  \n>> RESULTADO - VENCEDOR {partidas['resultado'][maior_indice].upper()}\
						  \n>> NÚMERO DE RODADAS - {partidas['num_rodadas'][maior_indice]}\
						  \n\n")		
					partidas["pontuacao"][maior_indice] = -1
				partidas["pontuacao"] = pontuacao_copia


		case 4:
			menu = False
		case _:
			print("Opção Incorreta")