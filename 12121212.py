class beijing():
    def __init__(self):
        self.course=[]
        self.cla=[]
        self.teacher=[]
    def create(self,cou):
        self.course.append(cou.name)
    def creat_cla(self,cla1):
        self.cla.append(cla1.name)
    def creat_teacher(self,teacher):
        self.teacher.append(teacher.name)
beijing=beijing()

class shanghai():
    def __init__(self):
        self.course=[]
        self.cla = []
        self.teacher = []
    def create(self,cou):
        self.course.append(cou.name)
    def creat_cla(self,cla1):
        self.cla.append(cla1.name)
    def creat_teacher(self,teacher):
        self.teacher.append(teacher.name)
shanghai=shanghai()



class linux():
    def __init__(self):
        self.name='linux'
        self.period='3 month'
        self.price='10000'
linux=linux()


class python():
    def __init__(self):
        self.name='python'
        self.period = '2 month'
        self.price = '15000'
python=python()


class go():
    def __init__(self):
        self.name='go'
        self.period = '1 month'
        self.price = '5000'
go=go()




class c1():
    def __init__(self,name):
        self.name=name
        self.course=[]
        self.teacher=[]
        self.student = []
    def create_course(self,cou):
        self.course.append(cou.name)
    def create_teacher(self,teacher):
        self.teacher.append(teacher.name)
    def create_student(self, student):
        self.student.append(student.name)
    def __str__(self):
        return self.name



class teacher():
    def __init__(self,name,cla,school):
        self.name=name
        self.school=school
        self.cla=cla



class student():
    def __init__(self,name,school,cla):
        self.name=name
        self.school=school
        self.cla=cla


def error():
    print('请重新输入')


course1={'python':python,'go':go,'linux':linux}
school1={'beijing':beijing,'shanghai':shanghai}
cla1={}
teacherlist={}
studentlist={}



def f1():
    sch = input("选择学校:")
    try:
        func1 = school1[sch]
    except:
        error()
        return f1()
    cou = input('创建课程:')
    try:
        func = course1[cou]
    except:
        error()
        return  f1()
    func1.create(func)


def f2():
    sch = input("选择学校:")
    try:
        func1 = school1[sch]
    except:
        error()
        return f2()
    cla_name = input('创建班级:')

    try:
        cla = c1(cla_name)
    except:
        error()
        return f2()
    func1.creat_cla(cla)
    cla1[cla_name] = cla
    print(cla)
    print(cla1)

def f3():
    try:
        teacher_name = input("老师姓名:")
        teacher_cla = input('所属班级:')
        teacher_school = input('所属学校:')
        teacher1 = teacher(teacher_name, teacher_cla, teacher_school)
        for i in cla1:
            if i == teacher_cla:
                cla1[i].create_teacher(teacher1)
        herschool = school1[teacher_school]
        herschool.creat_teacher(teacher1)
        teacherlist[teacher_name]=teacher1
    except:
        error()
        return f3()

def f4():
    try:
        cla = input("选择班级:")
        cou = input("创建课程:")
        for i in cla1:
            if i == cla:
                cla1[i].create_course(course1[cou])
    except:
        error()
        return f4()


def f5():
    try:
        student_name = input('学生姓名：')
        student_school = input('所属学校：')
        student_class = input("所属班级:")
        student1 = student(student_name, student_school, student_class)
        hisclass = cla1[student_class]
        hisclass.create_student(student1)
        print('student info:', student_name, student_school, student_class)
    except:
        error()
        return  f5()
    studentlist[student_name]=student1

def f6():
    info = input('查询：1.学校'
                 '     2.班级')
    if info == '1':
        print("beijing:课程：%s 班级：%s 老师:%s" % (beijing.course, beijing.cla, beijing.teacher))
        print("shanghai:课程：%s 班级：%s 老师:%s" % (shanghai.course, shanghai.cla, shanghai.teacher))
    if info == '2':
        for i in cla1:
            print("%s:课程：%s 老师：%s 学生:%s" % (i, cla1[i].course, cla1[i].teacher, cla1[i].student))

while 1:
    username = input("用户名：")
    password = input('password:')
    while 1:
        if username=='wjx' and password=='123':
            print('您是管理员')
            need=input("功能：1.为学校添加课程\n"
                       "     2.为学校添加班级\n"
                       "     3.为班级创建老师\n"
                       "     4.为班级添加课程\n"
                       "     5.添加学生\n"
                       "     6.查询\n"
                       "     7.返回\n")

            if need=='1':
                f1()

            if need=='2':
               f2()

            if need=='3':
                f3()

            if need=='4':
                f4()

            if need=='5':
                f5()

            if need=='6':
                f6()

            if need=='7':
                break
            if need=='8':
                print(cla1)


        if username == 'wjx2' and password == '123':
            print('您是老师')
            name=input("请输入您的姓名：")
            need = input("功能：1.查询\n"
                         "     2.管理班级\n"
                         "     3.查看学员\n"
                         "     4.修改学员成绩\n")
