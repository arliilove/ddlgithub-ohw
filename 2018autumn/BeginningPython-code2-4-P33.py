#检查用户名和PIN码是否在数据库中

database = [
    ['albert','1234'],
    ['dilbert','4242'],
    ['smith','7524'],
    ['jones','9843']
]
username = input('User Name: ')
pin = input('PIN code: ')

if [username,pin] in database:
    print ('Access granted')
