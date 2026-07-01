
# get => list
# post=>create
# put=>update
# delete=>delete
# retrieve=>detail

from mysql.connector import connect

class Expenses:

    def __init__(self):
        
        self.connection = connect(
            user="root",
            host="localhost",
            password="Password@123",
            database ="fundwise_db"
        )

    def get(self):

        self.cursor = self.connection.cursor()

        query = "select * from transaction"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        print(records)

    def post(self,**kwargs):#{'title': 'school monthly fee', 'amount': -2500, 'owner': 'hari', 'category': 'Housing', 'payment_method': 'upi'}

        print(kwargs)
        self.cursor = self.connection.cursor()

        query = "insert into transaction (title,amount,owner,category,payment_method) values (%s,%s,%s,%s,%s)"

        values=[v for v in kwargs.values()]

        self.cursor.execute(query,values)

        self.connection.commit()

        print("record inserted")

    def retrieve(self,id=None):

        self.cursor = self.connection.cursor()

        query = "select * from transaction where id = %s"

        values=(id,)

        self.cursor.execute(query,values)

        record = self.cursor.fetchone()

        print(record)


    def delete(self,id=None):

        query = "delete from transaction where id = %s"

        values = (id,)

        self.cursor = self.connection.cursor()

        self.cursor.execute(query,values)

        self.connection.commit()

        print("recoerd deleted")

    
    def put(self,id=None,**kwargs):

        self.cursor = self.connection.cursor()

        place_holder = ""

        for k in kwargs.keys():

            place_holder += k+"=%s,"

        place_holder = place_holder.rstrip(",")

        query = f"update transaction set {place_holder} where id = %s"

        values = [v for v in kwargs.values()]

        values.append(id)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("record inserted")
        



        

exp_instance = Expenses()


# exp_instance.put(id=2,amount=4000,owner="vipin")
# exp_instance.put(id=1,amount=4500)
# exp_instance.put(id=2,title="KSEB",amount=7000)

exp_instance.retrieve(id=2)


# exp_instance.post(title="lic",amount=-3300,owner="hari",category="Housing",payment_method="upi")

# exp_instance.get()


# exp_instance.retrieve(id=2)

# exp_instance.delete(id=1)
