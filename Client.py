#!/usr/bin/env python

import socket, threading, Crypt

class Client():
    def __init__(self):
        # Size of recieving buffer
        self.bufferLength = 1024
    def __call__(self):
        return self
    
    def RecieveData(self, s, ):
        try:
            D = Crypt.Crypt()
            key = self.key
            
            # Get Server Message (Unencrypted)
            print s.recv(self.bufferLength)
            
            while True:
                recieved = s.recv(self.bufferLength)
                print D.Decrypt(recieved, key)
        except Exception, e:
            #print e
            pass
    def SendData(self, s, ):
        try:
            E = Crypt.Crypt()
            key = self.key
            
            nick = "<Default> "
            
            while True:
                message = raw_input("")
                if(message.find("/nick") >= 0):
                    # Change nickname
                    new_nick = message.replace("/nick ", "")
                    if(new_nick.lower == "server"):
                        print "[--] Cannot Change Nick To Nick Of Server"
                    else:
                        nick = "<" + new_nick + "> "
                        print "[+] Nickname Changed To: %s" % nick
                elif(message.find("/clear") >= 0):
                    # Clears The Screen
                    print '\n' * 100
                elif(message.find("/help") >= 0):
                    # Display Help Message
                    print ("\n\t\t<--- HELP --->\n" +
                    "/nick [new nickname]\tChange Nick Name\n" +
                    "/clear\t\t\tClear The Screen\n" +
                    "/help\t\t\tShow This Message\n" +
                    "/online\t\t\tShow Who Is Online At The Moment\n")
                elif(message.find("/online") >= 0):
                    # Ask server who is online
                    # (Not Encrypted, but Recieved Encrypted)
                    s.send("Online?")
                else:
                    # Encrypt And Send Data
                    data = E.Encrypt((nick + message), key)
                    s.send(data)
        except Exception, e:
            #print e
            pass
    
    def connectToServer(self, IP, port, key):
        try:
            self.key = key
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, port))
            
            threading.Thread(target=self.RecieveData, args=(s, )).start()
            threading.Thread(target=self.SendData, args=(s, )).start()
            
        except KeyboardInterrupt:
            s.close()
            print "[*] Closed Connection To Server!"
        except Exception, e:
            print e
        return
