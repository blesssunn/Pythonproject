'''
file name : Ex02-6-tuple.py
tuple
    단일 변수에 여러 항목을 저장하는데 사용된다
    순서가 있고, 변경할 수 없는 list
    둥근 괄호로 작성된다 ()
'''

thistuple = ("피카츄", "라이츄", "파이리")
print(thistuple)
# tuple 길이 len()
print(len(thistuple))
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

# tuple 값 변경 방법
thistuple = ("피카츄", "라이츄", "파이리")
thiscast = list(thistuple)
thiscast[1] = "잠만보"
thistuple = tuple(thiscast)
print(thistuple)

# tuple 압축풀기
thistuple = ("피카츄", "라이츄", "파이리", "꼬부기")
(p1, p2, p3, p4) = thistuple
print(type(p1))
print(p2)
print(p3)
print(p4)
# 두개 tuple 조인
thistuple1 = ("피카츄", "라이츄", "파이리", "꼬부기")
thistuple2 = ("버터플", "야도란", "피존투", "또가스")
thistuple3 = thistuple1 + thistuple2
print(thistuple3)
