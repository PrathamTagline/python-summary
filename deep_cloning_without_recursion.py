arr = [1,2,3,[4,[5,6,[7,8],9],10],[11,[12,13],14],15]
clone_list = []
index = []
path = [arr]

stack = []


while path != []:
    current_last_index = path.index(path[0])
    temp = []
    for i in path[current_last_index]:
        if type(i) == list:
            path.append(i)   
            index.append(path[current_last_index].index(i))  
        else:
            temp.append(i)
            
    path.remove(path[current_last_index])
    stack.append(temp)

print("")
print(f"index {index}")
print(f"stack : {stack}")
print("")
