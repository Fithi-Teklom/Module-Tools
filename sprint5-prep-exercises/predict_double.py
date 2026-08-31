# Predict what double("22") will do. Then run the code and check. Did it do what you expected? Why did it return the value it did?
def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]

print(double(22))

#So I predicted the string would be doubled(repeated) --> "2222"
#As in Python, multiplying a string by an integer means repeat the string