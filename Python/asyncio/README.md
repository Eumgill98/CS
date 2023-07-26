# 파이썬의 비동기 프로그래밍

### 비동기 프로그램이란?

- 전통적으로 동시 프로그래밍(concurrent programming)은 여러개의 쓰레드(thread)를 활용하여 이루어졌는데 이는 직접 코딩해보면 쉽게 이해하겠지만 thread safe하게 작성하는 것은 쉽지가 않다

- 또한 싱글 코어에서는 그렇다할 성능 향상을 보지 못하고 심지어 성능이 떨어지기도 한다

- 이러한 이유에서 최근 **하나의 쓰레드로 동시에 처리하는** `비동기 프로그래밍(asynchronous programming)`이 주목을 받고 있다, 특히 대규모 APP에서 병렬처리 , 통신 , DB 등 다양한 방법에서 효율적으로 활용된다

---

- 코딩을 하다보면 (특히, 웹 서버) CPU 연산 보다는 DB 또는 API와 연동하는 과정에서 발생하는 대기 시간이 길다는 것을 알 수 있다. 비동기 함수는 이러한 대기 시간을 낭비하지 않고 그 시간에 CPU 연산을 하여서 시간을 단축하는 역할을 한다

- JS 와 같이 애초에 비동기 방식으로 설계된 언어에서는 매우 익숙하지만 파이썬은 동기 방식으로 동작하기 때문에 조금은 이해하기 어려울 수 있다

- `Python 3.4` 이후에 `asyncio`라는 표준 라이브러리가 제공되었고 `3.5` 부터는 `async/await`가 적용되면서 외부라이브러리 없이 비동기가 가능해졌다

---

### 비동기 프로그래밍 예제

`./not_asyncio.py`의 경우 동기 방법으로 함수를 실행했을 때 코드 실행에 걸리는 시간을 출력한다

`./asyncio.py`의 경우 비동기 방법으로 함수를 실행했을 때 코드 실행에 걸리는 시간을 출력한다

---

### Base 코드 및 설명 

- 비동기 함수는 `def` 앞에 `async`를 붙여 사용하면 비동기 처리가 된다

```
async def return_zero():
    return 0
```

- 이렇게 만들어진 `비동기 함수`를 일반 함수 처럼 로 호출을 하게 되면 `코루틴` 객체가 반환된다.
```
return_zero()

# <coroutine object do_async at 0x1567se710>

```

- 따라서 일반적으로 `async`로 선언된 다른 비동기 함수 내에서 `await` 키워드를 붙여서 사용하는 것이 일반적인 방법이다

```
async def main():
    await return_zero()
    
```
- 여기서 `await`는 해당 `return_zero()`객체가 끝날 때까지 기다린 다음 결과를 반환한다. 즉, 끝나기 전에 객체를 반환하는 것을 방지하기 위해서 `await`를 사용하는 것이다. 또한 여기서 주의할 점은 `await`의 경우 같은 코루틴 안에서만 사용할 수 있다 위 코드는 `main()` 이라는 코루틴 안에서 활용되고 있다

- 또한 여러 `async`를 사용하기 위해서 `await`를 반복해서 사용하는 것은 매우 귀찮은 일이다. 이를 해결해주기 위해서 `asyncio.gather`를 활용해주면된다

```
async def main():
    await asyncio.gather(
        return_zero(),
        return_zero(),
        return_zero(),
        return_zero(),
    )
```
- 위 방법대로 여러번 사용해야하는경우 한번에 `asyncio.gather`를 활용해서 선언해줄 수 있다

---


- 만약 `async`로 선언되지 않은 일반 동기 함수 내에서 비동기 함수를 호출하기 위해서는 `asyncio`의 이벤트 루프를 이용해야한다

```
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```

- `Python 3.7` 이상 부터는 위의 코드도 매우 불편하기 때문에 간단하게 아래의 방법으로 이용할 수 있다
```
asyncio.run(main()) 
```
---

### async with & for

**1. async with**

[예시코드](./with_for/async_with.py)

- `async with`는 클래스나 함수를 비동기로 처리한 뒤 결과를 반환하는 문법이다

```
async with 클래스() as 변수:
    코드
```
- 위 방법으로 비동기 처리된 클래스를 넣어주고 뒤에 결과를 받을 변수명을 지정해주면 된다

- 그리고 클래스의 경우 `__aenter__`와 `__aexit__`메소드를 클래스에 구현해주어야한다 (asynchronous enter, asynchronous exit라는 뜻)

```
class 클래스이름:
    async def __aenter__(self):
        코드
 
    async def __aexit__(self, exc_type, exc_value, traceback):
        코드
```

---

**2. async for**

[예시 코드](./with_for/async_for.py)

- `async_for`는 `__aiter__`와 `__anext__`메서들를 구현해야한다 (asynchronous iter, asynchronous next라는 뜻)

- 그리고 메서드를 만들때는 반드시 `async def`를 사용해야한다


### 참조 문헌
- [파이썬의 asyncio를 통한 비동기 프로그래밍](https://www.daleseo.com/python-asyncio/)

- [비동기 프로그래밍 동작 원리 (asyncio)](https://it-eldorado.tistory.com/159)

- [파이썬 코딩 도장](https://dojang.io/mod/page/view.php?id=2469)


### 추가로 보면 좋을 문헌
- [Python asyncio Doc](https://docs.python.org/3/library/asyncio.html)