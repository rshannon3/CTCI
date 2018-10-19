"""
7.7 Chat Server: Explain how you would design a chat server. In particular, provide details about the
various backend components, classes, and methods. What would be the hardest problems to solve?
Hints: #213, #245, #271
"""


#Modified version of https://www.geeksforgeeks.org/simple-chat-room-using-python/
# Python program to implement server side of chat room.
import socket
import select
import sys
from thread import *

class server:
	def clientthread(conn, addr):

	    # sends a message to the client whose user object is conn
	    conn.send("Welcome to this chatroom!")

	    while True:
	            try:
	                message = conn.recv(2048)
	                if message:

	                    """prints the message and address of the
	                    user who just sent the message on the server
	                    terminal"""
	                    print "<" + addr[0] + "> " + message

	                    # Calls broadcast function to send message to all
	                    message_to_send = "<" + addr[0] + "> " + message
	                    broadcast(message_to_send, conn)

	                else:
	                    """message may have no content if the connection
	                    is broken, in this case we remove the connection"""
	                    remove(conn)

	            except:
	                continue

	"""Using the below function, we broadcast the message to all
	clients who's object is not the same as the one sending
	the message """
	def broadcast(message, connection):
	    for clients in list_of_clients:
	        if clients!=connection:
	            try:
	                clients.send(message)
	            except:
	                clients.close()

	                # if the link is broken, we remove the client
	                remove(clients)

	"""The following function simply removes the object
	from the list that was created at the beginning of
	the program"""
	def remove(connection):
	    if connection in list_of_clients:
	        list_of_clients.remove(connection)

	def run(ip, port, server, MAX_CONNECTIONS):
		server.bind((ip, port))
		#Listens for up to max connections
		server.listen(MAX_CONNECTIONS)
		client_list = []

		while True:
			"""Accepts a connection request and stores two parameters,
			conn which is a socket object for that user, and addr
			which contains the IP address of the client that just
			connected"""
			conn, addr = server.accept()
			"""Maintains a list of clients for ease of broadcasting
			a message to all available people in the chatroom"""
			client_list.append(conn)
			# prints the address of the user that just connected
			print(addr[0] + " connected")
			# creates and individual thread for every user
			# that connects
			start_new_thread(clientthread,(conn,addr))
		conn.close()
		server.close()


##### Client
class Client:
	def run(ip, port, server):
		server.connect((IP_address, Port))

		while True:

		    # maintains a list of possible input streams
		    sockets_list = [sys.stdin, server]

		    """ There are two possible input situations. Either the
		    user wants to give  manual input to send to other people,
		    or the server is sending a message  to be printed on the
		    screen. Select returns from sockets_list, the stream that
		    is reader for input. So for example, if the server wants
		    to send a message, then the if condition will hold true
		    below.If the user wants to send a message, the else
		    condition will evaluate as true"""
		    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

		    for socks in read_sockets:
		        if socks == server:
		            message = socks.recv(2048)
		            print message
		        else:
		            message = sys.stdin.readline()
		            server.send(message)
		            sys.stdout.write("<You>")
		            sys.stdout.write(message)
		            sys.stdout.flush()
		server.close()


##### End Client


if len(sys.argv) != 4:
	print("Usage python mode ip port")
	exit()
mode = str(sys.argv[1])
ip = str(sys.argv[2]) 
port = int(sys.argv[3])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if mode == 'server':
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	MAX_CONNECTIONS = 10
	server = Server()
	server.run(ip, port, server, MAX_CONNECTIONS)


if mode == 'client':
	client = Client()
	client.run(ip, port, server)
