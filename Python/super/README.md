# 파이썬의 super의 의미

### Super란?

- Python의 객체지향 프로그래밍을 하다보면 `Class`를 만들어 다른 class에 상속해주는 상황을 마주치게 된다. 간단하게 상속의 개념을 소개하자면 [player.py]('./resource/player.py')에 있는 class를 `부모 객체`라고 하고 [child.py]('./resource/child.py')에 있는 class들을 `자식 개체`라고 하면 자세히 살펴보면 알 수 있듯이 각 `자식 객체`들이 부모 객체인 `Player` class를 상속 받는 것을 알 수 있다

```
...
class Human(Player):
...

...
class Orc(Player):
...

...
class Elf(Player):
...

```

- 이렇게 상속을 받는 경우 `Player` 클래스의 `greet` 메소드를 모든 객체가 상속받게된다.
- 만약 다른 `greet` 구현하고 싶다면 `Orc` 클래스 처럼 새롭게 정의해주면 새로운 `greet`가 만들어 지는데 이를 `Overriding(오버라이딩)`이라고 한다 

```
class Orc(Player):
    def __init__(self, name):
        super().__init__(name)
        self.power = 0

    def greet(self): #오버 라이딩
        print("!@!$@!%!%!@%!@%!@^")

    def bust_up(self):
        print("부수기에 성공했습니다.")
        self.power += 10

```

- 하지만 여기서 중요한 점은 부모 객체의 메소들은 모두 상속이 되지만 `인스턴스 속성`은 자식 객체에 상속이 되지 않는 다는 것이다
- 이게 무슨 말이냐면 `Player` 클래스를 보면 `self.name`, `self.exp`가 만들어져 있지만, 이를 상속받은 자식 객체에서 호출을 하면 해당 attribute가 없다고 나온다

```
 'Elf' object has no attribute 'name'
```

- 왜 상속이 되지 않는 것일까? 이는 `Player` 객체에서 해당 인스터스 속성들이 언제 생성되는지를 생각하면된다.

- 위 예시의 경우넨 `__init__` 라는 매직 메소드가 실행되면성 생성된다. 따라서 이 매직 메소드는 해당 자식 객체에서는 실행된적이 없기 때문에 해당 인스턴스 속성들이 생성되지 않는 것이다 (또는 상속 되지않는 것이다)

- 따라서 이를 자식 클래스의 `__init__` 매직 메소드에 `super().__init__()`으로 실행시키게 되면 문제가 해결된다.


### Super in 다중상속

- 위와 같이 인스턴스 상속 문제 뿐만 아니라 `다중상속`의 문제를 해결하는 것에도 super가 활용된다

- 아래의 예시를 보자

```
class A:
    def __init__(self):
        print('A 클래스 시작')
        print('A 클래스 끝')

class B:
    def __init__(self):
        print('B 클래스 시작')
        print('B 클래스 끝')

class C(A,B):
    def __init__(self):
        print('C 클래스 시작')
        super().__init__()
        print('C 클래스의 끝')

```
- 위와 같이 `C`클래스는 `A와 B`클래스를 동시에 상속 받고 있다
- 따라서 super()의 방법을 생각해보면 부모 객체를 가르켜야하기 때문에 A와 B 모두 호출 해야한다고 생각할  수 있다

- 하지만 실제로 실행해보면 A객체만을 생성한다는 것을 알 수 있다

- 이를 해결하기 위해서는 class A __init__에 super().__init__()을 추가해주면 된다

```
class A:
    def __init__(self):
        print('A 클래스 시작')
        print('A 클래스 끝')
        super().__init__()

class B:
    def __init__(self):
        print('B 클래스 시작')
        print('B 클래스 끝')

class C(A,B):
    def __init__(self):
        print('C 클래스 시작')
        super().__init__()
        print('C 클래스의 끝')
```

- 즉, super는 단순히 부모 객체를 가르키기 위해서인 것이 아니다. (왜냐하면 A의 부모가 B는 아님에도 위 코드는 B를 호출할 수 있기 때문이다)이는 사실 다중 상속 문제를 다루기 위함이다

- 여기서 살펴볼 다중상속의 문제는 다른 말로 `다이아몬드문제이다`

[다이아몬드 문제](https://everyyy.tistory.com/entry/%EC%A3%BD%EC%9D%8C%EC%9D%98-%EB%8B%A4%EC%9D%B4%EC%95%84%EB%AA%AC%EB%93%9C-the-Deadly-Diamond-of-Death-%EB%8B%A4%EC%A4%91%EC%83%81%EC%86%8D%EA%B3%BC-%EA%B7%B8-%EC%9D%B4%EC%95%BC%EA%B8%B0)

- 이러한 다이아몬드 문제를 해결하기 위해서 언어마다 다른 방법을 제안하지만 python의 경우에서는 `MRO(Method Resolution Order)`방법을 지원한다
- 즉, 해당 클래스를 포함하여 관련된 모든 부모 클래스의 실행 순서를 지정하는 방법이다

- 실제 MRO 순서는 print해서 볼 수 있다

```
print(C.mro) # 리스트로 반환

or

print(C.__mro__) # 튜플로 반환

```

- print를 활용한 mro의 경우 아래와 같은 결과가 출력된다

```
[
    <class '__main__.C'>,
    <class '__main__.A'>,
    <class '__main__.B'>,
    <class 'object'>
]
```

- 즉, super의 진정한 의미는 부모 객체가 아니라 mro에서 지정한 순서에서 다음으로 올 객체를 의미하는 것이다 **(call next)**


### 참조 문헌

- [클래스의 super( ) 에 대해 제대로 알아보자! ](https://supermemi.tistory.com/entry/Python-3-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%B4%EB%9E%98%EC%8A%A4%EC%9D%98-super-%EC%97%90-%EB%8C%80%ED%95%B4-%EC%A0%9C%EB%8C%80%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90-superinit-super%EC%9D%98-%EC%9C%84%EC%B9%98)

- [super의 의미(Duet 다중상속)_Pycon korea 2022](https://youtu.be/Gg99y1o5THM)

- [다이아몬드 문제](https://everyyy.tistory.com/entry/%EC%A3%BD%EC%9D%8C%EC%9D%98-%EB%8B%A4%EC%9D%B4%EC%95%84%EB%AA%AC%EB%93%9C-the-Deadly-Diamond-of-Death-%EB%8B%A4%EC%A4%91%EC%83%81%EC%86%8D%EA%B3%BC-%EA%B7%B8-%EC%9D%B4%EC%95%BC%EA%B8%B0)
