

interest_guess = eval(input("interest is :"))
years_pay = eval(input("years is :"))
first_item = eval(input("cash in every year is :"))
Total_income = (first_item*(1-(1+interest_guess)**years_pay))/(1.0-interest_guess-1)
print(Total_income)
