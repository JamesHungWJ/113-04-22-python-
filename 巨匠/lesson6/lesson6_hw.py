#try:
#    name = input('請輸入姓名:')
#    height = float(input('請輸入身高(120~230)(cm):')) 
#    if height<120 or height>230:
#        raise Exception("身高必需大於120同時小於230")    
#    weight = float(input('請輸入體重(40~170)(kg):'))
#    if weight<40 or weight>170:
#        raise Exception("體重必需大於40同時小於170")
#    bmi = weight / (height / 100) ** 2
#    print(f'{name}, 您的BMI: {round(bmi,ndigits=2)}')
#except Exception as e:
#    print(f'錯誤: {e}')

import pyinputplus as pyip
name = pyip.inputStr('請輸入姓名:')
height = pyip.inputFloat('請輸入身高(120~230)(cm):',min=120,max=300)
weight = pyip.inputFloat('請輸入體重(40~170)(kg):',min=40,max=170)

bmi = weight / (height / 100) ** 2
print(f'{name}, 您的BMI: {round(bmi,ndigits=2)}')