
PI = 3.141592653589793

VERSION = "1.0.8"
_secret = "это скрытая константа"

def circle_area(r):
    return PI * r ** 2

def circle_len(r):
    return 2 * PI * r

def _helper():
    return PI / 2


if __name__ == "__main__":
    print(f"(VERSION) Самопроверка модуля:")
    print("S(r=2)=", circle_area(2))
    print("L(r=2)=", circle_len(2))