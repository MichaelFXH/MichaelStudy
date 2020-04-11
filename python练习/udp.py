import socket
import  threading

class ChatServerUdp:
    def __init__(self,ip,port):
        self.sock=socket();
        self.addr=(ip,port)
        self.event=threading.Event

    def start(self):
        self.sock.bind(self.addr)
        threading.Thread(name="receive",target=self.ReceiveData,args=()).start()

    def stop(self):
        self.sock.close()

    def ReceiveData(self):
        data,clientaddr=self.sock.recvfrom(1024)
        msg="ack {}".format(data.decode())
        self.sock.sendTo(msg.encode(),clientaddr)

    def sendData(self):
        pass

cs=ChatServerUdp("127.0.01","9888")
cs.start()