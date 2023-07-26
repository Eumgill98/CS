import asyncio


## async with
"""
async with 클래스() as 변수:
    코드

---

class 클래스이름:
    async def __aenter__(self):
        코드
 
    async def __aexit__(self, exc_type, exc_value, traceback):
        코드
---

"""
class AsyncAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    async def __aenter__(self):
        await asyncio.sleep(1.0)
        return self.a + self.b
    
    # __aenter__에서 값을 반환하면 as에 지정한 변수에 들어감
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        pass


async def main():
    async with AsyncAdd(1, 2) as result:
        print(result)

asyncio.run(main()) 
