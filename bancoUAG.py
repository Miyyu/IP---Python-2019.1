import os
import sys

def criar_cliente():
    cpf = str(input("DIGITE SEU CPF: "))
    arq = open(cpf+".txt", "a")
    nome = str(input("Digite seu nome: "))
    arq.write(nome+"\n")
    tel = str(input("Digite seu numero de telefone: "))
    arq.write(tel+"\n")
    arq.close()
    print("Usuário cadastrado com SUCESSO!\n")
    return opcaoPrincipal()

def entrarConta():
    cpf = str(input("Digite seu CPF: "))
    user = verificarUser(cpf+".txt")
    if user == False:
        print ("Usuário não cadastrado")
        return opcaoPrincipal()
    else:
        arq = open(cpf+".txt")
        print("Bem vindo(a)!\n")

    menuSecundario(cpf)


def verificarUser(user):
    return os.path.exists(user)

def transferencia(cpf):
    conta = str(input("Digite o numero da conta que deseja transferir: "))
    existencia = verificarUser(conta+".txt")
    if existencia == False:
        print ("Usuário não existe.")
        return menuSecundario(cpf)
    else:
        arq = open(cpf+".txt", "a")
        arqUser = open(conta+".txt", "a")
        valor = input("Digite o valor que deseja transferir: ")
        arqUser.write("d "+valor+"\n")
        arq.write("t "+valor+"\n")
        arqUser.close()
        arq.close()
        print("Transferencia realizada com SUCESSO!\n")

        

def opcaoPrincipal ():
    print ('Digite a Opcao Desejada\n')
    print ("Digite 0 para cadastrar cliente")
    print ("Digite 1 para entrar na conta")
    print ("Digite 2 para sair")
        
    op = int (input())

    ok = True
    while ok == True:
        if op == 0:
            criar_cliente()
        elif op == 1:
            entrarConta()
        elif op == 2:
            ok = False
            print("VOLTE SEMPRE!")
            sys.exit()
        else:
            print("Opção inválida")

def menuSecundario(cpf):
    ok = True
    while ok == True:
        print("Digite 1 para saque")
        print("Digite 2 para deposito")
        print("Digite 3 para transferencia")
        print("Digite 4 para saldo")
        print("Digite 5 para sair")
        op = int(input())

        if op == 1:
            saque(cpf)
            
        elif op == 2:
            deposito(cpf)

        elif op == 3:
            transferencia(cpf)    
        elif op == 4:
            saldo(cpf)

        elif op == 5:
            ok = False
            return opcaoPrincipal()
        else:
            print("Opção inválida")

def deposito(cpf):
    valor = float(input('digite o valor do deposito: '))
    arquivo = open(cpf+".txt", 'a')
    arquivo.write('d '+str(valor)+'\n')
    print("Deposito realizado com SUCESSO!")
    arquivo.close()


def saque(cpf):
    valor = float(input('digite o valor do saque: '))
    arquivo = open(cpf+'.txt', 'a')
    arquivo.write('s '+str(valor)+'\n')
    print("Saque realizado com SUCESSO!")
    arquivo.close()    

def saldo(cpf):
    arquivo = open(cpf+".txt", 'r')
    saldo = 0
    for linha in arquivo:
        operacao = linha[0]
        valor = str(linha[2:len(linha)-1])
        if operacao == 'd':
            saldo += float(valor)
        elif operacao == 's':
            saldo -= float(valor)
        elif operacao == "t":
            saldo -= float(valor)
    print ("O saldo da conta e de: "+str(saldo)+"\n")
    

op = opcaoPrincipal()


        
