# -*-coding:utf-8 -*

class Tab:



    def __init__(self, *tuple):
        self.tab=list(tuple)


    def __getitem__(self, item):
        return self.tab[item]

    def __setitem__(self, key, value):
        self.tab[key]=value

    def __str__(self):
        return "{}".format(self.tab)

    def dimensions(self):
        return (len(self.tab),len(self.tab[0]))

    def mult(self,number,i,j):
        tempfirst = self.tab[i]
        tempsecond=[]
        for elt in tempfirst :
            tempsecond.append(elt*number)

        self.tab[j]=tempsecond

def main():
        print("")
        print ("-- Presentation of the Tab Class -- ")
        print("")
        print ("Let's show the functionalities by using this example : a = [[1,2,3,4],[7,5,2,3],[1000,-4,2]]")
        print("")
        a = Tab([1,2,3,4],[7,5,2,3],[1000,-4,2,11])
        print("1) Access the item (i,j) ")
        print("     For instance a[0][1] returns {} ".format(a[0][1]))
        print("")
        print("2) Do (line j = alpha * line i) is possible by using the mult method : e.g => a.mult(alpha,i,j)        ")
        a.mult(100,1,2)
        #a[0]=[1,1,1,1]
        print("     For instance a.mult(100,1,2) modifies a in order to have a = {} ".format(a))
        print("")
        print("3) The dimensions method ")
        print("The dimensions of a are {} ".format(a.dimensions()))


main()







