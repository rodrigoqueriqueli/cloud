# -*- coding: utf-8 -*-

#import
from cloud import Servers


Ttask = 4
Umax = 2

#the run simulation function
def runSimulation(fileInputName, Ttask, Umax):
    
    ticks = 0
    
    #open files
    #f = open("example.txt", "r")
    fin = open(fileInputName, "r")
    fout = open("output.txt", "w")
    
    #instanciate servers
    servers = Servers(Umax, Ttask)
    
    #loop reading file input
    for usersPerLine in fin:
        
        
        #get data and cast
        usersPerLine = int(usersPerLine)
        
        if (usersPerLine != 0):
            
            #increment tick
            servers.incrementTicks()
            
            for user in range(usersPerLine):
                servers.addUser()
                
            #print
            #servers.printServers()
            
        else:
            #increment tick
            servers.incrementTicks()
            
            #print
            #servers.printServers()
        
        #write the output line
        fout.write(str(servers.printServersForOutput())+"\n")
        
        #increment tick
        ticks += 1
    
    #close files
    fin.close()
    fout.close()

    #print the costs
    servers.printCosts()
    
#------------------------------------------------------------------------
    
#RUNNING
#runSimulation("example.txt", 4, 2)
runSimulation("input.txt", Ttask, Umax)
#runSimulation("input2 (1).txt", Ttask, Umax)