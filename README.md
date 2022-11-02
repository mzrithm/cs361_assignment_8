# BMI & BMR Microservice

This microservice calculates the BMI, or the BMR and BMI via text file pipelines.

# How to REQUEST Data

The BMI is calculated by submitting the person's weight in kg and their height in cm.
For example:

`def request_calculation(data_string):`
    
    `with open("calculate.txt", "w") as file:
    
    file.write(data_string)`

The BMR and BMI is calculated by submitting the person's sex ('m' or 'f'), their weight in kg, their height in cm, and their age in years.

# How to RECEIVE Data

# UML Sequence Diagram

![BMI & BMR Microservice UML Sequence Diagram](https://github.com/mzrithm/cs361_assignment_8/blob/ced4b5abdc9c506c16ff49d1698503ce3ebf085f/MicroserviceUML.png)
