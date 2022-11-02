# BMI & BMR Microservice

This microservice calculates the BMI, or the BMR and BMI upon request by the user. 

Requests are made and received via text file pipelines.

# How to REQUEST Data

The BMI is calculated by submitting the person's weight in kg and their height in cm.

The BMR and BMI is calculated by submitting the person's sex ('m' or 'f'), their weight in kg, their height in cm, and their age in years.

These data values are submitted to the microservice by writing a single space separated value string to `calculate.txt` 

For example, this is a generic function to request a calculation:

![request_calculation(data_string)](https://github.com/mzrithm/cs361_assignment_8/blob/79e1cfeaadb90776e647eee608759beae082e936/request_calculation().png)

This is an example of using the function to request the BMI calculation:

![request_calculation(bmi_string)](https://github.com/mzrithm/cs361_assignment_8/blob/afcf253da6055af723a9e3df10dfb63b7d55cb4d/bmi_string.png)

This is an example of using the function to request the BMR and the BMI calculation:

![request_calculation(bmr_string)](https://github.com/mzrithm/cs361_assignment_8/blob/94159a61b7216ee63d3b9183370ccd034489cf99/bmr_string.png)

# How to RECEIVE Data

# UML Sequence Diagram

![BMI & BMR Microservice UML Sequence Diagram](https://github.com/mzrithm/cs361_assignment_8/blob/61dedf440d198dec7b65d0de8329e9a997426791/bmi%20bmr%20UML.png)
