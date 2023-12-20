try:
    number=int(input("請輸入0~100其中一個數字:"))
    if number < 0 or number > 100:
        assert False,"數字超出範圍了"
    print(number)
    
except AssertionError as ae:
    print(f"發現錯誤:{ae}")
    
except:
    print("有錯誤喔!")
    
else:
    print("正確，繼續執行")
    
finally:
    print("不管有沒有錯，都繼續執行")