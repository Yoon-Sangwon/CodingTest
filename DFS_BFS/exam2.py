# 재귀 함수

'''
def recursive_function():
    print("재귀함수 호출")
    recursive_function()

recursive_function()
'''

def factorial(n):
    if n <= 1:
        return 1  # 종료조건 작성 매우 중요!
    return n * factorial(n-1)

print(factorial(5))