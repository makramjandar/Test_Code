#!/Applications/anaconda/envs/Python3/bin

import socket

def main():
    '''Example Creating a Simple Cliend Using the socket Module'''

    HOST = '127.0.0.1'
    PORT = 50002

    # s is socket object for IPv4, TCP
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send('Top o the morning to you!'.encode('utf-8'))
    data = s.recv(1024)
    print(data.decode('utf-8'))

    s.close()


if __name__ == '__main__':
    main()

# Run simpleServer.py first, then run simpleClient.py in separate terminal window
