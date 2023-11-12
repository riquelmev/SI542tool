# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def run_script():
    # Use a breakpoint in the code line below to debug your script.
    gender = input("Please input the patient's gender. Enter m or f")
    while gender != "m" or gender != "f":
        gender = input("That was not a valid input. Please input the patient's gender. Enter m or f")

    age = input("Please input the patient's age. Please enter a non-negative number")
    while type(age) != int or age < 0:
        age = input("That was not a valid input. Please input the patient's age. Please enter a non-negative number")

    HBV = input("Is the patient HBeAG+ or HBeAG-. Enter + or -")
    while HBV != "+" or HBV != "-":
        HBV = input("That is not an appropraite answer. Is the patient HBeAG+ or HBeAG-. Enter + or -")
    if HBV == "+":
        print("You have entered that the patient is HBeAG+")

        ALT = input("Is the patient's ALT score lower than their ULN score: Enter yes or no")
        while ALT != "yes" or ALT != "no":
            ALT = input("Is the patient's ALT score lower than their ULN score: Enter yes or no")

        if ALT == 'yes':
            if age > 40:
                if gender == "m":
                    risk = "10-15"
                else:
                    risk = "8-13"
                return(f"Recommedation is Biopsy/Therapy + HCC survailence. Risk score is {risk}")
            else:
                if gender == "m":
                    risk = "8-10"
                else:
                    risk = "6-8"
                return(f"Recommendation is 3 month follow up. Risk score of {risk}")
        else:

            ULN = input("Is the patient's ALT score greater than twice than their ULN score: Enter yes or no")
            while ULN != "yes" or ULN!= "no":
                ULN = input("That is not a valid input. Is the patient's ALT score greater than twice than their ULN score: Enter yes or no")

            if ULN == "yes":
                if gender == "m":
                    risk = "10-16"
                else:
                    risk = "8-14"
                return(f"User has persistently HBeAg(+) and elevated ALT. Recommendation is Antiviral treatment. Risk score of {risk}")
            else:
                if age > 40:
                    if gender == "m":
                        risk = "12-16"
                    else:
                        risk = "10-14"
                    return (f"Recommedation is Biopsy/Therapy + HCC survailence. Risk score is {risk}")
                else:
                    if gender == "m":
                        risk = "10-11"
                    else:
                        risk = "8-9"
                    return (f"Recommendation is 1-3 month follow up. Risk score of {risk}")



    else:
        print("You have entered that the patient is HBeAG-")






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_script()

