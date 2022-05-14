import sqlite3
from class_demo import Car

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE car(
            id integer,
            brand text,
            engine integer,
            price real,
            PRIMARY KEY(id))
            ''')

c.execute('''CREATE TABLE sales(
            id integer,
            sales_person text,
            sales_price real,
            profit real,
            FOREIGN KEY(id) REFERENCES car(id)
            )''')

car1 = Car('Maruti',1000,500)
car2 = Car('Maruti',2000,100)
car3 = Car('tata',1000,100)
car4 = Car('tata',2000,500)
car5 = Car('Audi',1000,100)
car6 = Car('Audi',2000,500)

sale1= ('Rahul',600,100)
sale2= ('Ravi',500,500)
sale3= ('Yudi',900,800)
sale4= ('Yash',700,200)


car_ = [car1,car2,car3,car4,car5,car6]
sale_ = [sale1,sale2,sale3,sale4]


def insert(i,n):
    with conn:
        c.execute("INSERT INTO car VALUES (:i,:brand,:engine,:price)",
                        {'i':i,'brand':n.brand,'engine':n.engine,'price':n.price})

def inserts(i,sale):
    with conn:
        c.execute("INSERT INTO sales VALUES (?,?,?,?)",(i,sale[0],sale[1],sale[2]))

def read(x,y):
    c.execute(f"SELECT * FROM car WHERE {x}=:x ORDER by engine ASC LIMIT(2)",{'x':y})
    return c.fetchall()

def update(w,x,y,z):
    with conn:
        c.execute(f"UPDATE car SET {y}=:y WHERE {w}=:w",{'y':z,'w':x})
    return 'Updated...'

def delete(engine,price):
    with conn:
        c.execute("DELETE from car WHERE engine<=:engine AND price<=:price"
                  ,{'engine':engine,'price':price})
     
for i,n in enumerate(car_):
    insert(i+1,n)
for i,sale in enumerate(sale_):
    inserts(i+1,sale)


##c.execute('''SELECT * FROM sales LEFT JOIN car USING(id)
##          UNION ALL
##          SELECT * FROM car LEFT JOIN sales USING(id)''')
##
##r = c.fetchall()
##for i in r:
##    print(i)

r = (c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())

##c.execute("DROP table sales")

##r1 = (c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())

##c.execute("TRUNCATE TABLE car").fetchall()  # DOES NOT EXIST IN SQLITE3


conn.close()
