# Exercise 1 Multiplication and addition of two integers

# Funnction
def product_or_sum(number1, number2):
    product = number1 * number2 
    if product <=1000:
        return product
    else:
        return number1 + number2

# Givens
# Given1
number1 = 50
number2 = 23
# Given2
nextnumber1 = 100
nextnumber2 = 10
# Result
# Results
result1 = product_or_sum(number1, number2)
print("For numbers", number1, "and", number2, "the result is", result1)

result2 = product_or_sum(nextnumber1, nextnumber2)
print("For numbers", nextnumber1, "and", nextnumber2, "the result is", result2)

