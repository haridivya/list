'''
10)Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50
'''
def sort_list(empty_list):
    empty_list.sort()
    after_sort=''
    for i in empty_list:
        after_sort+=str(i)+' '
    return after_sort
number=input().split(' ')
empty_list=[int(num) for num in number]
print(sort_list(empty_list))

#without using sort function
def sort_list(empty_list):
    list1=[]
    i,j,len_number=0,0,0
    after_sort=''
    while i==0:
        j=min(empty_list)
        list1.append(j)
        empty_list.remove(j)
        len_number=len(empty_list)
        if len_number==0:
            i+=1
    for i in list1:
        after_sort+=str(i)+' '
    return after_sort
number=input().split(' ')
empty_list=[int(num) for num in number]
print(sort_list(empty_list))
