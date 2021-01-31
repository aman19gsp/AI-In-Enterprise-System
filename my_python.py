#define class
class fullname:
    fname=""
    lname=""
    def __init__(self, first , last):
        self.fname = first
        self.lname = last
    def display(self):
        print('your name:{}'.format(self.fname + ' ' + self.lname))

#create class object
f = fullname('Aman' , 'Verma')

#show result
f.display()
