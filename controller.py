import pymysql
class Control:
    def __init__(self):
        try:
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='mysqlaqwqer2',
                                 database='reneemontoya')
            self.cursor = db.cursor()
            self.db = db
        except:
            print('Connect error!')
#add_new employee 1
    add_employee = ("INSERT INTO employees(Name,Email,Department_type,Department_id) VALUES ('%s','%s','%s','%s');")
    def write_data_employees(self):
        print('Ти вибрав добавлення нового працівника')
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        employee = (name, email, department_type, department_id)
        return employee
#add_new_plant 2
    add_plant = ("INSERT INTO plant(location,name,director_id) VALUES ('%s','%s','%s');")
    def write_data_plant(self):
        print('Ти вибрав добавлення нового заводу')
        location = input("Location: ")
        name = input("Name: ")
        director_id = int(input("Director ID: "))
        plants = (location, name, director_id)
        return plants
#add_mew_salon 3
    add_salon = ("INSERT INTO salon(id,name_salon,adress_salon) VALUES ('%s','%s','%s');")
    def write_data_salon(self):
        print('Ти вибрав добавлення нового салону')
        id_salon = int(input('id: '))
        name_salon = input('Choose letters!\n'
                           'Name Salon:')
        adress_salon = input('Adress Salon:')
        salon = (id_salon, name_salon, adress_salon)
        return salon

#пошук по ід плант 4
    find_plant_by_id = ("SELECT * FROM plant WHERE(id) = ('%s');")
    def write_id_plant(self):
        print('Ти вибрав пошук заводу по ід')
        search_id = int(input('What id you find: '))
        plant_id = (search_id)
        return plant_id
#пошук по ід емплоіс 5
    find_employees_by_id = ("SELECT * FROM employees WHERE(id) = ('%s');")
    def write_id_employees(self):
        print('Ти вибрав пошук працівника по ід')
        search_idemp = int(input("What id you find: "))
        employees_id = (search_idemp)
        return employees_id
#пошук по ід салон 6
    find_salon_by_id = ("SELECT * FROM salon WHERE(id) = ('%s');")
    def write_id_salon(self):
        print('Ти вибрав пошук салону по ід')
        search_idsal = int(input("What id you find: "))
        salonid = (search_idsal)
        return salonid
    def run(self):
        while True:
            print('Choose your item:\n'
                  '1.Add New employees.\n',
                  '2.Add New Plant \n',
                  '3.Add New Salon\n'
                  '4. Get plant by id \n'
                  '5. Get employees by id \n'
                  '6. Get salon by id')
            menu_flag = int(input('Select one number:'))
            if menu_flag == 1:
                self.cursor.execute(self.add_employee % self.write_data_employees())
                self.db.commit()
                print('NEW EMPLOYEE')
            elif menu_flag == 2:
                self.cursor.execute(self.add_plant % self.write_data_plant())
                self.db.commit()
                print('NEW PLANT')
            elif menu_flag == 3:
                self.cursor.execute(self.add_salon % self.write_data_salon())
                self.db.commit()
                print('New SALON ')
            elif menu_flag == 4:
                self.cursor.execute(self.find_plant_by_id % self.write_id_plant())
                print(self.cursor.fetchall())
            elif menu_flag == 5:
                self.cursor.execute(self.find_employees_by_id % self.write_id_employees())
                print(self.cursor.fetchall())
            elif menu_flag == 6:
                self.cursor.execute(self.find_salon_by_id % self.write_id_salon())
                print(self.cursor.fetchall())

