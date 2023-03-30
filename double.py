class A:
    def test(self):
        print("test A")

class B(A):
    pass

class C:
    def test(self):
        print("test C")

class D(B,C):
    pass

test = D()
test.test()
print(D.mro())

#다중 상속시, 클래스 호출 순서가 궁구미 D-> C -> B-> A
#호출 순서는 D먼저 뿌리고 그다음이 B 따라서 D로 인스턴스를 만들면  B로 생성댐
#다이아몬드 상속 구조 확인해보기
#이걸 깨기위해서, mro라는 규칙을 사용하는디, 깊이탐색마냥 젤 길이가 긴놈의 인스턴스를 호출하는 것 같음
# 공식문서 뒤져보니 C3 선형화라고 불러지는 알고리즘을 사용하고있다.


