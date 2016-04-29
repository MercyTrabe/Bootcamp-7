people =[('Alice', 20), ('Ben', 34), ('dan', 9), ('Jacob', 56)]
a=["Mercy","Mercy" ,"is"]
print("count for Mercy:",a.count("Mercy"))
print("count for is:",a.count("is"))

def super_sum(*args):
    return sum(args)

def hello_again(name, age):
    return "I am {} and {} years old".format(name, age)

def max_min(A):
    '''
    retrns max value - min value
    '''
    # return max (A) - min (A)
    max_, min_ = A[0], A[0]

    for i in A:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i

    return max_ - min_