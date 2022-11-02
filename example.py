def request_calculation(data_string):
    with open("calculate.txt", "w") as file:
        file.write(data_string)
        
def read_bmi():
    with open("bmi.txt", "r") as read_file:
        bmi = read_file.readline()
    with open("bmi.txt", "w") as write_file:
        write_file.write("")
    return bmi
    
def read_bmr():
    with open("bmr.txt", "r") as read_file:
        bmr = read_file.readline()
    with open("bmr.txt", "w") as write_file:
        write_file.write("")
    return bmr
    
request_calculation("f 58.967 167.64 42")
print("BMI: ", read_bmi())
print("BMR: ", read_bmr())
print("\n")
request_calculation("m 73.482 175.26 40")
print("BMI: ", read_bmi())
print("BMR: ", read_bmr())