import pymysql
con = pymysql.connect(host='localhost', user='root', password='1909802786110', db='register')
cs = con.cursor()
cs.execute("SELECT students.student_id,students.f_name,students.l_name,subjects.subject_id,subjects.subject_name,registers.semester FROM students,subjects,registers WHERE register.student_id=students.student_id AND registers.subject_id=subjects.subject_id AND semester=2")
data=cs.fetchall(5)
for (st_id,st_f,st_l,sub_id,sub_name,year) in data:
    print("{}, {}, {}, {},{},{}".format(st_id,st_f,st_l,sub_id,sub_name,year))
print(" ")
print(cs.rowcount)
con.close()
cs.close()