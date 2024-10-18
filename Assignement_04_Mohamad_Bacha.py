##### Exercise 1####

# def tuplesSum(tuple1, tuple2):
#     if len(tuple1)!=len(tuple2):
#         print("Error the tuples are not the same lenght please try again.")
#         tuplesSum(tuple1, tuple2)
#     else:    
#         result = [0] * len(tuple1)
#         for i, elem in enumerate(tuple1):
#             result[i] += elem
#         for i, elem in enumerate(tuple2):
#             result[i] += elem
#         return tuple(result)
    
# def writeJSON(d, file):
#     with open(file, "w") as f:
#         f.write("{\n")
#         for key, value in dict.items(N):
#             f.write(f'"{key}": {value}, \n')
#         f.write("}\n")
    
 




# def DisplayMenu():
#     print("The List is:\n" + "1- Sum Tuples\n" + "2- Export Json\n" + "3- Import Json\n" + "4- Exit\n")
#     Choice=int(input("Please choose from thr list: "))
#     while Choice!=4:
#         if Choice==1:
#             tuple1 = tuple(map(int, input("Enter tuple 1 (seperated by spaces): ").split()))
#             tuple2 = tuple(map(int, input("Enter tuple 1 (seperated by spaces): ").split()))
#             result=tuplesSum(tuple1, tuple2)
#             print("The result is:", result)
#             DisplayMenu()
#         elif Choice==2:
#             dict = {}
#             N = int(input("Enter the number of items in the dictionary: "))
#             for i in dict:
#                 key = input(f"Enter key {i+1}: ")
#                 value = int(input(f"Enter value {i+1}: "))
#                 dict[key] = value
#             file = input("Enter the file name: ")
#             writeJSON(dict, file)
#             print("JSON File Exported Successfully!!!")   
#             DisplayMenu() 
#         elif Choice==3:
#             print
        
#         else:
#             print("Invalid input please try again.")
#             DisplayMenu()
            
           

# DisplayMenu()


### Exercise 2 ###


#a- 1/6N+8000N3+24

# we have then N + N3
#the big O notation is then N3

#b- 1/6N3
#the big O notation is then N3

#c- 1/6N! +200N4
#the big O notation is then N!

#d- NlogN +1000
#the big O notation is then NlogN

#e. logN +N
#the big O notation is then logN

#f-1⁄2N(N-1)
#we have N^2/2
#the big O notation is then N2

#g- N2+220NlogN2+3N+9000
#the big O notation is then N2

#h- N!+3N+2N+N3+N2
#the big O notation is then N2






   