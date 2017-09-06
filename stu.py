class student:
    def __init__(self, name, surname, roll):
        self.name = name
        self.surname = surname
        self.roll = roll

    def full_name(self):
        return ('{} {}'.format(self.name, self.surname))
    def email_id(self):
        return ('{}.{}@gmail.com'.format(self.name, self.surname))
    def roll(self):
        return (self.roll+1)
