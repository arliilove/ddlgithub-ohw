#使用给定的宽度打印格式化后的价格列表

width = input("Please enter width: ")

price_width = 10
item_width = int(width) - price_width

header_format = "%-*s%*s"
format1 = "%-*s%*.2f"

print ("=" * int(width))
print (header_format % (item_width, 'Item', price_width, 'Price'))

print ("-" * int(width))

print (format1 % (item_width,"Apples",price_width,0.4))
print (format1 % (item_width,"Pears",price_width,0.5))
print (format1 % (item_width,"Cantaloupes",price_width,1.92))
print (format1 % (item_width,"Dried Apricots(16 oz)",price_width,8))
print (format1 % (item_width,"Prunes(4 1bs)",price_width,12))

print ("=" * int(width))
