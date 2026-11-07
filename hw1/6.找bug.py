"""
bug位置：
在for idx in range(len(list))循环里正序排除元素，超越实际大小，且不能正确检查下一项

原因：
1.range(len(list))的长度在循环开始时就固定为1000，之后列表变短，循环仍会向后查找，而pop已经删掉了元素，最终 idx 超出当前nums大小
2.pop(idx)删除一个元素后，后面的元素全部左移一位，而idx+1使下一个元素被跳过

改法：
实时记录列表长度len，循环改为while循环，idx只在偶数时才+1
"""

if __name__=="__main__":
    nums=list(range(1000))
    length=len(nums)
    idx=0
    while idx<length:
        if nums[idx]%2==1:
            nums.pop(idx)
            length-=1
        else:
            idx+=1
print(nums)