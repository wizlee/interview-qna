import random

def prac_1():
  a = [i for i in random.randint(0, 20)]
  low, mid, high = [], len(a) // 2, []
  low = a[:mid]
  high = a[mid:]

  print(a)
  print(low)
  print(high)

def prac_2():
  a = [random.randint(0, 19) for _ in range(10)]
  b = [f"even! {i}" if i % 2 == 0 else "Not even" for i in a]

  print(a)
  print(b)

def prac_3():
  test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 5]
  test_set = set(test)

  # using test_set is not compulsory but will make this more performant
  print(max(test_set, key = test.count))

def parrot(voltage, state='a stiff', action='voom'):
  print("-- This parrot wouldn't", action, end=' ')
  print("if you put", voltage, "volts through it.", end=' ')
  print("E's", state, "!")

def prac_4():
  d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
  parrot(**d)

if __name__ == "__main__":
  # prac_1()
  # prac_2()
  # prac_3()
  prac_4()
