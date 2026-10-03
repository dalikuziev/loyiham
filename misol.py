try:
    n = " aaa"
    exec(n)
except KeyboardInterrupt:
    print("checksiz sikl tugadi")
except IndentationError and ZeroDivisionError:
    print("ind yoki ty")
except:
    print("qolgan barcha xatolar")
else:
    print("try muvaffaqqiyatli tugadi")
finally:
    print("lboyi")

