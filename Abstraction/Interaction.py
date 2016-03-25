# -*-coding:utf-8 -*

from Constraint import *
from Goalfunction import *
from Table import *
from Table2 import *


def main() :
    a = Table2()

    print("Please enter your GoalFunction on this form ( respect spaces between characters )  "
          " : z = a * x1 + b * x2 + c ")
    c = raw_input()
    c = c.split()

    i1 = c.index("x1")
    i2 = c.index("x2")

    go =GoalFunction([int(c[i1-2]),int(c[i2-2]),int(c[i2+2])],True)

    que = "Do you want to add a constraint ? "

    value = True

    while value == True :
        print(que)
        h = raw_input()
        h = h.split()

        if h[0].upper()=='Y' :
            value=True
            print("Please enter your constraint on this form : alpha * x1 + beta * x2 < gamma ")
            cons = raw_input()
            cons = cons.split()
            index1 = cons.index('x1')
            index2 = cons.index('x2')
            index3 = cons.index('<')

            o = Constraint([int(cons[index1-2]),int(cons[index2-2]),int(cons[index3+1])],"<")
            a.addConstraintStepOne(o)



        else :
            value=False

    #g = GoalFunction([300,100,0],True)
    #c1 = Constraint([1,1,4],"<")
    #c2 = Constraint([1,0,3],"<")
    #c3 = Constraint([0,1,2],"<")

    #a.addConstraintStepOne(c1)
    #a.addConstraintStepOne(c2)
    #a.addConstraintStepOne(c3)



    print(a.simplex2(go))
    a.printTable()


main()