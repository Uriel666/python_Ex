import numpy as np
import pandas as pd

def creatingSeries():
    a = [1 , 2 , 3]
    b = ["first" , "second" , "third"]


    seriea = pd.Series(a)
    serieb = pd.Series(b)

    return seriea,serieb

def creatingDataFrames():
    fruit = {
        'apples':[3 ,2 ,0,1],
        'oranges':[0,3,7,2]
    }

    #automatic index
    purchases = pd.DataFrame(fruit)

    #defining index
    purchases_with_index = pd.DataFrame(fruit, index = ['June' , 'Robert' , 'Lily' , 'David'])

    return purchases, purchases_with_index
    

def main():

    print(creatingDataFrames()[0])
    print(creatingDataFrames()[1])

if __name__ == '__main__':
    main()