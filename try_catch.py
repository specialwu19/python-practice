data=input("請輸入數字：")

try:
    number=int(data) 
    
except Exception as exc:
    print(f"錯誤原因：{exc}")
    number=0

number=number*2
print(number)