import csv
prices=[]
with open("datas.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        close_price = float(row[4])
        prices.append(close_price)
prices.reverse()

def calculate_average(prices_list,current_day,window):
    recent_prices = prices_list[current_day-window:current_day]
    total = sum(recent_prices)/window
    average = total/window
    return average
cash= 1000
shares=0
for day in range(20, len(prices)):
    today_price= prices[day]
    fast_avg=calculate_average(prices,day,5)
    slow_avg=calculate_average(prices,day,20)
    if fast_avg>slow_avg and cash>=today_price:
        shares=shares+1
        cash=cash-today_price
        print(f"Day {day}: BOUGHT at {today_price}")
    elif fast_avg< slow_avg and shares>0:
        cash=cash+today_price
        shares=shares-1
        print(f"Day {day}: SOLD at {today_price}")

final_price=prices[-1]
final_portfolio_value= cash+shares*final_price
total_profit= final_portfolio_value-1000



print("\n--- FINAL RESULTS ---")
print(f"Total Portfolio Value: {final_portfolio_value}")
print(f"Total Profit/Loss: {total_profit}")

              
              
            
              
             
