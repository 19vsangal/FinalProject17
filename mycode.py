print("Welcome to Money Manager!")
def newline():
    input("Please click enter to move on.")
newline()
print("Welcome to Money Manager Hedge Fund. We are one of the famous hedge funds in the country.")
name = input("What's your name?")
print("Nice to meet you,", name)
newline()
print("Don't screw up or you will get moved down a position. If you lose us too much money, you can also lose your job.")
print("Your ultimate goal is to beat out your colleagues for CEO. Good luck.")
newline()
print("Your first assignment is to analyze this case and advise us what to do.")
amzn = input("AMZN is about to release their third quarter earnings report in two days. Should we buy more AMZN or sell all of our shares previous to the release? Type 'buy' or 'sell.'")
if amzn == "buy":
    print("Nice job. AMZN's shares went up 10 percent after the release. We made a lot of money.")
    newline()
    ftr = input("FTR just raised their div yield by 20 percent. Their stock has gone up by 20 percent. Should we short or buy? Type 'short' or 'buy'.")
    if ftr == "short":
        print("Nice job. The company couldn't sustain their 33 percent div yield. They dropped it and we made a lot of money.")

    if ftr == "buy":
        print("Not the best decision. After some growth, the company lowered their dividend by 20 percent and their stock went down. We lost money.")
        nextftr = input("Should we wait for their stock to show some growth again or sell and take our losses? Type 'wait' or 'sell'.")
        if nextftr == "wait":
            print("That was a good decision. Their stock rebounded and we sold for a profit. Not so bad.")

        if nextftr == "sell":
            print("Awful decision. The stock rebounded. We lost money on this deal. That was your last chance. You're fired.")
if amzn == "sell":
    print("You got it wrong. We missed out on making a lot of money. You're fired.")
