import os
print("******Welcome to the Silent Auction Program******")
def find_winner(bidder_details):
    highest_bid=0
    winner=""
    for bidder in bidder_details:
        price=bidder_details[bidder]
        if price > highest_bid:
            highest_bid=price
            winner=bidder
    print(f"Here is the list of bidder details:{bidder_data}")
    print(f"The winner is  {winner} with a bid price of {highest_bid}")
bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("What is your name?:")
    price=int(input("what is ypur bid?:"))
    bidder_data[name]=price
    more_bidders=input("Are there more bidders? Type 'yes' or 'no':").lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')


        
