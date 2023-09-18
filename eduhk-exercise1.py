# writer：LeBron James
# My email 1269497440@qq.com
def  determineGrade(Average):
    if Average>=0 and Average < 50:
        grade = 'Grade F '
    elif Average >= 50 and Average < 60:
        grade = 'Grade D'
    elif Average >=60 and Average < 70:
        grade = 'Grade C'
    elif    Average >=70 and Average < 80:
        grade = 'Grade B'
    else:
        grade = 'Grade A'
    return grade

if __name__ == '__main__':
    input("Student Name:")
    input("Student ID:")
    f1= float(input("Assignment 1:"))
    f2=float(input("Assignment 2:"))
    f3=float(input("Assignment 3:"))
    f4=float(input("Assignment 4:"))
    Average=((f1*0.2)+(f2*0.2)+(f3*0.3)+(f4*0.3))
    print("{name} {Average}".format(name="Average",Average=Average))
    print(determineGrade(Average))
    print("End of Report*********************")


