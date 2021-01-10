# Quiz) 변수를 이용하여 다음 문장을 출력하시오.
#
# 변수명 : station
#
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
#
# 출력 문장 : xx 행 열차가 들어오고 있습니다.

# station = ["사당", "신도림", "인천공항"]
# for i in station:
#     print(i, "행 열차가 들어오고 있습니다.")

station = "사당"
print("{} 행 열차가 들어오고 있습니다.".format(station))
station = "신도림"
print("{} 행 열차가 들어오고 있습니다.".format(station))
station = "인천공항"
print("{} 행 열차가 들어오고 있습니다.".format(station))