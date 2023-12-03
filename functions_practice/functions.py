
def hello():
  print("Hello, user!")

def pack(l1,l2,l3):
  return [l1,l2,l3]

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("there is no food here?")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"The collapse of humanity has driven me to pyschotic delusions, my first meal in attempt of a cleansing myself from this world will be {my_lst[0]}")
      else:
        print(f"yay more foood, i want {my_lst[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])