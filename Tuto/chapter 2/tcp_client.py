import socket

target_host = "0.0.0.0" #www.google.com
target_port = 9999 #80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send some data
client.send("Hye there! Sup")

#receive some data
response = client.recv(4096)

print response
