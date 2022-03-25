# for to while loop converter
total_ele = len(arr)
initial_number = 0
first = []
while initial_number<total_ele:
    selected_num = arr[initial_number]*2.5
    if selected_num%2==0:
        first.append(int(selected_num))
        
    initial_number+=1
    
print(first)
