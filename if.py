weather = ["맑음", "눈", "비", "미세먼지"]

for weather in weather:
    print("오늘 날씨는 '{0}' 입니다.".format(weather))
    if weather == "비" or weather == "눈":
        print("우산을 챙기세요")
    elif weather == "미세먼지":
        print("마스크를 챙기세요")
    else:
        print("준비물이 필요 없습니다")

temp = int(input("기온은 어떤가요?"))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")