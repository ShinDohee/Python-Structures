# 변수
x = 10  # 정수형
y = 3.14  # 실수형
name = "Alice"  # 문자열
is_active = True  # 불리언 (참/거짓)

# 2. 연산자
a = 5
b = 2
print(a + b)  # 덧셈: 7
print(a - b)  # 뺄셈: 3
print(a * b)  # 곱셈: 10
print(a / b)  # 나눗셈: 2.5
print(a // b)  # 몫: 2
print(a % b)  # 나머지: 1
print(a ** b)  # 거듭제곱: 25

print(a > b)  # True
print(a == b)  # False
print(a != b)  # True

#3. 조건문
x = 10
if x > 5:
    print("x는 5보다 큽니다.")
elif x == 5:
    print("x는 5입니다.")
else:
    print("x는 5보다 작습니다.")

#4. 반복문
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4 출력

count = 0
while count <5:
    print(count)
    count += 1

# 5. 리스트
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple 출력
fruits.append("orange")  # 리스트에 요소 추가
print(fruits)  # ["apple", "banana", "cherry", "orange"]

# 6. 함수
def greet(name):
    return "Hello, " + name

print(greet("Alice"))  # "Hello, Alice" 출력

# 7. 입력과 출력
# 출력: print() 함수로 값을 출력할 수 있습니다.
# 입력: input() 함수로 사용자 입력을 받을 수 있습니다.
name = input("이름을 입력하세요: ")
print("Hello, " + name)


# 8. 모듈
import math
print(math.sqrt(16))  # 4.0 출력
