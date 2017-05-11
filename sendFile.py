import socket,time
import sys
try:
  s = socket.error,msg:
    print 'Failed to create .error code: ' +str(msg[0])+ ',Error message: '+msg[1]
    sys.exit()
IP = '' #your server ip
PORT = '' #set by yourself
s.connect((IP,PORT))
filePath = sys.argv[1] #file add it's path in your server
try:
  s.sendall(filePath)
except socket.error:
  print 'Send failed'
  sys.exit()
  if "/" in filePath:
    outFile = open(filePath.split("/")[-1],'wb')
  else:
    print 'please Input file and path'
total_data = []
reply = s.recv(1024)
while reply:
  toatl_data.append(reply)
  reply = s.recv(1024)
for out in total_data:
  outFile.write(out)
outFile.close()
s.close()
