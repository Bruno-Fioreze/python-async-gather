
import asyncio

# A co-routine
async def add(x: int, y: int):
    return x + y

# Create a function to schedule co-routines on the event loop
# then print results
async def get_results():
    inputs = [(2,3), (4,5), (5,5), (7,2)]

    # Create a co-routine list
    cors = [add(x,y) for x,y in inputs]
    results = asyncio.gather(*cors)

    print(await results) # Prints [5, 9, 10, 9]

asyncio.run(get_results())
