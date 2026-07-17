
import asyncio
from concurrent.futures import ProcessPoolExecutor
import time

#cpu-heay task
def heavy_compute(x):
    print(f"Processing {x} ")
    time.sleep(1)
    return x * x

#async I/O task
async def fetch_data(x):
    await asyncio.sleep(1)
    return x

async def main():
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as executor:
        #step1 : fetch concurrently (non blocking)
        data = await asyncio.gather(*(fetch_data(i) for i in range(5)))

        #step2 : Process in Parallel
        results = await asyncio.gather(*(loop.run_in_executor(executor, heavy_compute, d) for d in data))
        print(results)

if __name__ == "__main__":     #always write the if statment
    asyncio.run(main())        

