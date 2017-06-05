#!/usr/bin/env python

list_example = [111,222,333,444]
list_example.append(555)
print(list_example[4]) # 555
list_example.remove(555)
list_example.insert(2, 777)
print(list_example) # 111, 222, 777, 333, 444

list_example2 = [988, 989]
list_example.extend(list_example2)
print(list_example) # 111, 222, 777, 333, 444, 988, 989