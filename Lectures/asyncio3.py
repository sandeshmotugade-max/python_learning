
import asyncio
import time

#blocaking tasks:
def parse_data(data):
    print(f"Parsing data: {data}")
    time.sleep(2)  # Simulate a blocking operation
    return f"Parsed {data}"

#async task:
async def fetch_data(id):
     print(f"fetching_data{id}")
     await asyncio.sleep(1)
     return f"Data{id}"

async def main():
     start = time.perf_counter()
     tasks = []

     for i in range(5):
          
          #step1: async fetch
          data = await fetch_data(i)

          #step2: run bolcking parse in a thread
          parsed = asyncio.to_thread(parse_data, data)
          tasks.append(parsed)

     results = await asyncio.gather(*tasks)
     end = time.perf_counter()
     print(results)
     print(f"\n Total execution time: {end - start:.2f} ") 

asyncio.run(main())