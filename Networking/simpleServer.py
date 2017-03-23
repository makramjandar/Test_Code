#!/Applications/anaconda/envs/Python3/bin

import socket

def main():
    '''Example Creating a Simple Server Using the socket Module'''

    HOST = ''
    PORT = 50002

    # s is socket object for IPv4, TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    connection, address = s.accept()
    message = connection.recv(1024)
    print(message.decode('utf-8'))
    connection.send('A good day to you, my friend!'.encode('utf-8'))

    connection.close()
    s.close()


if __name__ == '__main__':
    main()

# Run simpleServer.py first, run simpleClient.py in separate terminal window
