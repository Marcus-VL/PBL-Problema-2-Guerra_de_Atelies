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

def preencher(linha, coluna, elemento, sentido, numcasas, matriz, jogador):
	global nelmos, nelmosbot, narmadura, narmadurabot, ncapas, ncapasbot, nasas, nasasbot, limite

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
					if jogador == "player":
						posicionados["elmosply"].append((linha, coluna))
						nelmos -= 1
					elif jogador == "bot":
						posicionados["elmosbot"].append((linha, coluna))
						nelmosbot -= 1


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
								ncapas -= 1
							elif jogador == "bot":
								posicionados["capasbot"].append([(linha, coluna), (linha+1, coluna)])
								ncapasbot -= 1
							
						else:
							print("O espaço selecionado já está ocupado")
					elif sentido == 2:

						japreenchido = verifpreenchimento(numcasas, sentido, matriz)
						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha-1][coluna] = elemento
							if jogador == "player":
								posicionados["capasply"].append([(linha, coluna), (linha, coluna+1)])
								ncapas -= 1
							elif jogador == "bot":
								posicionados["capasbot"].append([(linha, coluna), (linha, coluna+1)])
								ncapasbot -=1
						else:
							print("O espaço selecionado já está ocupado")

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
							if jogador == "player":
								posicionados["armadurasply"].append([(linha, coluna), (linha+1, coluna), (linha+2,coluna)])
								narmadura -= 1
							elif jogador == "bot":
								posicionados["armadurasbot"].append([(linha, coluna), (linha+1, coluna), (linha+2,coluna)])
								narmadurabot -= 1
							
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
								narmadura -= 1
							elif jogador == "bot":
								posicionados["armadurasbot"].append([(linha, coluna), (linha, coluna+1), (linha, coluna+2)])
								narmadurabot -=1
						else:
							print("O espaço selecionado já está ocupado")
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
							
							if jogador == "player":
								posicionados["asasply"].append([(linha, coluna), (linha+1, coluna), (linha+2,coluna), (linha+3, coluna)])
								nasas -= 1
							elif jogador == "bot":
								posicionados["asasbot"].append([(linha, coluna), (linha+1, coluna), (linha+2,coluna), (linha+3, coluna)])
								nasasbot -= 1						
							
						else:
							print("O espaço selecionado já está ocupado")
					elif sentido ==2:
						japreenchido = verifpreenchimento(numcasas, sentido, matriz)

						if japreenchido == False:
							matriz[linha-1][coluna-1] = elemento
							matriz[linha-1][coluna] = elemento
							matriz[linha-1][coluna+1] = elemento
							matriz[linha-1][coluna+2] = elemento
							
							if jogador == "player":
								posicionados["asasply"].append([(linha, coluna), (linha, coluna+1), (linha, coluna+2), (linha, coluna+3)])
								nasas -= 1
							elif jogador == "bot":
								posicionados["asasbot"].append([(linha, coluna), (linha, coluna+1), (linha, coluna+2), (linha, coluna+3)])
								nasasbot -= 1
								
						else:
							print("O espaço selecionado já está ocupado")
				else:
					print("Entrada de sentido inválida")

		if japreenchido == True:
			print("POSIÇÃO INVÁLIDA. JÁ PREENCHIDA")

def cantada(linha, coluna, matriz, espelho, jogador):
	global posicionados, pontos_player, pontos_bot
	coordenada = (linha, coluna)
	pecacompleta = False
	if matriz[linha-1][coluna-1] in ("@", "#", "$", "%"):
		espelho[linha-1][coluna-1] = "x"
		elemento_acerto = matriz[linha-1][coluna-1]
		print(jogador, "ACERTOU UMA CASA COM PEÇA! + 10 PONTOS")

		if jogador == "PLAYER":
			pontos_player += 10
			sufixo = "bot"
		elif jogador == "BOT":
			pontos_bot += 10
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
			elif jogador == "BOT":
				pontos_bot += 50
			print("+50 PONTOS")
		acerto = True
	else:
		espelho[linha-1][coluna-1] = "o"
		print(jogador, " ERROU E A CASA CANTADA NÃO POSSUI PEÇA. -5 PONTOS")
		if jogador == "PLAYER":
			pontos_player -=5
		elif jogador == "BOT":
			pontos_bot -= 5
		acerto = False

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
	print(posicionados)
	print(f"Tem {contador} partes de peças em volta desse ponto.\n-30 PONTOS DEVIDO A USO DE OLHO CLÍNICO")

menu = True

while menu:
	print("|MENU - GUERRA ATELIÊ|\
	     \n1 - Jogar nova partida\
	     \n2 - Regras\
		 \n3 - Pontuação do dia\
	     \n4- Sair")

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
			usos_olho = int(grade/2) # 1 OLHOS CLÍNICO A CADA 2 UNIDADES
			
			pecasbot = (nelmos+ncapas+narmadura+nasas)

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
						

					preencher(linha,coluna,elemento,sentido, numcasas, bancadaplayer, "player")
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
					
				pecasbot = (nelmos+ncapas+narmadura+nasas)


			#Fase de Ataques
			print("|FASE DE CANTADAS DE POSIÇÕES|")

			pontos_player = pontos_bot = 0
			bancbot_espelho = []
			bancply_espelho = []
			jogadas_bot = []
			for i in range(grade):
				bancbot_espelho.append(["n"]*grade)
				bancply_espelho.append(["n"]*grade)

			ataquesbancadas = True
			inicio = True
			while ataquesbancadas:
				#RODADA DO PLAYER
				if usos_olho > 0:
					while True:
						ajuda = input(f"Você tem {usos_olho} usos do olho clínico. Deseja usar um olho clinico?[S/N]:")
						if ajuda.lower() == "s":
							while True:#INPUT LINHA
								try:
									linha_olho= int(input("Número da linha que deseja usar o olho clínico: "))
									if linha_olho < 0 and linha_olho > grade:
										print("Linha fora da bancada. Tente de novo.")
									else:
										break
								except:
									print("Entrada Inválida.")
							while True:#INPUT COLUNA
								try:
									coluna_olho= int(input("Número da coluna que deseja usar o olho clínico: "))
									if coluna_olho < 0 and coluna_olho > grade:
										print("Coluna fora da bancada. Tente de novo.")
									else:
										break
								except:
									print("Entrada Inválida.")
							olho_clinico(linha_olho, coluna_olho, bancadabot)
							pontos_player -=30
							usos_olho -=1
							break
						elif ajuda.lower() == "n":
							break
						else:
							print("Entrada incorreta. Tente novamente")
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

				acerto_ply = cantada(linha_canto, coluna_canto, bancadabot, bancbot_espelho, "PLAYER")
			
				#RODADA DO BOT
				if modobot == "normal":
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

				#EXIBIÇÃO DAS BANCADAS
				print("SUA BANCADA: ")
				exibirbancada(bancbot_espelho)

				print("--" * 20)

				print("BANCANDA DO BOT: ")
				exibirbancada(bancply_espelho)

				

		case 2:
			menu = False
		case _:
			print("Opção Incorreta")