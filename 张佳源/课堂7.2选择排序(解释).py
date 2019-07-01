A=[78,59,43,12,93,42]
for i in range(len(A)):        #将以下运行n次（保证列表中每一个数都能比较大小）
    min_idx=i                  #从头开始，依次，取列表中的一个位置
    for j in range(i+1,len(A)):#判断这个位置的数和后面所有数的关系
        if(A[min_idx]>A[j]):   #如果这个位置的数比后面的数都小，才能占据这个位置
            min_idx=j          #如果这个数不如后面数小，就掉换位置
    A[i],A[min_idx ]=A[min_idx ],A[i]#排序的结果就是每过一个i，就能把一个最小的数放在前面
print("排序后：")              #再比较下一个最小的数放在前面，和上节课最大的放在后面相反
for i in range(len(A)):
    print("%d"%A[i])