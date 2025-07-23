global_ver = "I am outside global"

def global_function():
    local_var = "I am inside global"
    print(local_var)
global_function()

print(global_ver)