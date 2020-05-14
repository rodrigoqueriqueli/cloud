# -*- coding: utf-8 -*-


class Server:
    
    def __init__(self, id, Umax, Ttmax):
        self.users = []
        self.id= id
        self.Umax = Umax
        self.Ttmax = Ttmax
    #----------------------------------------------------------
    
    
    def addUser(self, id):
        
        #criar usuário
        newUser = User(id)
        
        if (len(self.users) < self.Umax):
            #append
            self.users.append(newUser)
            return True
        else:
            #raise Exception('servidor cheio')
            print('Try to add user '+str(id)+', but the Server id= '+str(self.id)+', The server is full')
            return False

    #----------------------------------------------------------
    
    def incrementTick(self):
        #loop pra incrementar
        for u in self.users:
            u.incrementTicks()
        
        #remover usuários que finalizaram
        self.removeUsersFinished()
    #----------------------------------------------------------
        
    def removeUsersFinished(self):
        #interate the list and get only the users that have ticks less than Ttmax
        newList = [x for x in self.users if x.ticksCount < self.Ttmax]
        self.users = newList
        del(newList)
    #----------------------------------------------------------
    
    
    def printServerUsers(self):
        
        if (len(self.users) == 0):
            print('Serverid = '+str(self.id)+'Nenhum usuário encontrado no servidor')
        else:
            print('------------------------')
            print('Serverid = '+str(self.id))
            for u in self.users:
                u.printUser()
    #----------------------------------------------------------
    
    def getNumberOfUsers(self):
        return len(self.users)
    #----------------------------------------------------------

#------------------------------------------------------------------------  
        
    
#s = Server(1,2,4)

#s.addUser(1)
#s.addUser(2)
#s.addUser(3)

#s.printServerUsers()

# -*- coding: utf-8 -*-


class Servers:
    
    def __init__(self, Umax, Ttmax):
        self.sList = []
        self.Umax = Umax
        self.Ttmax = Ttmax
        self.serverIdCount = 0
        self.userIdCount = 0
        self.costs = 0
        self.serverListPerTick = []
        self.tickCount = 0
    #----------------------------------------------------------
    
    def createServer(self, id):
        #criar servidor
        s = Server(id, self.Umax, self.Ttmax)
        
        #adicionar na lista
        self.sList.append(s)
    #----------------------------------------------------------
    
    def addUser(self):
        #verificar se existe algum outro server
        if (len(self.sList) == 0):
            
            self.serverIdCount += 1
            self.userIdCount += 1
            
            self.createServer(self.serverIdCount)
            
            self.sList[-1].addUser(self.userIdCount)
            
        else:
            tryToAdd = None
            self.userIdCount += 1
            
            for s in self.sList:
                tryToAdd = s.addUser(self.userIdCount)
                
                if (tryToAdd == True):
                    break
            
            if (tryToAdd != True):
                self.serverIdCount += 1
                
                self.createServer(self.serverIdCount)
                
                self.sList[-1].addUser(self.userIdCount)                
    #----------------------------------------------------------
    
    def incrementTicks(self):
        
        self.tickCount += 1
        
        if (len(self.sList) == 0):
            print('Não existem servers pra incrementar')
        else:
            for s in self.sList:
                s.incrementTick()
         
        #incrementar custos
        self.costs += len(self.sList)
        # import ipdb; ipdb.sset_trace()
        self.serverListPerTick.append(len(self.sList))
        
        #loop pra pegar server que nao esta sendo usado
        for s in self.sList:
            newList = [x for x in self.sList if len(x.users) != 0]
            self.sList = newList
            del(newList)
            
        
        
        #print('\n')
        #print('--------------')
        #print('TickCount = '+str(self.tickCount))
        #print('--------------')
    
    def printServers(self):
        if (len(self.sList) == 0):
            print('There are no servers')
        else:
            for s in self.sList:
                s.printServerUsers()
    #----------------------------------------------------------
    
    def printCosts(self):
        print ('Costs = $'+str(self.costs))
        
    
    def printServersForOutput(self):
        
        if (len(self.sList) == 0):
            return "0"
        
        line = ""
        
        for s in self.sList:
            if (line == ""):
                line = str(s.getNumberOfUsers())
            else:
                line = line+","+str(s.getNumberOfUsers())
                
        return line
        
         
#------------------------------------------------------------------------
                

#s = Servers(2, 4)



#print(s.sList)

#1
#3
#0
#1
#0
#1
#0
#0
#0
#0

#s.incrementTicks()
#s.addUser()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.addUser()
#s.addUser()
#s.addUser()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.addUser()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.addUser()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.printCosts()
#
#print(s.ss)
#
#print(sum(s.ss))

# -*- coding: utf-8 -*-

class User:
    
    def __init__(self, id):
        self.id = id
        self.ticksCount = 0
        
    def __str__(self):
        return str(self.id)
    
    def printUser(self):
        print('UserID = '+str(self.id)+', ticks = '+str(self.ticksCount))
        
    def incrementTicks(self):
        self.ticksCount += 1


#------------------------------------------------------------------------