
def time_to_text(h,m):

    time_dict ={ 00:"o",1: "one",2: "two",3: "three",4: "four",
            5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
            10:"ten", 11:"eleven", 12:"twelve",13: "thirteen",
            14:"fourteen",15: "quarter",16: "sixteen",
            17:"seventeen", 18:"eighteen",19: "nineteen",
            20:"twenty", 21:"twenty one",22: "twenty two",
            23:"twenty three", 24:"twenty four",
            25:"twenty five", 26:"twenty six", 27:"twenty seven",
            28:"twenty eight", 29:"twenty nine",30:"half"}

    if(m<=30):
        i = time_dict.get(h)
        j = time_dict.get(m)
        print(j,"past",i)

    else:
        j = 60 - m
        i = h+1

        i = time_dict.get(i)
        j = time_dict.get(j)

        if(j =="quarter"):
            print("quarter to", i)

        else:
            print(j, "minutes to", i)


time_to_text(1,33)
time_to_text(2,20)