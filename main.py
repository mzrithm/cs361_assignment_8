# bmi = ((weight in kg)/(height in cm)^2)*10,000
# bmr (Revised Harris-Benedict Formula)
# female bmr = 447.593 + (9.247 * weight in kg) + (3.098 * height in cm) - (4.330 * age in years)
# male bmr = 88.362 + (13.397 * weight in kg) + (4.799 * height in cm) - (5.677 * age in years)

def read_data():
    """This function reads calculate.txt for bmi/bmr calculation requests."""
    read = False
    while not read:
        file = open("calculate.txt", "r")
        data = file.readline()
        file.close()
        data = data.split()
        if len(data) != 0:
            read = True
            if len(data) == 2:
                weight = float(data[0])
                height = float(data[1])
                write_bmi(weight, height)
                write_bmr("No BMR Data", weight, height, 0)
            elif len(data) == 4:
                sex = data[0]
                weight = float(data[1])
                height = float(data[2])
                age = float(data[3])
                write_bmi(weight, height)
                write_bmr(sex, weight, height, age)
            with open("calculate.txt", "w") as file:
                file.write("")
                
def write_bmi(weight, height):
    """Calculate the BMI and write to bmi.txt."""
    bmi = str((weight/(height**2))*10000)
    with open("bmi.txt", "w") as file:
        file.write(bmi)

def write_bmr(sex, weight, height, age):
    "Calculate the BMR and write to bmr.txt."
    if sex.lower() == "f":
        bmr = str((447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)))
    elif sex.lower() == "m":
        bmr = str((88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)))
    else:
        bmr = sex
    with open("bmr.txt", "w") as file:
        file.write(bmr)
        

while(True):
    read_data()
    