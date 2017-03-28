#!/Applications/anaconda/envs/Python3/bin

import socket

def main():
    '''Example Creating a Simple Client Using the socket Module'''

    HOST = '127.0.0.1'
    PORT = 50002
    incomingMessage = ''
    outgoingMessage = ''

    # s is socket object for IPv4, TCP
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while(outgoingMessage != 'EXIT'):
        outgoingMessage = input('Reply (type EXIT to esc): ')
        s.send(outgoingMessage.encode('utf-8'))
        incomingMessage = s.recv(1024).decode('utf-8')
        if (incomingMessage == 'EXIT'):
            print('The server has chosen to exit. Goodbye.')
            break
        print(incomingMessage)

    s.close()


if __name__ == '__main__':
    main()

# Run simpleServer.py first, then run simpleClient.py in separate terminal window
