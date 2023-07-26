import time
import asyncio

async def good_night():
    await asyncio.sleep(1)
    print('Good night')

async def main():
    await asyncio.gather(
        good_night(),
        good_night()
    )


print(f"start : {time.strftime('%X')}")
asyncio.run(main())
print(f"end : {time.strftime('%X')}")
