# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art

print(art.logo)

def find_highest_bidder(bidding_dictionary):
    max_bid = 0
    max_bidder = ""
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > max_bid:
            max_bid = bidding_dictionary[bidder]
            max_bidder = bidder

    print(f"The winner is {max_bidder}, whose bid is ${max_bid:2}")

done = False
bids = {}

while not done:
    person = input("What is your name? ")
    bid = float(input("How much is your bid? $"))
    bids[person] = bid
    done = "no" == input("Is there any other bidder? (type 'yes' or 'no') ").lower()
    print('\n'*100)

find_highest_bidder(bids)