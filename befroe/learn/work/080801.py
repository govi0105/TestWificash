import socket
class TalkClient:
    def __init__(self):
        pass
    def send_message(self):
        s =socket.socket()
        s.connect(('35.154.129.44',8888))
        s.send('a323232132323')
        s.close()
if __name__ == '__main__':
    print('nihao')
