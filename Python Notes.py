# 1. import json ( For working with json files )
# ------> For converting dictionary to JSON
import json
json_var = json.dumps(dict_var, indent=4) 
with open('demo.json', 'w') as f:
	json.dump(dict_var, f, indent=4)

# -------> For converting JSON to dictionary 
with open('demo.json', 'r') as f:
	python_dict = json.load(f)

# 2. To get details of a class into json object
class User:	
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
user = User("nik", 24)

def encode_user(o):
	if o.isinstance(o, User):
		return {"name": o.name, "age": o.age, "class_name": o.__class__.__name__
	else:
		raise TypeError("Object is not serializable")

userJSON = json.dumps(user, default=encode_user)

# ==============================================================================================================================

# 3. Decorators => They extend the behaviour of a function without explicitly modifying it.
def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

def print_name():
    print("Nik")

print_f = start_end_decorator(print_name)

print_f()

# 4. Generalized Decorator Syntax
import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do Something....
        result = func(*args, **kwargs)
        # Do Something....
        return result
    return wrapper

# 5. Count the number of times a function is called
class CountCalls():

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Executed {self.num_calls} times!")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello")


say_hello()
say_hello()

# =============================================================================================================

# 6. Generators use very less memory as compared to any other data structure in python
def fibbonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a+b

fib = fibbonacci(10)
for i in fib:
    print(i)

# 7. One line generators are created in the same way as list comprehension. We use () brackes instead of [], that's it.

# ===============================================================================================================

# 8. conda commands to add a virtual environment to jupyter notebook
	# pip install --user ipykernel
	# python -m ipykernel install --user --name=myenv
			
