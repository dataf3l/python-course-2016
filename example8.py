class Duck:
    def talk(self):
        print "quack"


class Truck:
    def talk(self):
        print "broom"


def main():
    x = Truck()
    y = Duck()
    stuff = [x,y,1,2,3]
    for item in stuff:
        #if type(item).__name__ == 'Duck'):
        if hasattr(item, 'talk'):
            item.talk()
        else:
            print(item," has no talk()")


if __name__ == "__main__":
    main()
