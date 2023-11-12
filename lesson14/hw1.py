def correct_lst(list_1,lst_name = [],lst_2 = [],lst_3 = []):
    for i in list_1:
        if isinstance(i,str):
            lst_name.append(i.title())
            lst_name.sort()
        elif isinstance(i,int):
            lst_2.append(i)
            lst_2.sort(reverse=True)
        else:
            lst_3.append(i)
    return lst_name,lst_2,sum(lst_3)

list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]
print(correct_lst(list_1))