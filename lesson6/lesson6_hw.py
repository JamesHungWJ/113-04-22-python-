import pyinputplus as pyip

    name = input('請輸入姓名:')
    height = pyip.inputInt('請輸入身高(120~230)(cm):',min=120,max=300)
    weight = pyip.inputInt(('請輸入體重(40~170)(kg):',min=40,max=170))
    bmi = weight / (height / 100) ** 2
    print(f'{name}, 您的BMI: {round(bmi,ndigits=2)}')