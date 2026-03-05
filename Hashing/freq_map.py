x=int(input("Enter a number between 1 and 10 : "))
if x<1 and x>10:
    print("wrong input,please provide number within the range")
else:
    nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 8, 8, 9, 10, 10]
    frequency_map={}
    for i in range(0,len(nums)):
        if nums[i] in frequency_map:
            frequency_map[nums[i]]+=1
        else:
            frequency_map[nums[i]]=1
    print(frequency_map[x])