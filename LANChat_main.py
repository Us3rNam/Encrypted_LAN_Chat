#!/usr/bin/env python

def main():
    try:
        # Key Used In Encryption
        # This key needs to be the same on all clients for the to recieve messages
        key = "79vb&(%FVB7v68%V^&*IH%C&(ov"
        
        print ("1. Run A Server\n" +
               "2. Connect To A Server")
        opt = raw_input("> ")
        
        if(opt == '2'):
            serverIP = raw_input("Server's IP:\n> ")
            port = raw_input("Server's Port:\n> ")
            
            # Clears The Screen
            print '\n'*100
            
            import Client
            C = Client.Client()
            C.connectToServer(serverIP, int(port), key)
        elif(opt == '1'):
            import Server
            S = Server.Server()
            port = raw_input("Port To Run On:\n> ")
            
            # Clears The Screen
            print '\n'*100
            
            S.startListener("", int(port), key)
        else:
            print '[*] Unknown Command Exiting'
            raw_input("Press [ENTER] To Exit")
    except Exception, e:
        #print e
        pass

if __name__ == "__main__":
    main()
