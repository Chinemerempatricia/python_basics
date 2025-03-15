string_list = ["apple", "banana", "cherry", "date", "fig"]
init_list = [5, 3, 8, 1, 9, 2]

print("string_list:", string_list)
print("init_list:", init_list)

print("length of sring_list:", len(string_list)) 

print("first item (positive index):", string_list[0])
print("second item (positive index)", string_list[-1])

print("sliced int_list (index 1 to 4):", init_list[1:5])

string_list.append("grape")
print("updated string_list (after append):", string_list)

string_list.insert(2, "orange")
print("updated string_list (after insert):", string_list)

init_list.extend([10, 11, 12])
print("updated init_list (after extend):", init_list)

string_list.remove("banana")
print("updated string_list (after removal):",  string_list)

popped_item = init_list.pop()
print("updated int_list (after pop):", init_list)
print("popped item:", popped_item)
print("Items in init_list with index:")
for index, item in enumerate(init_list):  
    print(f"Index {index}: {item}")


string_list.reverse()
print("reversed string_list:", string_list)

init_list.sort()
print("sorted int_list (ascending):", init_list)

init_list.sort(reverse=True)
print("sorted int_list (descending):", init_list)

print("minimum of int_list:", min(init_list))
print("maximum of int_list:", max(init_list))
print("sum of int_list:", sum(init_list))

joined_string = ''.join(string_list) 
print("joined string_list:", joined_string)

split_list = "apple-banana-cherry-date".split("-")
print("split list:", split_list)

fruit_tuple = ("mango", "pineapple", "papaya", "guava")

print("fruit_tuple:", fruit_tuple)

print("Items in fruit_tuple:")
for fruit in fruit_tuple:
    print(fruit)

print("First element of fruit_tuple:", fruit_tuple[0])
print("Last element of fruit_tuple:", fruit_tuple[-1])

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

print("Intersection of set1 and set2:", set1 & set2)

print("Difference of set1 - set2:", set1 - set2)

print("Union of set1 and set2:", set1 | set2)







