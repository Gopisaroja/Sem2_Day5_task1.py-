#count positive negative and zero
lists=[]
n=int(input("Enter the number of elements to form the list:"))
posi=0
neg=0
zero=0
for i in range(n):
	list=int(input("Enter the number %d:"%(i+1)))
	lists.append(list)
for i in lists:
	if i>0:
		posi+=1
	elif i<0:
		neg+=1
	else:
		zero+=1	
print("Positive number(s):",posi)
print("Negative number(s):",neg)
print("Zero(es):",zero)	
#palindrome
palindrome=True
for i in range(n):
	if lists[i]!=lists[n-1-i]:
		palindrome=False
		break
if palindrome==True:
	print("Palindrome")
elif palindrome==False:
	print("Not palindrome")
else:
	print("Invalid")		
#move all zeroes to end
end=[]
count=0
for i in range(n):
	if lists[i]!=0:
		end.append(lists[i])
	if lists[i]==0:
		count+=1	
for i in range(count):
		end.append(0)
print(end)
#second smallest number
second=float("inf")
smallest=float("inf")
for i in  lists:
	if i<smallest:
		second=smallest
		smallest=i
	elif i>smallest and i<second:
		second=i
if second==float("inf"):
			print("No second smallest.")
			
else:
		print(second)				
#mini  menu based program
task=[]
while True:
    print("1.Add a task.\n2.Show list\n3.Show sum.\n4.Exit.\n")
    choice = int(input("Enter the choice:"))

    if choice == 1:
        n = int(input("Enter how many numbers:"))
        for i in range(n):
            tasks = int(input("Enter a number:"))
            task.append(tasks)
            print("Tasks added successfully.")

    if choice == 2:
        for i in range(len(task)):
            if len(task) == 0:
                print("No tasks available, add a task to show up.")
            else:
                print(task[i])                              
    if choice==3:
        total=0
        for i in range(len(task)):
            total+=task[i]	
        print(total)
    if choice==4:
        print("Exiting....!")      
        break  
        
																																																																																																																																																												