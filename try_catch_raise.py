try:
    number=int(input("請輸入0~10其中一個數字:"))
    if number < 0 or number > 10:
        raise ValueError("數字超出範圍了")
    print(number)
    
except ValueError as ve:
    print(f"出現錯誤:{ve}")
    
except:
    print("有錯誤喔!")