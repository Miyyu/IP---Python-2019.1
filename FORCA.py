palavra = str(input("Digite a palavra: "))
jogo = [] #letras acertadas
vogais = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
for i in range (0,(len(palavra))):
    jogo.append('-') #coloca na lista jogo a quantidade que - quem tem a palavra
    
print("*\n"*35)
print("JOGO DA FORCA\n".center(80))
p = int(input("Digite o nível do jogo:\n[1]FÁCIL\n[2]DIFÍCIL\n¬"))
print(" ")

cont = 0 #contador para o while
LetrasDescorbertas = 0
k = 0

for t in palavra: #coloca um t para rodar pelos indices da variavel palavra
    if t in vogais: #se t que é o indice estiver no dict vogais
        vogais[t] += 1 #a chave que tem passou pelo if recebe +1

if p == 1:
    for y,x in vogais.items(): #y é a chave(indice) do dict enquanto o x é o valor, items pega os dois em ordem
        print("Exitem",x, "letra(s)", y)
    print(" ")
    
    while k < 5:
        for h in jogo:
            print(h, end = " ")        
        
        if LetrasDescorbertas == len(palavra): #se a quantidade de letras foi preenchida, para o programa
            print("**PARABENS!**".center(80))
            break
        elif cont == 0: #se for 0, a pessoa acertou a letra, sendo assim o programa roda
            k -= 1
        else: #caso contrario, a pessoa errou uma letra, add assim mais um para o k do while
            k += 1
               
        b = str(input("Digite uma letra: "))
        print(" ") #printar espaço vazio
        
        for i in range(len(palavra)): #percorrer todo o tamanho da variavel palavra
            if palavra[i] == b: #se o indice da palavra for igual a letra que digitei
                jogo[i] = b #lista jogo muda o - para a letra correspondente de acordo com o indice da palavra que passou do if
                LetrasDescorbertas += 1 
                cont = 0 #deixa o contador com 0 para usar no if de parada
            else:
                cont += 1 #se a letra não for igual add mais um no contador para usar no if de parada
if p == 2:
    while k < 5:
        for h in jogo:
            print(h, end = " ")
                
        if LetrasDescorbertas == len(palavra): #se a quantidade de letras foi preenchida, para o programa
            print("**PARABENS!**".center(80))
            break
        elif cont == 0: #se for 0, a pessoa acertou a letra, sendo assim o programa roda
            k -= 1
        else: #caso contrario, a pessoa errou uma letra, add assim mais um para o k do while
            k += 1
               
        b = str(input("Digite uma letra: "))
        print(" ") #printar espaço vazio
        
        for i in range(len(palavra)): #percorrer todo o tamanho da variavel palavra
            if palavra[i] == b: #se o indice da palavra for igual a letra que digitei
                jogo[i] = b #lista jogo muda o - para a letra correspondente de acordo com o indice da palavra que passou do if
                LetrasDescorbertas += 1 
                cont = 0 #deixa o contador com 0 para usar no if de parada
            else:
                cont += 1 #se a letra não for igual add mais um no contador para usar no if de parada
