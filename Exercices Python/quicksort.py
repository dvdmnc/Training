
def quicksort(list): 
    new_list = []
    if len(list) <= 1:
        return list
    
    pivot = list.pop(0)
    lower = [i for i in list if i <= pivot]
    higher = [j for j in list if j > pivot]

    lower = quicksort(lower)
    higher = quicksort(higher)
    new_list += lower + [pivot] + higher

    return new_list


def fib(n, key_value): #find fibonacci value
    if n<=2:
        return 1
    elif n in key_value.keys():
        return key_value[n]
    key_value[n] = fib(n-1, key_value) + fib(n-2, key_value)
    return key_value[n]

def fib2(n):
    if n <= 1:
        return n
    fib_array = [0]*(n+1) #We count 0
    fib_array[1] = 1
    for i in range(1, n):
        print(fib_array)
        fib_array[i+1] += fib_array[i]
        try:
            fib_array[i+2] += fib_array[i]
        except IndexError:
            pass
    return fib_array[n]

def canConstruct(target,list, memo={}): #can we construct the target word with the list of words that is given to us
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return True
    memo[target] = False
    for sub in list:
        if target.startswith(sub):
            test_string = target.replace(sub,'',1)
            memo[test_string] =  canConstruct(test_string, list)
            if memo[test_string]:
                return True
    return memo[target]

def countConstruct(target, list, memo={}): #How many different ways do we have to construct that word
    if target in memo:
        return memo[target]
    memo[target] = 0
    if len(target) == 0:
        memo[target] += 1
        return memo[target]
    for sub in list:
        if target.startswith(sub):
            test_string = target.replace(sub,'',1)
            memo[target] += countConstruct(test_string,list)
    return memo[target]

def allConstruct(target,list, memo={}): #Print all the combination of words in the list to obtain target word
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return [[]]
    memo[target] = []
    for sub in list:
        if target.startswith(sub):
            test_string = target.replace(sub,'',1)
            res =  allConstruct(test_string,list)
            for sol in res:
                memo[target].append([sub, *sol])

    return memo[target]

def gridTraveler(i,j,count=0, memo={}):
    if (i,j) in memo:
        return memo[(i,j)]
    if i == 0 or j == 0:
        return 0
    if i == 1 and j == 1:
        count += 1
        return count
    left = gridTraveler(i-1, j)
    right = gridTraveler(i, j-1)

    memo[(i,j)] = left + right
    return memo[(i,j)]

def TabCanConstruct(list,target):
    new_list = [False]*(len(target)+1)
    new_list[0]= True

    for i in range(len(target)):
        if not new_list[i]:
            continue
        for sub in list:
            if target[i:].startswith(sub):
                try:
                    new_list[i+len(sub)]= True
                except IndexError:
                    continue
            if new_list[len(new_list)-1]:
                return True
    return False

def TabCountConstruct(list,target):
    new_list = [0]*(len(target)+1)
    new_list[0]= 1

    for i in range(len(target)):
        if new_list[i] == 0:
            continue
        for sub in list:
            if target[i:].startswith(sub):
                try:
                    new_list[i+len(sub)] += new_list[i]
                except IndexError:
                    continue
    return new_list[len(target)]

def TabAllConstruct(list,target):
    new_list = [[] for _ in range(len(target)+1)]
    new_list[0].append([])

    for i in range(len(target)):
        if len(new_list[i]) == 0:
            continue
        for sub in list:
            if target[i:].startswith(sub):
                try:
                    for l in new_list[i]:
                        new_list[i+len(sub)].append([*l,sub])
                except IndexError:
                    continue
    return new_list[len(target)]

def daily_temp(array): #Did we find a higher temperature ? If yes, how many days after. Return the array containing the days for each temp
    ans = [0]*len(array)
    ValueToIndex = {}
    for i,n in enumerate(array):
        try:
            ValueToIndex[n].append(i)
        except KeyError:
            ValueToIndex[n] = [i]

    stack = []
    for i, value in enumerate(array):
        current = value
        while stack and current > stack[-1]:
            val = stack.pop()
            try:
                idx = ValueToIndex[val].pop(0)
            except AttributeError:
                idx = ValueToIndex[val]
            ans[idx] = i - idx
        stack.append(current)
    
    return ans

def twoSum(array,target):#Find one combination of two numbers in the list equal to target (work but better time with two pointers)
    for i in range(len(array) - 1, 0 , -1):
        sub = target - array[i]
        if (sub) in array[:i]:
            return(array.index(sub), i)

def ThreeSum(array): #Find all combination of three numbers in the list equal to 0 (take too much time on really long lists. Use loop and two pointers solutions from twoSum for better time)
    array.sort()
    def backtracking(array,start,sol,ans):
        for i in range(start,len(array)):
            sol.append(array[i])
            if len(sol) == 3:
                if sum(sol) == 0:
                    if sol not in ans:
                        ans.append([*sol])
                sol.pop()
                continue
            ans = backtracking(array,i+1,sol,ans)
            sol.pop()
        return ans
    return backtracking(array,0,[],[])


def LongestSub(string):
    max_sub = string[0]
    max_len = 1
    j = 1
    while j < len(string):
        print(max_sub, max_len, string[j])
        if string[j] in max_sub:
            max_sub = max_sub[max_sub.index(string[j])+1:]
        max_sub += string[j]
        if len(max_sub) > max_len:
            max_len = len(max_sub)
        j += 1
    return(max_len)

