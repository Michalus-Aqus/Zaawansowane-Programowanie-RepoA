class Library:# (klasa opisująca bibliotekę), posiadająca pola:
    def __init__(self,city,street,zip_code,open_hours,phone):
        self.city:str=city
        self.street:str=street
        self.zip_code=zip_code
        self.open_hours=open_hours
        self.phone=phone
    def __str__(self):
        return "Library<"+self.city+" "+self.street+">"
    
class Employee:
    def __init__(self,first_name,last_name,hire_date,birth_date,city,street,zip_code,phone):
        self.first_name=first_name
        self.last_name=last_name
        self.hire_date=hire_date
        self.birth_date=birth_date
        self.city=city
        street=street
        zip_code=zip_code
        phone=phone
    def __str__(self):
        return "Employee<"+self.first_name+" "+self.last_name+">"
        
class Book:
    def __init__(self,library,publication_date,author_name,author_surname,number_of_pages):
        self.library=library
        self.publication_date=publication_date
        self.author_name=author_name
        self.author_surname=author_surname
        self.number_of_pages=number_of_pages
    def __str__(self):
        return "Book<"+self.library.__str__()+" "+self.last_name+">"
    
class Order:
    def __init__(self,employee,student,books,order_date):
        self.employee=employee
        self.student=student
        self.books=books
        self.order_date=order_date
    def __str__(self):
        return "Order<"+str(self.employee)+" "+self.student+str(self.books)+str(self.order_date)+">"

def main():
    lib_01=Library("Katowice","Ligonia 7","40-036",
    "poniedziałek – piątek: 8.00 – 19.00 sobota: 9.00 – 15.00",
    "322 513 047")
    lib_02=Library("Katowice","Gliwicka 93","40-854",
    "poniedziałek – piątek: 8.00 – 19.00 sobota: 9.00 – 15.00",
    "322 545 969")
    book_01=Book(lib_01,"1960","Jan","Kowalsky",500)
    book_02=Book(lib_02,"1960","Jan","Kowalsky",500)
    book_03=Book(lib_01,"1970","Jan","Kowalsky",540)
    book_04=Book(lib_02,"1970","Jan","Kowalsky",540)
    book_05=Book(lib_01,"1975","Jaś","Kowalski",580)
    stud_01="TODO1"
    stud_02="TODO2"
    stud_03="TODO3"
    emp_01=Employee("James","Bond","18-10-2022","08-05-1963","Tychy","kościuszki 4","36-650","444 444 444")
    emp_02=Employee("Janusz","Bielski","10-10-2020","08-05-1923","Sosnowiec","kasztanowa 16","30-650","555 444 444")
    emp_03=Employee("Grażyna","Bielska","12-11-2020","08-05-2012","Sosnowiec","kasztanowa 24","30-650","555 333 444")
    ord_01=Order(emp_01,stud_01,[book_01,book_05],"20.10.2022")
    ord_02=Order(emp_02,stud_03,[book_03,book_02],"20.10.2022")
    print(str(ord_01))
main()
