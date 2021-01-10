# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
#
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년
#
# [코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.competion_year = completion_year

    def set_house_type(self, house_type):
        # if self.deal_type != deal_type:
        #     self.deal_type = deal_type
        self.house_type = house_type

    def set_deal_type(self, deal_type):
        # if self.deal_type != deal_type:
        #     self.deal_type = deal_type
        self.deal_type = deal_type

    # 매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}년".format(self.location, self.house_type, self.deal_type, self.price, self.competion_year))



seller1 = House("강남", "아파트", "매매", "10억", 2010)
seller2 = House("마포", "오피스텔", "전세", "5억", 2007)
seller3 = House("송파", "오피스텔", "월세", "500/50", 2000)
seller3.set_house_type("빌라")

# print("총 3대의 매물이 있습니다.")
# seller1.show_detail()
# seller2.show_detail()
# seller3.show_detail()

houses = []
houses.append(seller1)
houses.append(seller2)
houses.append(seller3)

print("총 {}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()