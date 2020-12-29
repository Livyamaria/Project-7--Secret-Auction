new_secret={}
end_of_bid = False


def secret(new_secret):
    score=0

    # bidding_record = {"Angela": 123, "James": 321}
    for keys in new_secret:

        if  new_secret[keys] > score :
            score = new_secret[keys]

    print(f"The winner is {keys} with a bid of ${score}")


while not end_of_bid:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    new_secret[name]=bid
    result = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if result == "no":
        end_of_bid = True
        secret(new_secret)
    else :
        result == "yes"



