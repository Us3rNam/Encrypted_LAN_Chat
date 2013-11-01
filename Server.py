#!/usr/bin/env python

import socket, threading, time
import Crypt

class Server():
    def __init__(self):
        # Server message
        self.serverMessage = (
            "Welcome To _UserName_'s Server" +
            "")
        # This key needs to be the same on all clients for the to recieve messages
        self.key = "afsd67viauyh3wrf8e7boyiuf67"
        
        # List of connected users
        self.connections = []
        
        # Declare basic socket stuff
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    def __call__(self):
        return self
    
    def broadcastToAll(self):
        try:
            E = Crypt.Crypt()
            
            print "\nType messages below to be broadcasted as the server.\n----------------------------------------------------\n"
            
            while True:
                message = raw_input("")
                message = "<SERVER> " + message
                # Encrypt Message
                message = E.Encrypt(message, self.key)
                # Send To All Connected Clients
                self.dispense(message)
        except Exception, e:
            print e
            pass
    
    def handleClient(self,client):
        try:
            # Send Server Message
            client.send((self.serverMessage[:1024]))
            E = Crypt.Crypt()
            
            while True:
                data = client.recv(1024)
                if(data == "Online?"):
                    response = "[*] Users Online\n"
                    for clients in self.connections:
                        response += "\t" + clients.getpeername()[0] + "\n"
                    message = E.Encrypt(response, self.key)
                    client.send(message)
                elif data:
                    threading.Thread(target=self.dispense, args=(data,)).start()
                else:
                    pass
        except socket.error:
            # Remove Clients From List If An Error Occurs
            self.connections.remove(client)
            client.close()
        except Exception, e:
            #print e
            pass

    def dispense(self,data):
        for clients in self.connections:
            try:
                clients.send(data)
            except Exception, e:
                #print e
                pass
    
    def startListener(self, IP, port, key):
        self.key = key
        
        self.server.bind((IP, port))
        self.server.listen(5)
        print "Started Server On: %s : %i" % (IP, port)
        try:
            threading.Thread(target=self.broadcastToAll, args=()).start()
            while True:
                try:
                    client, addr = self.server.accept()
                    self.connections.append(client)
                    print "Connection From %s : %i" % (client.getpeername()[0], client.getpeername()[1])
                    threading.Thread(target=self.handleClient, args=(client,)).start()
                except Exception, e:
                    #print e
                    pass
            self.server.close()
        except Exception, e:
            #print e
            pass
