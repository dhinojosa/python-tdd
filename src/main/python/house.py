class House:
    def __init__(self, kitchen, bedroom):
        self.kitchen = kitchen
        self.bedroom = bedroom

    def bake_cookies(self):
        self.kitchen.set_oven(350)
        self.kitchen.set_oven(150)
        self.kitchen.set_oven(650)


class Kitchen:
    def __init__(self):
        pass

    def set_oven(self, temp):
        print "connecting to a real oven"
        print "there's a lot going on here"
        print "raising temp to " + temp
