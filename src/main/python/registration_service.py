

class Registrant:
    def __init__(self, first_name, last_name, age, state):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.state = state


class RegistrationService:
    def __init__(self, db):
        self.db = db

    def insert(self, registrant):
        try:
            cursor = self.db.cursor()
        except:
            self.db.close()
            raise Exception("Unable to get cursor")

        try:
            cursor.execute("INSERT INTO REGISTRANT VALUES ('%s', '%s', %d, '%s')" %
                           (registrant.first_name, registrant.last_name, registrant.age, registrant.state))
            self.db.commit()
        except:
            self.db.rollback()

        self.db.close()
