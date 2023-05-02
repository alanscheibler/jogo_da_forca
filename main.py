import os
from funcoes import limpar, resposta, sHistorico, eHistorico, cores, menuHistorico

while True:
    nDica = -1
    chances = 5
    limpar()
    print(cores[4] , "- * "*5 , cores[3] , " JOGO DA FORCA " , cores[4] + " - *"*5 , "\n" ,
          cores[4] , " "*18, " *- Bem-vindo! -* " , cores[0])
    menu = input("Digite:" + "\n" + cores[2] + "*(1) " + cores[0] + "para " + cores[2] + "jogar " + cores[0] + "\n" +  
                  cores[4] + "*(2) " + cores[0] + "para " + cores[4] + "Ver Histórico " + cores[0] + "\n" +
                  cores[5] + "*(0) " + cores[0] + "para " + cores[5] + "sair " + cores[0] + "\n")

    if menu == "1":
        limpar()
        nDesafiante = input("-Insira o nome do" + cores[4] + " desafiante: " + "\n" + cores[0])
        nCompetidor = input("\n" + "-Insira o nome do" + cores[1] + " competidor: " + "\n" + cores[0])
        limpar()

        while True:
            pChave = input(cores[4] + "Desafiante " + cores[0] + "insira a " + cores [4] + "palavra chave! " + cores[0] + "\n").upper()
            if pChave != "":
                break

        dica1 = input("\n" + cores[4] + "Desafiante " + cores[0] + "insira a primeira " + cores[4] + "dica! " + cores[0] + "\n")
        dica2 = input("\n" + cores[4] + "Desafiante " + cores[0] + "insira a segunda " + cores[4] + "dica! " + cores[0] + "\n")
        dica3 = input("\n" + cores[4] + "Desafiante " + cores[0] + "insira a terceira " + cores[4] + "dica! " + cores[0] + "\n")
        dicas = [dica1, dica2, dica3]

        limpar()
        numLetras = ["*"] * len(pChave)
        quanLetras = len(pChave)
        tentLetras = []

        while chances != 0 and "".join(numLetras) != pChave:
            print(cores[1] , "A palavra contém ", quanLetras, " letras!","\n", numLetras , cores[0] + "\n" "\n", 
                    "Você ainda tem ", cores[3] , chances , cores[0] , "tentativas!" "\n",
                    )             
            if nDica <2:
            
                opcao = input("Digite " + cores[2] + "(1) " + cores[0] + "para " + cores[2] + "jogar " + cores[0] +
                        "ou " + cores[4] + "(0) " + cores[0] + "para receber uma " + cores[4] + "dica!" + cores[0] + "\n")
                
                if opcao == "0":
                    nDica = nDica + 1
                    print("\n" + "A dica é: " + cores[3] + dicas[nDica] + cores[0] + "\n")
                    vResposta = resposta()
                    limpar()  

                elif opcao == "1":
                    vResposta = resposta()
                    limpar() 

                elif opcao != "0" or opcao != "1":
                        print(cores[2] + "Por favor pressione " + cores[4] + "(enter) " , 
                        cores[2] + "para continuar e escolha uma opção válida" + cores[0])
                        input()
                        limpar()
            else:
                print("\n" + cores[5] + "Suas dicas acabaram! " "\n", cores[0])
                vResposta = resposta()
                limpar()
                
            while vResposta.upper() in tentLetras:
                print(cores[1] , "Você já escolheu essa letra, tente outra!" , cores[0], "\n", 
                      "Você já tentou as seguintes letras: ", cores[4] , tentLetras, "!" , cores[0] + "\n")
                print(cores[1] , "A palavra contém ", quanLetras, " letras!","\n", numLetras , cores[0] + "\n" "\n", 
                    "Você ainda tem ", cores[3] , chances , cores[0] , "tentativas!" "\n")
                vResposta = resposta()
                limpar()

            tentLetras.append(vResposta.upper())
            if vResposta.upper() in pChave:
                print(cores[4] , "Você acertou uma letra!", "\n" , cores[0] ,
                "Você já tentou as seguintes letras: ", cores[4] , tentLetras, "!" , cores[0] + "\n")
                for item in range(len(pChave)):
                    if vResposta.upper() == pChave[item]:
                        numLetras[item] = vResposta.upper()
                        print(cores[1] , numLetras , cores[0])

            else:
                chances = chances -1
                print(cores[1] ,"A letra digitada não compõe a palavra, tente outra!","\n", cores[0],
                    "Você já tentou as seguintes letras:",cores[4] , tentLetras, cores[0], "\n")

        if chances == 0:
            print("Infelizmente suas tentativas acabaram " +cores[5] + "COMPETIDOR "+ nCompetidor.upper()+ " você perdeu!", "\n"+
                cores[0] + "Parabéns "+ cores[4]+ "DESAFIANTE "+ nDesafiante.upper()+ " você ganhou!", "\n" + "\n"+
                cores[0] + "A palavra chave era: "+ cores[4] + pChave+ " !"+ cores[0] + "\n")
            
            resultado = sHistorico()
            resultado.append("Vencedor: DESAFIANTE - " + nDesafiante + " - Perdedor: COMPETIDOR - " + nCompetidor + " - Palavra Chave: " + pChave + "\n")
            eHistorico(resultado)
            print("\n"+ cores[2] + "Obrigado por jogar, até a próxima!", "\n"+                
                    cores[4]+ "Pressione enter para continuar!")
            input()

        else:
            print("Parabéns " + cores[4] + "COMPETIDOR " + nCompetidor.upper() + " você ganhou!" "\n",
                 cores[0] + "Infelizmente " + cores[5] + "DESAFIANTE " + nDesafiante.upper() + " você perdeu!" + cores[0])
            resultado = sHistorico()
            resultado.append("Vencedor: COMPETIDOR - " + nCompetidor + " - Perdedor: DESAFIANTE - " + nDesafiante + " - Palavra Chave: " + pChave + "\n")
            eHistorico(resultado)
            print("\n" + cores[2] , "Obrigado por jogar, até a próxima!", "\n" ,
                    cores[4] , "Pressione enter para continuar!")
            input()
        print()
    
    elif menu == "2":
        limpar()
        menuHistorico()
        
    elif menu == "0":
        print(cores[2] + "Obrigado por jogar, até a próxima!" + cores[0])
        break
    
    else:
        print(cores[2] + "Por favor pressione " + cores[4] + "(enter) " , 
              cores[2] + "para continuar e escolha uma opção válida" + cores[0])
        input()