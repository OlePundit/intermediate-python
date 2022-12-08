from multiprocessing import Pool
#Used to manage multiple processes. Controls a pool of worker processes to which chops can be submitted and manages the available process for you and splits the available data to smaller chunks which can be amanaged in parallel by different processes

import time

#With Value


def cube(number):
    return number* number * number
      


if __name__ == '__main__': 

    numbers = range(10)
    pool = Pool() #further look at documentation(map, apply, join, close)
    
    
    
    result = pool.map(cube, numbers) #create as many process as available in the machine and then split the iterable it into equal chunks and submit to the function above, and it is executed in parallel by different processes
    #pool.apply(cube, numbers[0])->if we only want to execute one process
    pool.close()
    pool.join()

    print(result)