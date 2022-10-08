import asyncio
import time
async def fun():
    print("国庆有什么安排？")
    time.sleep(3)
    print("孙笑川吧")
def main():
    f1=fun()
    asyncio.run(f1)
main()