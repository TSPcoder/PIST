# -*-coding:utf-8 -*

class Constraint :

    """
    Defining of a constraint

    Variables : - coeffs list
                - constant
                - operateur ( a String )

    """

    def __init__(self, myCoeffs=[1,1,1], myConstant=0, myOperator= "<"):
        self.coeffsConstraint=myCoeffs
        self.constantConstraint=myConstant
        self.operatorConstraint=myOperator



    def normalize(self):
        outPut = []
        temp = self.coeffsConstraint
        if self.operatorConstraint == "<=" or self.operatorConstraint == "<":
            for elt in temp :
                outPut.append(elt)

            outPut.append(self.constantConstraint)

        else:
            for elt in temp :
                outPut.append(-elt)

            outPut.append(-self.constantConstraint)

        return outPut



