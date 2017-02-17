for i in range(1, 101):
    if i % 3 == 0 or "3" in str(i):
        print("aho!")
    # elif str(i).find("3") == 1 :
    #     print("aho!")
    else:
        print(i)
