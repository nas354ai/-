from utils.profit_analyzer import profit_analyzer

item_price=float(input("請輸入進貨商品價格(RMB):"))
item_weight=float(input("請輸入進貨商品重量(RMB):"))
chinashipping=float(input("請輸入國際運費(rmb):"))

result= profit_analyzer(item_price,item_weight,chinashipping)

print("---毛利30%分析---")
print(f"採購價:{item_price}RMB")
print(f"總成本:{result['總成本']}")
print(f"建議售價:{result['建議售價']}")
print(f"應繳稅收:{result['應繳稅收']}")      
print(f"實拿純利:{result['實拿純利']}")