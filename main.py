even  = 43219

sum = 0

x1 = even % 10      #   3
sum += x1
even = even // 10     #124
x2 = even % 10      #4
sum += x2
even = even // 10     #12
x3 = even % 10       #   2
sum += x3
even = (even // 10)       #1
x4 = even % 10      #1
sum += x4
even = even // 10 
x5 = even % 10      #   3
sum += x5
even = even // 10 

# answer = x1 * 100 + x2 * 10 + x3
print(sum)