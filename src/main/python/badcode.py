import time


class MyService:
    def __init__(self):
        pass

    def method3(self):
        self.method_support(self, lambda s: ServerInstance.find(s))

    def method_support(self, lm):
        resource = lm("120.0.4.1:8080/services/accounts")
        return resource["message"]


class ServerInstance:
    def __init__(self):
        pass

    @staticmethod
    def find(string):
        # I dont want this to run
        time.sleep(10)
        return {"message": "hooray"}
