#define Snapchat class

class Snapchat():
    def _init_(self):
        self.earnings = "low"
        self.growthpotential = "high"
        self.news = "bad"

snapchat = Snapchat()
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

#now the game starts, using input functions and if statements, the person progresses through the game
print("Your first assignment is to analyze this case and advise us what to do.")

#AMZN
amzn = input("AMZN is about to release their third quarter earnings report in two days. Should we buy more AMZN or sell all of our shares previous to the release? Type 'buy' or 'sell.'")
if amzn == "buy":
    print("Nice job. AMZN's shares went up 10 percent after the release. We made a lot of money.")
    newline()

    #FTR
    ftr = input("FTR just raised their div yield by 20 percent. Their stock has gone up by 20 percent. Should we short or buy? Type 'short' or 'buy'.")
    if ftr == "short":
        print("Nice job. The company couldn't sustain their 33 percent div yield. They dropped it and we made a lot of money.")
        newline()

        #BITCOIN
        bit = input("Bitcoin is a highly volatile currency. It just went up 4,000 dollars today. Should we buy tomorrow morning or short it? Type 'buy' or 'short'.")
        if bit == "buy":
            print("The currency went down by 2,000 dollars. Our investors panicked and withdrew some of their money. That was an awful decision.")
            print("You're fired.")

        if bit == "short":
            print("Nice work! The currency went down 2,000 dollars and we made a lot of money by shorting it.")

            #ARK COIN
            ark = input("ArkCoin is a new crytocurrency. They have a CEO with a vision. Currently, each Arkcoin is equal to 50 cents. Should we invest in Arkcoin and take the risk or leave it? Type 'leave' or 'invest'.")
            if ark == "invest":
                print("Excellent choice. Arkcoin has gone up to 10 dollars; we've made tons of money. You are promoted to associate.")
                newline()
                print("As associate, you will be trusted with harder decisions and asked to make tough decisions.")

                #APPLE
                apple=input("Apple's going to unveil their latest design tomorrow. Should we buy more right now or sell? Type 'buy' or 'sell'.")
                if apple == "buy":
                    print("Apple's latest design turned off investors. We lost a lot of money from our shares. Bad job.")

                    #VERIZON
                    verizon=input("Net neutrality decision is coming out tomorrow. Speculation says it will be repealed. Should we buy or sell now?")
                    if verizon == "buy":
                        print("Good job. Investors saw that their profits would rise and the price shot up.")

                    if verizon == "sell":
                        print("Verizon's stock shot up and we missed out.")
                        print("You have been demoted to Analyst.")

                        #J.C. PENNEY
                        jc=input("J.C Penney is up quite a bit today; people are excited about it, but it's also really volatile and took losses of up to 30 percent last quarter. Buy or Sell?")
                        from random import randint
                        for x in range(1):
                             print(randint(0,10))
                        if x < 5:
                            print("Your decision was bad.")
                            print("You're fired,", name)
                        if x >= 5:
                            print("Good decision.")

                            #TESLA
                            tesla=input("Tesla is coming out with their earnings report for the first quarter of 2018 tomorrow. Buy or short?")
                            if tesla == "buy":
                                print("Unfortunately, Tesla came out with an awful report and their stock dipped by more than 20 percent. I'm ashamed of you.")
                                print("You're fired,", name)
                            if tesla == "short":
                                print("You're making me a lot of money,", name)

                if apple == "sell":
                    print("Never thought I'd say this, but that was the right choice. Apple's stock dipped when investors realized their new design doesn't have wireless charging.")
                    newline()

                    #MCDONALD'S
                    mcdonald=input("ObamaCare will be in effect soon and employers can opt to not provide healthcare to employees if they work less than 40 hours. Should we buy their McDonald's stock for the long run? Type 'yes' or 'no'.")
                    if mcdonald == "yes":
                        print("I'm glad we hired you. Their stock has been slowly rising.")

                    if mcdonald == "no":
                        print("We missed out on investing on a power stock; it's been rising a lot. But, that's alright.")

            if ark == "leave":
                print("We trusted your analysis and you let us down. Arkcoin has been booming. But, it's okay. Just take more risks in the future.")
    if ftr == "buy":
        print("Not the best decision. After some growth, the company lowered their dividend by 20 percent and their stock went down. We lost money.")
        nextftr = input("Should we wait for their stock to show some growth again or sell and take our losses? Type 'wait' or 'sell'.")
        if nextftr == "wait":
            print("That was a good decision. Their stock rebounded and we sold for a profit. Not so bad.")
            newline()
            print("You are promoted to associate.")

            #BITCOIN2
            bit2 = input("Bitcoin went up by 3,000 dollars today. Should we short it tomorrow or buy it? Type 'short' or 'buy'.")
            if bit2 == "short":
                print("Their stock went down. We made some money. Nice job. You are promoted to associate.")

                #VANGUARD ETF
                vanguard=input("Usually we don't invest in ETF's but our analysts are saying that the Fed is going to lower rates. Should we invest in some Vanguard S&P 500 ETF's or not? Type 'leave' or 'invest'.")
                if vanguard == "invest":
                    print("Nice job, they lowered rates and the market is booming. S&P is blowing up.")

                   #Snapchat questions (not actual investing), leads to promotion or them getting fired.

                    print("Now, you will be asked to do research and provide the following information to your managers. If your information clashes with the majority of your other associates, you will be fired.")
                    snapchat2=input("How have the past earning reports for Snapchat been? Type 'low' or 'high.'")
                    # if snapchat2 == snapchat.earnings:
                    if snapchat2 == 'low':
                        print("Nice job.")
                        newline()
                        snapchat3=input("How does the growth potential of Snapchat Inc. look? Type 'high' or 'low'.")
                        if snapchat3 == "high":
                            print("Nice job, your analysis was correct.")
                            snapchat4=input("How does has recent news been regarding Snapchat Inc.? Type 'good' or 'bad'.")

                            if snapchat4 == "bad":
                                print("You're correct. Good job.")
                                newline()
                                print("You've been promoted to Portfolio Manager. Congratulations.")

                            if snapchat4 == "good":
                                print("That is wrong. Do your research.")
                                print("You're fired.")

                        if snapchat3 == "low":
                            print("Unfortunately, this is wrong. All analysis and reporting shows the oppposite.")
                            print("You're fired.")


                    if snapchat2 == 'high':
                    # if snapchat2 != snapchat.earnings:
                        print("This is wrong.")
                        newline()
                        print("You're fired.")

                if vanguard == "leave":
                    print("We missed out on a great opportunity. Take risks. Listen to your analysts.")

                    #BOFA
                    bofa=input("We have heard rumours of a bank run happening at BoFA in California. Should we short their stock or leave it? Type 'short' or 'leave'.")
                    from random import randint
                    for u in range(1):
                        print(randint(0,100))

                        #FIRED
                        if u > 50:
                            print("Good decision.")
                            print("Unfortunately, your competition has been very good and we need to cut down.")
                            newline()
                            print("You're fired.")

                        #FIRED
                        if u <= 50:
                            print("Bad decision.")
                            newline()
                            print("You're fired.")
            #FIRED
            if bit2 == "buy":
                print("Their stock went down and we lost a lot of money. You're fired.")
        #FIRED
        if nextftr == "sell":
            print("Awful decision. The stock rebounded. We lost money on this deal. That was your last chance. You're fired.")

#END GAME at beginning (FIRED)
if amzn == "sell":
    print("You got it wrong. We missed out on making a lot of money. You're fired.")
