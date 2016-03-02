# -*-coding:utf-8 -*

class Tab:

    def __init__(self, myTab=[[]]):
        self.tab=myTab

    def __getitem__(self, item):
        return self.tab[item]

    def dimensions(self):
        return (len(self.tab),len(self.tab[0]))

    def multline(self,index,number):
        temp = self[index]
        newtemp = []

        for elt in temp :
            newtemp.append(number*elt)

        self[index]=newtemp





