import tkinter as tkdef 

 def iniciar_jogo():
    print("Bem-vindo ao Jogo de Escolhas!")
      tk.Label(janela, text= "Você está em uma floresta misteriosa.")
    
       tk.Label (janela, text= escolha1 = input"Você quer seguir pela trilha da esquerda ou pela trilha da direita? (esquerda/direita): ")pack()
    
    tk.Button (janela, text= if escolha1 == "esquerda":)
        tk.Label (janela, text= "Você encontrou um rio e conseguiu atravessá-lo com segurança.")
       tk.button( escolha2 = input"Você quer continuar seguindo a trilha ou voltar para casa? (seguir/voltar): ")
        
        if escolha2 == "seguir":
          tk.Label (janela, text=   print"pelo caminho da trilha voce encontrou um lobisomem!")
        
          tk.Label(janela, text=   print"Você escolhe atacar ou fugir.")
            if escolha1=="atacar"

          
        escolha2 = input("Você quer continuar seguindo a trilha? (seguir/voltar): ")
        
        if escolha2 == "seguir":
            print("Você encontrou um tesouro no final da trilha. Parabéns, você venceu!")
        
            print("Você decidiu voltar para casa.")
       
    elif escolha1 == "direita":
        print("Você se perdeu na floresta e não encontrou o caminho de volta.jogo acabou")
         
             
    else:
        print("Escolha inválida. O jogo acabou.")

iniciar_jogo()

      