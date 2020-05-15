#import
from cloud import Servers


Ttask = 0
Umax = 0

#the run simulation function
def runSimulation(fileInputName, Ttask, Umax):
    
    ticks = 0
    
    #abrir arquivos
    #f = open("example.txt", "r")
    fin = open(fileInputName, "r")
    fout = open("output.txt", "w")

    # abrindo arquivo pra extrair parametros
    parameters = fin.read() 
    Ttask = int(parameters[0])
    Umax =  int(parameters[2])
    

    fin.close()

    fin = open(fileInputName, "r")
       
    #instanciando servers
    servers = Servers(Umax, Ttask)
    
    #lendo arquivo de input
    for index, usersPerLine in enumerate(fin):
    
        #obtendo dados
        usersPerLine = int(usersPerLine) if index > 1 else None
        
        
        if (usersPerLine != 0) and (usersPerLine != None):
            
            #incrementando ticks
            servers.incrementTicks()
            
            for user in range(usersPerLine):
                servers.addUser()
                
            #print
            #servers.printServers()
            
        elif(usersPerLine == 0) and (usersPerLine != None):
            #incrementando ticks
            servers.incrementTicks()
            
        #imprimir output
        if (servers.printServersForOutput() != '0'):
            fout.write(str(servers.printServersForOutput())+"\n")
        #incrementar tick
            ticks += 1
    
    #fechar arquivos
    fin.close()
    fout.write(str(servers.costs)+"\n")
    fout.close()

    
#------------------------------------------------------------------------

runSimulation("input.txt", Ttask, Umax)
