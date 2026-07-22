def cube(num):
    answer = num**3
    return answer

def square(num):
    answer = num**2
    return answer

def average(list):
    length = len(list)
    total = 0
    for num in list:
        total += num

    answer = total/length
    return answer
