from src.com.python.study.classStudy.Car import Car

if __name__ == '__main__':
    carList = list()

    c1 = Car('현대자동차', '펠리세이드', '화이트')
    c2 = Car('현대자동차', '쏘나타', '블랙')

    carList.append(c1)
    carList.append(c2)

    for carObj in carList:
        # print(carObj)
        print(f'모델명: {carObj.model}')

