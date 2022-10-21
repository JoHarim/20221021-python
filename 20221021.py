a = {1, 2, 3}
b = {}
if b and a:
    print('첫번째 : ', a)
if b or a:
    print('두번째 : ', a)
    print(b)
if a and b:
    print('세번째 : ', a)
    if bool(b):
        print('세번째 : ', b)
if a or b:
    print('네번째 : ', a)
    print('네번째 : ', b)