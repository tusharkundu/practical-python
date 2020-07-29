# pcost.py
#
# Exercise 1.27

import csv
import sys
# #List for storing stock information
# stocks = []

# #Read in data
# with open('Data/portfolio.csv', 'rt') as f:
#     for line in f:
#         row = line.split(',')
#         stocks.append(row)

# #Number of stocks
# num_stocks = len(stocks)

# #Initialize
# cost = 0

# #Add cost of all stocks
# for stock in range(1,num_stocks):
#     num_shares = int(stocks[stock][1]) 
#     stock_price = float(stocks[stock][2])
#     stock_cost = num_shares * stock_price 
#     cost += stock_cost
    
# print('Total cost', cost)

def portfolio_cost(filename):
    #List for storing stock information
    stocks = []
    
    
    #Read in data
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stocks.append(row)
    
    #Number of stocks
    num_stocks = len(stocks)
    
    #Initialize
    cost = 0
    
    #Add cost of all stocks
    for stock in range(1,num_stocks):
        try:
            num_shares = int(stocks[stock][1]) 
            stock_price = float(stocks[stock][2])
            stock_cost = num_shares * stock_price 
            cost += stock_cost
        except ValueError:
            print("Couldn't parse", stocks[stock])
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'  
    
cost = portfolio_cost(filename)
print('Total cost:', cost)

