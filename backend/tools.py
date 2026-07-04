from langchain_core.tools import tool


@tool
def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate Body Mass Index.
    Height should be in centimeters.
    Weight should be in kilograms.
    """
    height = height / 100
    bmi = weight / (height * height)
    return round(bmi, 2)


@tool
def calculate_bmr(weight: float, height: float, age: int, gender: str) -> float:
    """
    Calculate Basal Metabolic Rate.
    """

    gender = gender.lower()

    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5

    elif gender == "female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    else:
        raise ValueError("Invalid gender. Please use 'Male' or 'Female'.")

    return round(bmr, 2)


@tool
def water_intake(weight: float) -> float:
    """
    Calculate recommended daily water intake in liters.
    """

    return round(weight * 0.035, 2)