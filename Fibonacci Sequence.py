# Example n = 5 , is 0,1,1,2,3

def gen_fib(n):
    fibo_seq= [0,1]

    while len(fibo_seq) < n :
        next_term = fibo_seq[-1] + fibo_seq[-2]
        fibo_seq.append(next_term)
    return fibo_seq

user_input = int(input("Enter Your number 'n': "))
seq = gen_fib(user_input)
print(f"The first {user_input} terms of fibonacci sequence is {seq}")