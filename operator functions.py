# operator
print("10+20=", 10+20)
print("10*20=", 10*20)
print("10/20=", 10/20)
print("10//20=", 10//20)

## reminder
print("10%20=", 10%20)

## exponent
print("10**20=", 10**20)


# comparasion operator
print("10==20",10==20)
print("10 !=20", 10 !=20)

# logic operator
print("(10 >20) and (10 < 20)", (10> 20) and (10<20))
print("(10 >20) or (10 < 20)", (10> 20) or (10<20))
print("not(10 >20)", not(10> 20))


####### for #######
print(" for function")
subjects = ["excel", "sql", "python", "statistics"]
for sub in subjects:
    print("I am learning: {}".format(sub))
###{} is necessary for sub ###
    
### while ###
likenum = 0
while likenum < 10:
    print("I and little fly is not good friend because i only have {} tumb up". format(likenum))
    likenum = likenum + 1
print("i and little fly is good friend because I have {} tumbup".format(likenum))
print("_"*30 + "end section 2 cycle" + "-"*30)

##### conditional###

body_temperature = 30

if body_temperature > 42:
    print ("please monitor")
elif body_temperature >38:
    print("please monitor")
elif body_temperature >37:
    print("please monitor")
else: 
    print("he is normal")
print("if condition")

#### function###
def learn_python(location):
    print("I am learning python at {}".format(loction))
learn_python("subway")
learn_python("airplane")

def learn_python_with(location):
    doing = "I am learning at {} python".format(location)
    return doing
ret = learn_python_with("airplane")
print(ret)


### def multiple functions##

def learn_python_mul(location,people):
    doing = "I am at {} lean python, people{}".format(location,people)
    return doing
ret = learn_python_mul("bicycle", "I")
print(ret)


### module###

import pandas as pd
s1 = pd.Series(['a','b','c','d','e'])
print(s1)









