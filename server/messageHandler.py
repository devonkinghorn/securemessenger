
class ClientData:
    def __init__(self):
        self.messages = []
        self.key = ''

class MessageHandler:
    def __init__(self):
        self.clients = {}

    def storeMessage(self, receiver, message):
        if not receiver in self.clients:
            self.clients[receiver] = ClientData()
        self.clients[receiver].messages.append(message)

    def getKey(self,name):
        if name in self.clients:
            return self.clients[name].key
        else:
            raise Exception('user not found')

        