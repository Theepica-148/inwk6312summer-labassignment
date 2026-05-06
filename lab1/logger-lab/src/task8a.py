class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.salary} -> {self.message}"


# Start of Program
try:
    salary = int(input("Enter salary amount: "))

    if not 5000 < salary < 15000:
        raise SalaryNotInRangeError(salary)

    print("Salary is within valid range.")

except SalaryNotInRangeError as e:
    print("Error:", e)

except ValueError:
    print("Please enter a valid integer.")
