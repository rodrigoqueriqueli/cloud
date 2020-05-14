# -*- coding: utf-8 -*-

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
    users = fin.read()

    users = users[::2]  
    Ttask = int(users[0])
    Umax =  int(users[1]) 
    # import ipdb; ipdb.set_trace() 

    #instanciate servers
    servers = Servers(Umax, Ttask)
    
    #loop reading file input
    for index, usersPerLine in enumerate(users):
    
        
        
        #get data and cast
        usersPerLine = int(usersPerLine)
        


        if (usersPerLine != 0) and (index>=2):
            
            #increment tick
            servers.incrementTicks()
            
            for user in range(usersPerLine):
                servers.addUser()
                
            #print
            #servers.printServers()
            
        elif(usersPerLine == 0) and (index>=2):
            #increment tick
            servers.incrementTicks()
            
            #print
            #servers.printServers()
        
        #imprimir output
        fout.write(str(servers.printServersForOutput())+"\n")
        
        #increment tick
        ticks += 1
    
    #fechar arquivos
    fin.close()
    fout.close()

    #imprimir custo final
    servers.printCosts()
    
#------------------------------------------------------------------------
    
#RUNNING
#runSimulation("example.txt", 4, 2)
runSimulation("input.txt", Ttask, Umax)
#runSimulation("input2 (1).txt", Ttask, Umax)