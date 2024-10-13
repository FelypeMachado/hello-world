print ( "seja bem vindo a sorveteria hello word" )
print ( "Vendemos casquinhas, aonde sera cobrado pelo numero de bolas de sorvete")
print ( "Vamos la ")
quantia_casquinhas = int( input("quantas casquinhas serão?" ))
escolha = False

while escolha == False:
    opcao = int(input("Temos os sabores a seguir:\n[1] - Chocolate\n[2] - Creme\n[3] - Morango\n[4] - Flocos\n[5] - Maracuja\n[6] - Chocomenta\n[7] - Personalisado:"))
   
    #chocolate
    if opcao == 1:
        print("O sabor de chocolate está saindo por 5 R$ uma bola, gostaria de quantas bolas de sorvete?")
        quer = int(input("[1] - 1 Bola\n[2] - 2 Bolas\n[3] - 3 Bolas\n[4] - 4 ou mais bolas:"))
        if quer == 1:
            valor_c1 = quantia_casquinhas * 5 
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de chocolate com {quer} bola")
            print ( f" seu pedido ficou em {valor_c1} R$, dirija-se ao caixa para efetuar o pagamento")
        
        elif quer == 2:
             valor_c2 = quantia_casquinhas * 10 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de chocolate com {quer} bolas")
             print ( f" seu pedido ficou em {valor_c2} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 3:
             valor_c3 = quantia_casquinhas * 15 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de chocolate com {quer} bolas")
             print ( f" seu pedido ficou em {valor_c3} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 4:
            quantidade_de_bolas_c = int( input("Quantas bolas serão?  "))
            preso_da_escolha_4_c = quantidade_de_bolas_c * 5 
            valor_c4 = preso_da_escolha_4_c * quantia_casquinhas
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de chocolate com {quantidade_de_bolas_c} bolas")
            print ( f"Seu pedido ficou em {valor_c4} R$, dirija-se ao caixa para efetuar o pagamento")
            escolha = True 
    
    # Creme
    elif  opcao == 2:
        print("O sabor de Creme está saindo por 5 R$ uma bola, gostaria de quantas bolas de sorvete?")
        quer = int(input("[1] - 1 Bola\n[2] - 2 Bolas\n[3] - 3 Bolas\n[4] - 4 ou mais bolas:"))
        if quer == 1:
            valor_cr1 = quantia_casquinhas * 5 
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Creme com {quer} bola")
            print ( f" seu pedido ficou em {valor_cr1} R$, dirija-se ao caixa para efetuar o pagamento")
        
        elif quer == 2:
             valor_cr2 = quantia_casquinhas * 10 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Creme com {quer} bolas")
             print ( f" seu pedido ficou em {valor_cr2} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 3:
             valor_cr3 = quantia_casquinhas * 15 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Creme com {quer} bolas")
             print ( f" seu pedido ficou em {valor_cr3} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 4:
            quantidade_de_bolas_cr = int( input("Quantas bolas serão?  "))
            preso_da_escolha_4_cr = quantidade_de_bolas_cr * 5 
            valor_cr4 = preso_da_escolha_4_cr * quantia_casquinhas
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Creme com {quantidade_de_bolas_cr} bolas")
            print ( f" seu pedido ficou em {valor_cr4} R$, dirija-se ao caixa para efetuar o pagamento")
            escolha = True 
    
    #Morango
    elif  opcao == 3:
        print("O sabor de Morango está saindo por 5 R$ uma bola, gostaria de quantas bolas de sorvete?")
        quer = int(input("[1] - 1 Bola\n[2] - 2 Bolas\n[3] - 3 Bolas\n[4] - 4 ou mais bolas:"))
        if quer == 1:
            valor_m1 = quantia_casquinhas * 5 
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Morango com {quer} bola")
            print ( f" seu pedido ficou em {valor_m1} R$, dirija-se ao caixa para efetuar o pagamento")
        
        elif quer == 2:
             valor_m2 = quantia_casquinhas * 10 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Morango com {quer} bolas")
             print ( f" seu pedido ficou em {valor_m2} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 3:
             valor_m3 = quantia_casquinhas * 15 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Morango com {quer} bolas")
             print ( f" seu pedido ficou em {valor_m3} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 4:
            quantidade_de_bolas_m = int( input("Quantas bolas serão?  "))
            preso_da_escolha_4_m = quantidade_de_bolas_m * 5 
            valor_m4 = preso_da_escolha_4_m * quantia_casquinhas
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Morango com {quantidade_de_bolas_m} bolas")
            print ( f" seu pedido ficou em {valor_m4} R$, dirija-se ao caixa para efetuar o pagamento")
            escolha = True 
            
    
    #Flocos
    elif  opcao == 4:
        print("O sabor de Flocos está saindo por 5 R$ uma bola, gostaria de quantas bolas de sorvete?")
        quer = int(input("[1] - 1 Bola\n[2] - 2 Bolas\n[3] - 3 Bolas\n[4] - 4 ou mais bolas:"))
        if quer == 1:
            valor_f1 = quantia_casquinhas * 5 
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Flocos com {quer} bola")
            print ( f" seu pedido ficou em {valor_f1} R$, dirija-se ao caixa para efetuar o pagamento")
        
        elif quer == 2:
             valor_f2 = quantia_casquinhas * 10 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Flocos com {quer} bolas")
             print ( f" seu pedido ficou em {valor_f2} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 3:
             valor_f3 = quantia_casquinhas * 15 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Flocos com {quer} bolas")
             print ( f" seu pedido ficou em {valor_f3} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 4:
            quantidade_de_bolas_f = int( input("Quantas bolas serão?  "))
            preso_da_escolha_4_f = quantidade_de_bolas_f * 5 
            valor_f4 = preso_da_escolha_4_f * quantia_casquinhas
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de chocolate com {quantidade_de_bolas_f} bolas")
            print ( f" seu pedido ficou em {valor_f4} R$, dirija-se ao caixa para efetuar o pagamento")
            escolha = True 
            
    
    #Maracuja
    elif  opcao == 5:
        print("O sabor de Maracuja está saindo por 5 R$ uma bola, gostaria de quantas bolas de sorvete?")
        quer = int(input("[1] - 1 Bola\n[2] - 2 Bolas\n[3] - 3 Bolas\n[4] - 4 ou mais bolas:"))
        if quer == 1:
            valor_ma1 = quantia_casquinhas * 5 
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Maracuja com {quer} bola")
            print ( f" seu pedido ficou em {valor_ma1} R$, dirija-se ao caixa para efetuar o pagamento")
        
        elif quer == 2:
             valor_ma2 = quantia_casquinhas * 10 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Maracuja com {quer} bolas")
             print ( f" seu pedido ficou em {valor_ma2} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 3:
             valor_ma3 = quantia_casquinhas * 15 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Maracuja com {quer} bolas")
             print ( f" seu pedido ficou em {valor_ma3} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 4:
            quantidade_de_bolas_ma = int( input("Quantas bolas serão?  "))
            preso_da_escolha_4_ma = quantidade_de_bolas_ma * 5 
            valor_ma4 = preso_da_escolha_4_ma * quantia_casquinhas
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Maracuja com {quantidade_de_bolas_cr} bolas")
            print ( f" seu pedido ficou em {valor_ma4} R$, dirija-se ao caixa para efetuar o pagamento")
            escolha = True 
            
    #Chocomenta
    elif  opcao == 6:
        print("O sabor de Chocomenta está saindo por 5 R$ uma bola, gostaria de quantas bolas de sorvete?")
        quer = int(input("[1] - 1 Bola\n[2] - 2 Bolas\n[3] - 3 Bolas\n[4] - 4 ou mais bolas:"))
        if quer == 1:
            valor_cm1 = quantia_casquinhas * 5 
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Chocomenta com {quer} bola")
            print ( f" seu pedido ficou em {valor_cm1} R$, dirija-se ao caixa para efetuar o pagamento")
        
        elif quer == 2:
             valor_cm2 = quantia_casquinhas * 10 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Chocomenta com {quer} bolas")
             print ( f" seu pedido ficou em {valor_cm2} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 3:
             valor_cm3 = quantia_casquinhas * 15 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Chocomenta com {quer} bolas")
             print ( f" seu pedido ficou em {valor_cM3} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 4:
            quantidade_de_bolas_cM = int( input("Quantas bolas serão?  "))
            preso_da_escolha_4_cM = quantidade_de_bolas_cM * 5 
            valor_cM4 = preso_da_escolha_4_cM * quantia_casquinhas
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de Chocomenta com {quantidade_de_bolas_cM} bolas")
            print ( f" seu pedido ficou em {valor_cM4} R$, dirija-se ao caixa para efetuar o pagamento")
            escolha = True 
            
    #Personalisado
    elif  opcao == 7:
        sabor_novo = str(input("Qual sabor esta procurando?"))
        print(f"O sabor de {sabor_novo} está saindo por 10 R$ uma bola, gostaria de quantas bolas de sorvete?")
        quer = int(input("[1] - 1 Bola\n[2] - 2 Bolas\n[3] - 3 Bolas\n[4] - 4 ou mais bolas:"))
        if quer == 1:
            valor_p1 = quantia_casquinhas * 10 
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de {sabor_novo} com {quer} bola")
            print ( f" seu pedido ficou em {valor_pe1} R$, dirija-se ao caixa para efetuar o pagamento")
        
        elif quer == 2:
             valor_pe2 = quantia_casquinhas * 20 
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de {sabor_novo} com {quer} bolas")
             print ( f" seu pedido ficou em {valor_pe2} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 3:
             valor_pe3 = quantia_casquinhas * 30
             print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de {sabor_novo} com {quer} bolas")
             print ( f" seu pedido ficou em {valor_pe3} R$, dirija-se ao caixa para efetuar o pagamento")
            
        elif quer == 4:
            quantidade_de_bolas_pe = int( input("Quantas bolas serão?  "))
            preso_da_escolha_4_pe = quantidade_de_bolas_pe * 10 
            valor_pe4 = preso_da_escolha_4_pe * quantia_casquinhas
            print ( f"Seu pedido foi {quantia_casquinhas} casquinhas de {sabor_novo} com {quantidade_de_bolas_pe} bolas")
            print ( f" seu pedido ficou em {valor_pe4} R$, dirija-se ao caixa para efetuar o pagamento")
            escolha = True 
            
            
    
            