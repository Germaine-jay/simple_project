# a programme that ask for the product you want, the quantity and will give the amount left in store 

'''class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        
    def my_list(want):
        product_list =  [{'name':'apple', 'amount':200, 'price':33},
           {'name':'carrot', 'amount':200, 'price':33},
           {'name':'orange', 'amount':200, 'price':33},
           {'name':'banana', 'amount':200, 'price':33}]
        for i in range(len(product_list)):
            if want == product_list[i]['name']:
                return product_list[i]['name'], product_list[i]['amount'], product_list[i]['price']
        
    def get_price(self, number_to_be_bought):
        if number_to_be_bought < 10:
            discount=0
            price = (100 - discount)/100 * self.price
            return price * number_to_be_bought
        elif 10 >= number_to_be_bought <= 99:
            discount=10
            price = (100 - discount)/ 100 * self.price
            return price * number_to_be_bought
        else :
            discount =20
            price = (100 - discount)/100 * self.price
            return price * number_to_be_bought
        
    def make_purchase(self, quantity):
       self.amount = self.amount - quantity
       return self.amount
  
want=input('enter product you want:')
print(Product.my_list(want))
fruits = Product((Product.my_list(want)[0]), Product.my_list(want)[1], Product.my_list(want)[2])

q1 = eval(input('enter quantity:'))
print('cost of ',q1, (Product.my_list(want)[0]),'is', '{:2d}'.format(fruits.get_price(q1)))
print('remaining stock:', fruits.make_purchase(q1)),'\n'

q2 = eval(input('enter quantity:'))
print('cost of ', q2, (Product.my_list(want)[0]),'is', fruits.get_price(q2))
print('remaining stock:', fruits.make_purchase(q2))'''



# a programme that ask for the current password and if incorrect, adds it to the list of passwords

'''class Password_manager:
    old_password = ['suarez', 'baddest', 'apple', 'orange']
    
    def __init__(self, password):
        self.password = password
        
    def get_password(self):
        
        for i in Password_manager.old_password:
            if self.password == Password_manager.old_password[-1]:
                self.password = self.password
            return self.password

    def set_password(self):
        if self.password != Password_manager.old_password[-1]:
            Password_manager.old_password.append(self.password)
            return self.password
        else:
            print ('logged in')
            return self.password
               
login = Password_manager(input('enter password:'))
print(Password_manager.set_password(login))
print(Password_manager.old_password)    
print(login.get_password())'''


# a prog that converts a number in seconds to minutes and hour
'''class Time:
    def __init__(self, minutes):
        self.minutes = minutes
    def convert_to_minutes(self):
        print( self.minutes//60,':',self.minutes%60)
        
    def convert_to_hours(self):
        hours, mini, sec = (self.minutes//3600), (self.minutes%3600)//60,(self.minutes%3600)%60
        print(hours,':',mini,':',sec)

number = Time(eval(input('enter amount of seconds:')))
Time.convert_to_minutes(number)
Time.convert_to_hours(number)'''


# another alternative to the previous programme
'''class Time:
    def __init__(self, minutes):
        self.minutes = minutes
    def convert_to_minutes(self):
        minute = float(self.minutes/60)
        mini =  int(self.minutes/60)
        seconds = int((minute - int(minute))*60)
        calc = str(mini) + ':' + str(seconds)
        return calc
    def convert_to_hours(self):
        hours, mini = (self.minutes/3600), int(self.minutes/3600)
        minute, sec = ((hours - mini)*60), int((hours - mini)*60)
        seconds = (minute - sec)*60
        hour,minute,seconds = int(hours), int(minute), int(seconds)
        self.seconds = str(hour) + ':' + str(minute) + ':' + str(seconds)
        return self.seconds

number = Time(eval(input('enter amount of seconds:')))
print(Time.convert_to_minutes(number))
print(Time.convert_to_hours(number))
print(number.convert_to_minutes())'''