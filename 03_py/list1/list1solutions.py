def first_last6(nums):
  return nums[-1] == 6 or nums[0] ==6

def same_first_last(nums):
  return len(nums) > 0 and nums[0] == nums[-1]

def make_pi():
  return [3,1,4]
  
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]
  
def sum3(nums):
    i = 0
    sum = 0
    while i < len(nums):
        sum += nums[i]
        i += 1
    return sum
    
def rotate_left3(nums):
  return nums[1:] + [nums[0]]
  
def reverse3(nums):
    i = 1
    reverse = []
    while i <= len(nums):
        reverse.append(nums[-i])
        i += 1
    return reverse

def max_end3(nums):
  maxval = max(nums[0],nums[-1])
  return [maxval,maxval,maxval]
  
def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) <= 2:
        sum = 0
        i = 0
        while i < len(nums):
            sum += nums[i]
            i += 1
        return sum
    else:
        return nums[0] + nums[1]
        
def middle_way(a, b):
  return [a[1],b[1]]
  
def make_ends(nums):
  return [nums[0] , nums[-1]]
  
def has23(nums):
  return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3
  