***The Following Formula Shows How to Imput a Phone Number***
phone_number = int(input())

area_code = int(phone_number // 1000  / 10000)

prefix = int(phone_number // 10000 % 1000)
 
line_number = int(phone_number % 10000)

print('({}) {}-{}'.format(area_code, prefix, line_number))
