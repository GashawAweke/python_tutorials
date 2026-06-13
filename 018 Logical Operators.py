# AND

high_income = True
good_credit = True

if high_income and good_credit:
    print("Loan Approved")


# OR Operator
high_income = False
good_credit = True

if high_income or good_credit:
    print("Loan Approved")


# NOT Operator

student = True

if not student:
    print("Eligible")
else:
    print("Not Eligible")

# Combining Logical Operators

# Using parentheses makes complex conditions easier to read.
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