def spiral_matrix(matrix): #My way of spiral matrix
    if not matrix:
        return []

    ans = []
    visited = []
    m = len(matrix[0])
    n = len(matrix)
    max_len = m * n
    i, j = 0, 0
    while len(ans) < max_len:
        # Traverse right
        while i < m and (i, j) not in visited:
            ans.append(matrix[j][i])
            visited.append((i, j))
            i += 1
        i -= 1
        j += 1
        # Traverse down
        while j < n and (i, j) not in visited:
            ans.append(matrix[j][i])
            visited.append((i, j))
            j += 1
        j -= 1
        i -= 1
        # Traverse left
        while i >= 0 and (i, j) not in visited:
            ans.append(matrix[j][i])
            visited.append((i, j))
            i -= 1
        i += 1
        j -= 1
        # Traverse up
        while j >= 0 and (i, j) not in visited:
            ans.append(matrix[j][i])
            visited.append((i, j))
            j -= 1
        j += 1
        i += 1
    return ans

def better_spiral_matrix(matrix): #Cleaner code for spiral matrix, and maybe shorter time complexity
    if not matrix:
        return []

    ans = []
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    direction_index = 0
    m = len(matrix[0])
    n = len(matrix)
    max_len = m * n
    i, j = 0, 0

    while len(ans) < max_len:
        current = matrix[i][j]

        if (i, j) in visited:
            break

        ans.append(current)
        visited.add((i, j))

        next_i, next_j = i + directions[direction_index][0], j + directions[direction_index][1]

        if not (0 <= next_i < m) or not (0 <= next_j < n) or (next_i, next_j) in visited:
            direction_index = (direction_index + 1) % 4

        i, j = i + directions[direction_index][0], j + directions[direction_index][1]

    return ans

def groupAnagrams(strs): #Doesn't work for really long array of strings
    if not strs:
        return [[""]]
    
    count = 0 
    visited = set()
    next_start = 0
    ans = []

    while len(visited) < len(strs):
        prev_start = i = next_start
        j = i + 1
        try:
            ans[count].append(strs[i])
        except IndexError:
            ans.append([strs[i]])
        visited.add(i)
        while j < len(strs):
            if j not in visited:
                if sorted(strs[j]) == sorted(strs[i]):
                    ans[count].append(strs[j])
                    visited.add(j)
                    i = j
                elif prev_start == next_start:
                    next_start = j
            j += 1
        count += 1
    
    return ans

def maxContainer(height): #Each number represents the height of a container (y-axis) on a graph and each index the position of the container (x-axis). Find the container with the most water
    container = 0
    l = 0
    r = len(height) -1
    while l < r:
        max_height = max(height[l], height[r])
        new = min(height[l],height[r])* (r - l)
        if new > container:
            container = new
        if max_height == height[l]:
            r -= 1
        else:
            l += 1
    return container

def permute(s1,s2): #If s2 contains any permutation of s1
    for i in range(len(s2)):
        j = i + len(s1)
        copy_s1 = s1
        for k in range(i,j):
            if s2[k] in copy_s1:
                copy_s1 = copy_s1.replace(s2[k],'',1)
            else:
                break
        if len(copy_s1) == 0:
            return True
    return False 

def maxWindow(nums,k): #Find the highest number in each window of k elements in nums array
    res = []
    i = 0
    j = i + k
    while j < len(nums) + 1:
        print(i,j,nums[i:j], max(nums[i:j]))
        res.append(max(nums[i:j]))
        i += 1
        j += 1
    return res

if __name__=='__main__':
    '''numbers = [4,6,3,2,9,7,3,5]
    ordered_list = quicksort(numbers)
    print(ordered_list)'''

    '''key_value = dict()
    res = fib(50, key_value)
    print(res)'''

    target1 = 'abcdef'
    target2 = 'skateboard'
    target3 = 'enterapotentpot'
    target4='purple'
    list1 = ['ab','abc','cd','def','abcd']
    list2 = ['bo','rd','ate','t','ska','sk','boar']
    list3 = ['a','p','ent','enter','ot','o','t']
    list4 = ['purp','p','ur','le','purpl']
    #print(canConstruct(target3,list3))
    #print(countConstruct(target4,list4))

    #print(allConstruct(target4,list4))

    #print(fib2(50))

    #print(gridTraveler(4,5))

    ''' print(TabCanConstruct(list4,target4))

    print(TabCountConstruct(list4,target4))

    print(TabAllConstruct(list3,target3))'''
    
    '''array1 = [73,74,75,71,69,72,76,73]
    array2 = [30,40,50,60]
    array3 = [30,60,90]
    print(daily_temp(array1))'''

    '''array = [1,3,4,5,7,10,11]
    array2 = [2,1,5,3]
    target = 9
    print(twoSum(array,target))'''

    '''array = [-3,3,4,-3,1,2]
    array2 = [-1,0,1,2,-1,-4]
    print(ThreeSum(array2))'''

    '''string1 ='abcabcbb'
    string2='bbbbbbb'
    string3='pwwkew'
    print(LongestSub(string2))'''

    '''matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiral_matrix(matrix))'''

    '''strs = ["eat","tea","tan","ate","nat","bat"]
    strs2 = [""]
    strs3 = ["a"]
    strs4 = ["",""]
    print(groupAnagrams(strs))'''

    '''height = [1,8,6,2,5,4,8,3,7]
    height2 = [1,1]
    print(maxContainer(height2))'''

    '''s1 = 'ab'
    s2 = 'eidboaoo'
    print(permute(s1,s2))'''

    nums=[1,3,-1,-3,5,3,6,7]
    nums2 = [1]
    k2 = 1
    k = 3
    print(maxWindow(nums2,k2))
