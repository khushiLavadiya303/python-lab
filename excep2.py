try:
    my_list=[2,4,6]
    print(my_list[0])
except IndexError:
        print("index out of range")
else:
    print("found successfully")
finally:
    print("done")                