import pyinputplus as py
def bmi_show(height: float, weight: float) -> float:
    return weight / (height / 100) ** 2
def valu_show (bmi:float) ->str:
    if bmi < 18.5:
        result = '過輕'
    elif bmi < 24:
        result = '正常'
    elif bmi < 27:
        result = '過重'
    elif bmi < 30:
        result = '輕度肥胖'
    elif bmi < 35:
        result = '中度肥胖'
    else:
        result = '重度肥胖'
    return result

name=input("請輸入姓名:")
height=py.inputFloat('請輸入身高(cm):', min = 1, max = 200) 
weight=py.inputFloat('請輸入體重(kg):', min = 1, max = 200)

bmi:float = bmi_show(height,weight) #引數值的呼叫
valu:str = valu_show(bmi)

print(f'\n{name}, 您的BMI: {bmi:.2f}，您是{valu}')