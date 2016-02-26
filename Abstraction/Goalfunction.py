# -*-coding:utf-8 -*

class GoalFunction:

    """
    Defining of the Goal function
    Variables  :coeff list  ,
                boolean (true if max si max, false if min)

    E.g : if z = 3x1 + 4x2 + 5
          if we want to maximize z
          then coeffs = [3,4,5]
          minOrMax = true

    """


    # CONSTRUCTOR
    def __init__(self,myCoeffs=[0,0,0],myMinOrMax=True):
        self.coeffs=myCoeffs
        self.minOrMax=myMinOrMax


    # e.g , with the example above , normalize returns [3,4,5,True]

    def normalize(self):
        output= []
        temp = self.coeffs
        for elt in temp :
            output.append(elt)

        output.append(self.minOrMax)

        return output