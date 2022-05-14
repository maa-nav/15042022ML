import sqlite3
from class_demo import Car

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE car(brand text,engine integer,price real)''')

car1 = Car('Maruti',1000,500)
car2 = Car('Maruti',2000,100)
car3 = Car('tata',1000,100)
car4 = Car('tata',2000,500)

######## 3 ways to Insert #######

##c.execute("INSERT INTO car VALUES('Maruti800',1500,500)")
##c.execute("INSERT INTO car VALUES(?,?,?)",(car4.brand,car4.engine,car4.price))
##
##c.execute(f"INSERT INTO car VALUES('{car1.brand}',{car1.engine},{car1.price})")
##
##c.execute("INSERT INTO car VALUES (?,?,?)",(car2.brand,car2.engine,car2.price))
##
##c.execute("INSERT INTO car VALUES (:brand,:engine,:price)",
##                                    {'brand':car3.brand,
##                                     'engine':car3.engine,
##                                     'price':car3.price})
##
########### 3 ways to select ###########
##
##c.execute("SELECT * FROM car WHERE engine=? AND brand=?",(2000,'tata'))

##c.execute("SELECT * FROM car WHERE engine=:engine",{'engine':1000})

##print(c.fetchall())
##print(c.fetchmany(1))
##print(c.fetchone())

def insert(car):
    with conn:
        c.execute("INSERT INTO car VALUES (?,?,?)",(car.brand,car.engine,car.price))

def read(num,brand):
    c.execute("SELECT * FROM car WHERE engine=? AND brand=?",(num,brand))
    return c.fetchall()

def update(price):
    with conn:
        c.execute("UPDATE car SET price = :price",{'car':car,'price':price})

def delete(engine,price):
    with conn:
        c.execute("DELETE from car WHERE engine<=:engine AND price<=:price"
                  ,{'engine':engine,'price':price})
     
insert(car1)
insert(car2)
insert(car3)
insert(car4)

print(read(1000,'tata'))

update(car2,1000)

c.execute("SELECT * FROM car")
print(c.fetchall())

delete(1000,1000)
c.execute("SELECT * FROM car")
print(c.fetchall())




conn.close()
