# introduce the game using the print function
print("Welcome to Money Manager!")
#define a function that allows the user to press enter to move to the next line
def newline():
    input("Please click enter to move on.")
newline()
#further introduction that explains how the game works
print("Welcome to Money Manager Hedge Fund. We are one of the famous hedge funds in the country.")
# using an input function to have the person's name. Makes the game more personable.
name = input("What's your name?")
print("Nice to meet you,", name)
newline()
#The rules to this game
print("Don't screw up or you will get moved down a position. If you lose us too much money, you can also lose your job.")
print("Your ultimate goal is to beat out your colleagues for CEO. Good luck.")
newline()
print("Your first assignment is to analyze this case and advise us what to do.")
amzn = input("AMZN is about to release their third quarter earnings report in two days. Should we buy more AMZN or sell all of our shares previous to the release? Type 'buy' or 'sell.'")
if amzn == "buy" or "'buy'":
    #scenario 1
    print("Nice job. AMZN's shares went up 10 percent after the release. We made a lot of money.")
    newline()
    ftr = input("FTR just raised their div yield by 20 percent. Their stock has gone up by 20 percent. Should we short or buy? Type 'short' or 'buy'.")
    if ftr == "short" or "'short'":
        print("Nice job. The company couldn't sustain their 33 percent div yield. They dropped it and we made a lot of money.")
        newline()
        bit = input("Bitcoin is a highly volatile currency. It just went up 4,000 dollars today. Should we buy tomorrow morning or short it? Type 'buy' or 'short'.")
        if bit == "buy" or "'buy'":
            print("The currency went down by 2,000 dollars. Our investors panicked and withdrew some of their money. That was an awful decision.")
            print("You're fired.")

            newline()



        if bit == "short" or "'short'":
            print("Nice work! The currency went down 2,000 dollars and we made a lot of money by shorting it.")
            ark = input("ArkCoin is a new crytocurrency. They have a CEO with a vision. Currently, each Arkcoin is equal to 50 cents. Should we invest in Arkcoin and take the risk or leave it? Type 'leave' or 'invest'.")
            if ark == "invest" or "'invest'":
                print("Excellent choice. Arkcoin has gone up to 10 dollars; we've made tons of money. You are promoted to associate.")
                newline()
                print("As associate, you will be trusted with harder decisions and asked to make tough decisions.")
                apple=input("Apple's going to unveil their latest design tomorrow. Should we buy more right now or sell? Type 'buy' or 'sell'.")
                if apple == "buy" or "'buy'":
                    print("Apple's latest design turned off investors. We lost a lot of money from our shares. Bad job.")
                    verizon=input("Net neutrality decision is coming out tomorrow. Speculation says it will be repealed. Should we buy or sell now?")
                    if verizon == "'buy'" or "buy":
                        print("Good job. Investors saw that their profits would rise and the price shot up.")

                    if verizon == "'sell'" or "sell":
                        print("Verizon's stock shot up and we missed out.")

                        newline()
                        print("You have been demoted to Analyst.")
                        jc=input("J.C Penney is up quite a bit today; people are excited about it, but it's also really volatile and took losses of up to 30 percent last quarter. Buy or Sell?")


                if apple == "sell" or "'sell'":
                    print("Never thought I'd say this, but that was the right choice. Apple's stock dipped when investors realized their new design doesn't have wireless charging.")
                    newline()


            if ark == "leave" or "'leave'":
                print("We trusted your analysis and you let us down. Arkcoin has been booming. But, it's okay. Just take more risks in the future.")
    if ftr == "buy" or "'buy'":
        print("Not the best decision. After some growth, the company lowered their dividend by 20 percent and their stock went down. We lost money.")
        nextftr = input("Should we wait for their stock to show some growth again or sell and take our losses? Type 'wait' or 'sell'.")
        if nextftr == "wait" or "'wait'":
            print("That was a good decision. Their stock rebounded and we sold for a profit. Not so bad.")
            newline()
            print("You are promoted to associate.")
            bit2 = input("Bitcoin went up by 3,000 dollars today. Should we short it tomorrow or buy it? Type 'short' or 'buy'.")
            if bit2 == "short" or "'short'":
                print("Their stock went down. We made some money. Nice job. You are promoted to associate.")

            if bit2 == "buy" or "'buy'":
                print("Their stock went down and we lost a lot of money. You're fired.")

        if nextftr == "sell" or "'sell'":
            print("Awful decision. The stock rebounded. We lost money on this deal. That was your last chance. You're fired.")
#scenario 2
if amzn == "sell" or "'sell'":
    print("You got it wrong. We missed out on making a lot of money. You're fired.")
