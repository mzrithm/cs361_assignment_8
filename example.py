def request_calculation(data_string):
    with open("calculate.txt", "w") as file:
        file.write(data_string)


def read_bmi():
    read = False
    while not read:
        with open("bmi.txt", "r") as read_file:
            bmi = read_file.readline()
        if len(bmi.split()) != 0:
            read = True
    with open("bmi.txt", "w") as write_file:
        write_file.write("")
    return bmi


def read_bmr():
    read = False
    while not read:
        with open("bmr.txt", "r") as read_file:
            bmr = read_file.readline()
        if len(bmr.split()) != 0:
            read = True
    with open("bmr.txt", "w") as write_file:
        write_file.write("")
    return bmr


# person is 130 lbs and 5 ft 6 inches
# convert to metric -> 58.967 kg and 167.64 cm
# submit as one space separated string to function

request_calculation("58.967 167.64")

with open("result_1.txt", "w") as result_1:
    result_1_message = f'BMI is {read_bmi()} and BMR is {read_bmr()}.'
    result_1.write(result_1_message)

# person is male, 160 lbs, 5 ft 9 inches, and 40 years old
# convert to metric -> 73.482 kg and 175.26 cm
# submit as one space separated string to function

request_calculation("m 73.482 175.26 40")

with open("result_2.txt", "w") as result_2:
    result_2_message = f'BMI is {read_bmi()} and BMR is {read_bmr()}.'
    result_2.write(result_2_message)
