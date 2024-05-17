class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def __str__(self):
        return f"имя - {self.name},элктронная почта - {self.email},телефон - {self.phone}"
aza = GeeksPeople("azamkhodja", "azamkhodjaews.17@gmail.com", "samsung")
print(aza)

class Studente(GeeksPeople):
    def __init__(self, name, email, phone, studente_id,group_where_study):
        GeeksPeople.__init__(self,name, email, phone)
        self.studente_id = studente_id
        self.group_where_study = group_where_study
    def study(self):
        print(f"имя - {self.name},учится в группе-{self.group_where_study}")
aza = Studente("azamkhodja", "azamkhod1aews.17@gmail.com", "samsung",123456533433,"17-2b")
aza.study()

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        GeeksPeople.__init__(self,name, email, phone)
        self. teacher_id = teacher_id
        self.group_where_teach = group_where_teach
    def teach(self):
        print(f"имя - {self.name},препадает группе-{self.group_where_teach}")
Syimyk = Teacher("Syimyk","Syimyk@gmail.com","apple",47327598,"17-2b")
Syimyk.teach()

class Admin(GeeksPeople):
    def __init__(self, name, email, phone,admin_id):
        GeeksPeople.__init__(self,name, email, phone)
        self.admin_id = admin_id
    def creat_group(self):
        print(f"{self.name}-создал группу")

admin = Admin('ulan','ulan@gmail.com','apple',23246578)   
admin.creat_group()
class Mentor(Studente,Teacher):
    def __init__(self, name, email, phone, studente_id, group_where_study,teacher_id, group_where_teach):
        Teacher.__init__(self,name, email, phone, studente_id, group_where_study)
        Studente.__init__(self,name, email, phone,teacher_id, group_where_teach )
mentor = Mentor("aslan","aslan@gmail.com","apple",123456533433,"17-2b",47327598,"15-2b")
mentor.teach()
mentor.study()


    
    

        



    









    
