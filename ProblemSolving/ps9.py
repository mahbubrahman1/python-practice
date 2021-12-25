
# # - Fibonacci series


#  Print 10 finacchi number 
#  i mean first 10 ta fibonacci number print korar kotha bola hoyeche 


n = int(input("Enter number: "))
a = 0
b = 1 # a & b holo constant egula 2 ta lagbei ar amra variable nilam C
c = 0
count = 1

while count <= n:
  print(c)
  count = count + 1
  a = b
  b = c
  c = a + b




# def fibo(x):

# 	a = 0
# 	b = 1
# 	print(0)
# 	print(1)
	
# 	for i in range(2, x):
# 		c = a + b
# 		a = b
# 		b = c
# 		print(c)

# fibo(10)







# # * Fibonacci number less then 50
# # i mean 50 er vitore ba choto je sonkha gla ache ta print kote hobe    

# n = int(input("Enter a number: "))

# a = 0  
# b = 1  # a & b holo constant egula 2 ta lagbei ar amra variable nilam C
# c = 0

# while c <= n:
#     print(c)
#     a = b
#     b = c
#     c = a + b



# def fibo(n):

#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fibo(n-1) + fibo(n-2)

# n = int(input("Enter number of terms: "))

# for i in range(1, n + 1):
#     print(fibo(i))














# # altenative 


# def fibonacciq(num):

#     fibo = [0, 1]
#     i = 2
#     while i <= num:
#         next_fibo = fibo[i-1] + fibo[i-2]
#         fibo.append(next_fibo)
#         i = i + 1
#     return fibo

# print(fibonacciq(10))
