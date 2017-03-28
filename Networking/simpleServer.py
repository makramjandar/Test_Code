#!/Applications/anaconda/envs/Python3/bin

import socket

def main():
    '''Example Creating a Simple Server Using the socket Module'''

    HOST = ''
    PORT = 50002
    incomingMessage = ''
    outgoingMessage = ''

    # s is socket object for IPv4, TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    connection, address = s.accept()

    while(outgoingMessage != 'EXIT'):
        incomingMessage = connection.recv(1024).decode('utf-8')
        if (incomingMessage == 'EXIT'):
            print('The client wishes to exit. Farewell, sweet server.')
            connection.send('Epic chat, until next time!'.encode('utf-8'))
            break
        print(incomingMessage)
        outgoingMessage = input('Reply (type EXIT to esc): ')
        connection.send(outgoingMessage.encode('utf-8'))

    connection.close()
    s.close()


if __name__ == '__main__':
    main()

# Run simpleServer.py first, run simpleClient.py in separate terminal window
