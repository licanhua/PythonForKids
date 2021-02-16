def PrintMax(ages):
    if (type(ages) is tuple):
        print("max is tuple " + str(max(ages)))

    elif (type(ages) is list):
        print("the max in list is " + str(max(ages)))

    elif (type(ages) is int):
        print("type is not supported")

ages = (4,4,6,5,2)
PrintMax(ages)

ages = [1, 2, 3, 4, 5]
PrintMax(ages)

ages = 1
PrintMax(ages)
