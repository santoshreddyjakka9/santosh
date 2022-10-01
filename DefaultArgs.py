def DefaultArguments(a,b,c='rambo'):
    print(a,b,c)
    return
def DefaultArguments(d,f,e=55):
    print(d,e,f)

DefaultArguments(22,33)
DefaultArguments(d=45,f=67)

#keyword arguments funtions

def KeywordArguments(name,age,dept=10):
    print("Name:",name)
    print("Age:",age)
    print("Dept:",dept)
    return
KeywordArguments('satish',25)


