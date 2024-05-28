print("AUCTION PROGRAM")

bids = {}
bidding_finished = False

while not bidding_finished:
    bidder = input("Enter your name :")
    bid = int(input("Enter your bid ammount: "))
    bids[bidder] = bid
    should_continue = input("Are there any other users for bidding? Type 'yes' or 'no'..")
    if should_continue.lower() == "no":
        bidding_finished = True
        
#uptil here we have taken names as input and their bid amounts now we have to create a function,
#which will calculate the highest amount of bid and declare that person as the winner...

def highest_bid(bidding_record):
    highest_bid = 0    
    for bidder in bidding_record:
        bid_amount =  bidding_record[bidder]
        if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = bidder
    print(f"The highest bidder is {winner} and the amount of his/her bid is {highest_bid}")   
    
highest_bid(bids)          



    

