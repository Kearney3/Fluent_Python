from Person import Person, Manager

def init_db():
    import shelve
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)
    db = shelve.open('person.db')
    for obj in (bob, sue, tom):
        db[obj.name] = obj
    db.close()

def display():
    import shelve
    db = shelve.open('person.db')
    for key in db:
        print(key, '=>', db[key])


def update():
    import shelve
    db = shelve.open('person.db')
    for key in db:
        person = db[key]
        person.giveRaise(0.10)
        db[key] = person
    db.close()



if __name__ == '__main__':
    display()
    update()
    print('After update')
    display()



