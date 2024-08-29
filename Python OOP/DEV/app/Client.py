class Client:
    def __init__(self, name, telephone):
        self._name = name
        self._telephone = telephone

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getTelephone(self):
        return self._telephone

    def setTelephone(self, telephone):
        self._telephone = telephone