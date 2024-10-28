
'''
Enter the code from 1 to 5 according to the list
and then enter the quantity of the product and the
price will appear
# VScode
'''
code = int(input('enter the product code: \n'))
amount = float(input('Enter the quantity of the product: \n'))
price = 0,00
produtos = [['hot-dog','salad','x-bacon','toast','soda'],[4.000,4.5000,5.000,2.000,1.500]]
#price = round(produtos[1][code-1] * amount, 2)
price = produtos[1][code-1] * amount
print(produtos[0][code-1])
print(price)