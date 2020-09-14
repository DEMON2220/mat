import cProfile as cpr
import oop
import timeit


if __name__ == "__main__":
 cpr.run('''
g = oop.Good("Max")
g.sayHello()
''')



print(timeit.timeit(f"{g.sayHello()}"))



print("""


""")
start_time = time.time()  
# oop.Bad.area(9,8)
g = oop.Good("Max")
end_time = time.time() - start_time
print(f'Time : {end_time}')