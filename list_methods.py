def list_methods():
    counter = 0
    for method in dir(list):
        if "__" not in method:
            counter += 1
            print(f"{counter}: {method}")


list_methods()
print("----------------------------------------------------")
# 1: append() method
# append method will add an element at the end of the list
list_append = ["mustafa", "ali"]
list_append.append("fatima")
print(f"1. append method: {list_append}")
print("=====================")
# 2: clear() method
# clear method will clear the list
list_clear = [1, 2, 3, 4]
list_clear.clear()
print(f"2. clear method: {list_clear}")
print("=====================")
# 3: copy() method
# copy method will create a copy of an existing list
list_copy = ["python", "java"]
list2_copy = list_copy.copy()
print(f"3. copy method: {list2_copy}")
print("=====================")
# 4: count() method
# count method will count the elements of a alist
list_count = [1, 3, 5, 6, "mustafa", "python", "flask", "mustafa", "mustafa", "this is mustafa"]
count_element = list_count.count("mustafa")
print(f"4. count method: {count_element}")
print("=====================")
# 5: extend() method
# extend method allows to extend a list to an existing list
list_extend = [1, 3, 5, 7, 9]
list_extend2 = [2, 4, 6, 8]
list_extend.extend(list_extend2)
print(f"5. extend method: {sorted(list_extend)}")
print("=====================")
# 6: index() method
# index method will find the index or location of an element from the list
list_index = ["mustafa", "john", "luca", "fatima"]
find_index = list_index.index("fatima")
print(f"6. index method: {find_index}")
print("=====================")
# 7: insert() method
# insert method will help to insert an element to an existing list in a specific index location
list_insert = [1, 2, 3, 4, 6, 7, 8, 9]
list_insert.insert(4, 5)
print(f"7. insert method: {list_insert}")
print("=====================")
# 8: pop() method
# pop method will remove an element from the list by its index position and return the removed element
list_pop = ["mustafa", "ali", "masoud", "fatima", "akbari"]
list_pop.pop(0)
print(f"8. pop method: {list_pop}")
print("=====================")
# 9: remove() method
# remove method will remove an element of a list by its value
list_remove = ["python", "java", "css", "html"]
list_remove.remove("java")
print(f"9. remove method: {list_remove}")
print("=====================")
# 10. reverse() method
# reverse method will reverse the element of the list
list_reverse = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_reverse.reverse()
print(f"10. reverse method: {list_reverse}")
print("=====================")
# 11. sort() method
# sort method will sort the list, by default it sorts the list string alphabetical
# if there is a list that has lowercase and uppercase it will sort the uppercase first
# than sort the lowercase
# we can define a key to sort all elements as lower or upper
list_sort2 = ["mustafa", "fatima", "ali", "jan", "ehsan", "farid", "Ghulam", "Akbar"]
list_sort2.sort(key=lambda name: name.casefold())
print(f"11. sort method alphabetical: {list_sort2}")
list_sort = [4, 6, 8, 2, 3, 9, 10]
list_sort.sort()
print(f"11. sort method: {list_sort}")
list_sort.sort(reverse=True)
print(f"11. sort method in reverse order: {list_sort}")