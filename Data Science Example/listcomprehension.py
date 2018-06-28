lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [i+i1+j+j1 for i in lowercase for i1 in lowercase for j in digits for j1 in digits]
print(answer)