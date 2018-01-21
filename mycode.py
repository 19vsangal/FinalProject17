#define Snapchat class, this will be used in one section of the game where the user has to answer questions
#their will be checked against the components of this class for accuracy

class Snapchat():
    def _init_(self):
        self.earnings = "low"
        self.growthpotential = "high"
        self.news = "bad"

snapchat = Snapchat()

#make "leaderboards" using dictionaries with names as keys and numbers as values
#these leaderboards will be throughout the game to demonstrate to the user where they "rank" among colleagues because their goal is to get CEO.
leaderboard1 = {"chris" : "1", "john" : "2", "patricia" : "3", "susan": "4", "janet":"5", "You": "6"}
leaderboard2 = {"john" : "1", "chris" : "2", "susan" : "3", "patricia" : "4", "You" : "5", "janet":"6"}
leaderboard3 = {"john": "1", "susan": "2", "patricia": "3","You" : "4", "janet": "5", "chris" : "6"}
leaderboard4 = {"You" : "1", "susan": "2", "patricia" : "3", "janet" : "4", "chris" : "5", "john" : "6"}

# introduce the game using print
print("Welcome to Money Manager!")

#define a function that allows the user to press enter to move to the next line
#I will use this function throughout the game in order to provide the user with less crowding of lines and for a neat user-interface
def newline():
    input("Please click enter to move on.")
newline()

#further introduction that explains how the game works
print("Welcome to Money Manager Hedge Fund. We are one of the famous hedge funds in the country.")

# using an input function to have the person's name. Makes the game more personable.
#defining the input function as name and then using "name" in a print function to address the user
name = input("What's your name?")
print("Nice to meet you,", name)
newline()

#A series of print functions to introduce the user to the game
print("The object of the game is to answer each question correctly. If you answer multiple questions correctly, you get promoted.")
print("Don't screw up or you will get moved down a position. If you lose us too much money, you can also lose your job.")
print("Your ultimate goal is to beat out your colleagues for CEO. Good luck.")
newline()

#now the game starts, using input functions and if statements, the person progresses through the game
print("Your first assignment is to analyze this case and advise us what to do.")

#AMZN input function
amzn = input("AMZN is about to release their third quarter earnings report in two days. Should we buy more AMZN or sell all of our shares previous to the release? Type 'buy' or 'sell.'")
#These type of while loops will be used frequently throughout the game in order to ensure that if the user makes an error whilst typing (continued on next line)
#They can correct their spelling or case because the while loop uses the "not in" command
while amzn not in ("buy", "sell"):
    amzn=input("AMZN is about to release their third quarter earnings report in two days. Should we buy more AMZN or sell all of our shares previous to the release? Type 'buy' or 'sell.'")
if amzn == "buy":
    print("Nice job. AMZN's shares went up 10 percent after the release. We made a lot of money.")
    newline()

    #FTR input function
    ftr = input("FTR just raised their div yield by 20 percent. Their stock has gone up by 20 percent. Should we short or buy? Type 'short' or 'buy'.")
    while ftr not in ("short", "buy"):
        ftr=input("FTR just raised their div yield by 20 percent. Their stock has gone up by 20 percent. Should we short or buy? Type 'short' or 'buy'.")
    if ftr == "short":
        print("Nice job. The company couldn't sustain their 33 percent div yield. They dropped it and we made a lot of money.")
        newline()

        #BITCOIN input function
        bit = input("Bitcoin is a highly volatile currency. It just went up 4,000 dollars today. Should we buy tomorrow morning or short it? Type 'buy' or 'short'.")
        while bit not in ("buy", "short"):
            bit=input("Bitcoin is a highly volatile currency. It just went up 4,000 dollars today. Should we buy tomorrow morning or short it? Type 'buy' or 'short'.")
        if bit == "short":
            print("Nice work! The currency went down 2,000 dollars and we made a lot of money by shorting it.")

            #ARK COIN input function
            ark = input("ArkCoin is a new crytocurrency. They have a CEO with a vision. Currently, each Arkcoin is equal to 50 cents. Should we invest in Arkcoin and take the risk or leave it? Type 'leave' or 'invest'.")
            while ark not in ("leave","invest"):
                ark = input("ArkCoin is a new crytocurrency. They have a CEO with a vision. Currently, each Arkcoin is equal to 50 cents. Should we invest in Arkcoin and take the risk or leave it? Type 'leave' or 'invest'.")
            if ark == "invest":
                print("Excellent choice. Arkcoin has gone up to 10 dollars; we've made tons of money. You are promoted to associate.")
                newline()
                print("As associate, you will be trusted with harder decisions and asked to make tough decisions.")

                #APPLE input function
                apple=input("Apple's going to unveil their latest design tomorrow. Should we buy more right now or sell? Type 'buy' or 'sell'.")
                while apple not in ("buy","sell"):
                    apple=input("Apple's going to unveil their latest design tomorrow. Should we buy more right now or sell? Type 'buy' or 'sell'.")
                if apple == "buy":
                    print("Apple's latest design turned off investors. We lost a lot of money from our shares. Bad job.")

                    #VERIZON input function
                    verizon=input("Net neutrality decision is coming out tomorrow. Speculation says it will be repealed. Should we buy or sell now?")
                    while verizon not in ("buy", "sell"):
                        verizon=input("Net neutrality decision is coming out tomorrow. Speculation says it will be repealed. Should we buy or sell now?")
                    if verizon == "buy":
                        print("Good job. Investors saw that their profits would rise and the price shot up.")
                        #BOEING input function
                        boeing=input("Is Boeing a risky stock? Say 'yes' or 'no'.")
                        while boeing not in ("yes", "no"):
                             boeing=input("Is Boeing a passive stock or a volatile stock? Say 'yes' or 'no'.")
                        if boeing == "yes":
                            print("That is wrong. Over time, it has been shown that Boeing is not a volatile stock and is good for investors who like long-term appreciation.")
                            print("The fact that you answered such a simple question incorrectly makes me question whether you are fit to be a part of our firm.")
                            print("You're fired.")
                        if boeing == "no":
                            print("Good job.")
                            newline()
                            print("Below are the rankings of you and your colleagues. If you want to replace me as CEO, you must be number one.")
                            print(leaderboard3.items())

                            #Acadia Pharmaceuticals. Making this one more randomized to replicate actual market
                            pharma=input("The results of Acadia Pharma's trial come out today. Should we 'short' or 'buy'?")
                            while pharma not in ("short", "buy"):
                                pharma=input("The results of Acadia Pharma's trial come out today. Should we 'short' or 'buy'?")
                            #using the random integer function and for loops, I can randomize the game a little. But, I make the odds less in their favor
                            #The odds are very much skewed so that the user is likely to lose because this simulates the danger of investing
                            #to use random int function, i first have to import randint from random
                            from random import randint
                           #then, by using for loop and if statements I can make the game provide the user with a result
                            for x in range(1):
                                print(randint(0,100))
                                if x < 90:
                                    print("Unfortunately, your decision lost us a lot of money.")
                                    newline()
                                    print("Due to your inability to compete with your competition, you have been fired.")
                                    print("You were last among your colleagues in terms of ranking of earnings.You would have had zero chance at becoming CEO.")
                                    print(leaderboard1.items())
                                if x >= 90:
                                    print("Great decision. We made a lot of money. You have been promoted to Portfolio Manager.")

                    if verizon == "sell":
                        print("Verizon's stock shot up and we missed out.")
                        print("You have been demoted to Analyst.")

                        #J.C. PENNEY input function
                        jc=input("J.C Penney is up quite a bit today; people are excited about it, but it's also really volatile and took losses of up to 30 percent last quarter. Buy or Sell?")
                        #Randomize using the random integer and then using for loops
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
                            while tesla not in ("buy", "short"):
                                tesla=input("Tesla is coming out with their earnings report for the first quarter of 2018 tomorrow. Buy or short?")
                            if tesla == "buy":
                                print("Unfortunately, Tesla came out with an awful report and their stock dipped by more than 20 percent. I'm ashamed of you.")
                                print("You're fired,", name)
                            if tesla == "short":
                                print("You're making me a lot of money,", name)
                                print("You've been promoted to Portfolio Manager. Congratulations.")

                                #Use dictionary to give the user their "ranking"
                                print("I want to update you on your earnings compared to your fellow colleagues. Remember you want to beat these guys, so you can be up there.")
                                print("Here are the current rankings. The number one gets picked to be CEO.")
                                print(leaderboard1.items())


                if apple == "sell":
                    print("Never thought I'd say this, but that was the right choice. Apple's stock dipped when investors realized their new design doesn't have wireless charging.")

                    #MCDONALD'S input function
                    mcdonald=input("ObamaCare will be in effect soon and employers can opt to not provide healthcare to employees if they work less than 40 hours. Should we buy their McDonald's stock for the long run? Type 'yes' or 'no'.")
                    while mcdonald not in ("yes","no"):
                        mcdonald=input("ObamaCare will be in effect soon and employers can opt to not provide healthcare to employees if they work less than 40 hours. Should we buy their McDonald's stock for the long run? Type 'yes' or 'no'.")
                    if mcdonald == "yes":
                        print("I'm glad we hired you. Their stock has been slowly rising.")
                        print("You've been promoted to Portfolio Manager.")

                    if mcdonald == "no":
                        print("We missed out on investing on a power stock; it's been rising a lot. But, that's alright.")
                        newline()
                        johnson=input("Is Johnson and Johnson a buy? Type 'yes' or 'no'.")
                        while johnson not in ("yes", "no"):
                            johnson=input("Is Johnson and Johnson a buy? Type 'yes' or 'no'.")
                        if johnson == "yes":
                            print("Nice job. Our friends at the Fool agree with you.")

                        if johnson == "no":
                            print("That's wrong. You haven't been showing good decision-making these past few times.")
                            print("I'm sorry, but you're fired.")

            if ark == "leave":
                print("We trusted your analysis and you let us down. Arkcoin has been booming. But, it's okay. Just take more risks in the future.")
            #FINISH THIS ONE
    if ftr == "buy":
        print("Not the best decision. After some growth, the company lowered their dividend by 20 percent and their stock went down. We lost money.")

        #NEXT FTR input function
        nextftr = input("Should we wait for their stock to show some growth again or sell and take our losses? Type 'wait' or 'sell'.")
        while nextftr not in ("wait", "sell"):
            nextftr=input("Should we wait for their stock to show some growth again or sell and take our losses? Type 'wait' or 'sell'.")
        if nextftr == "wait":
            print("That was a good decision. Their stock rebounded and we sold for a profit. Not so bad.")
            newline()
            print("You are promoted to associate.")

            #BITCOIN2 input function
            bit2 = input("Bitcoin went up by 3,000 dollars today. Should we short it tomorrow or buy it? Type 'short' or 'buy'.")
            while bit2 not in ("short", "buy"):
                bit2=input("Bitcoin went up by 3,000 dollars today. Should we short it tomorrow or buy it? Type 'short' or 'buy'.")
            if bit2 == "short":
                print("Their stock went down. We made some money. Nice job. You are promoted to associate.")

                #VANGUARD ETF input function
                vanguard=input("Usually we don't invest in ETF's but our analysts are saying that the Fed is going to lower rates. Should we invest in some Vanguard S&P 500 ETF's or not? Type 'leave' or 'invest'.")
                while vanguard not in ("leave", "invest"):
                    vanguard=input("Usually we don't invest in ETF's but our analysts are saying that the Fed is going to lower rates. Should we invest in some Vanguard S&P 500 ETF's or not? Type 'leave' or 'invest'.")
                if vanguard == "invest":
                    print("Nice job, they lowered rates and the market is booming. S&P is blowing up.")

                   #Snapchat questions (not actual investing), leads to promotion or them getting fired.

                    print("Now, you will be asked to do research and provide the following information to your managers. If your information clashes with the majority of your other associates, you will be fired.")
                    snapchat2=input("How have the past earning reports for Snapchat been? Type 'low' or 'high.'")
                    # if snapchat2 == snapchat.earnings:
                    while snapchat2 not in ("low", "high"):
                        snapchat2=input("How have the past earning reports for Snapchat been? Type 'low' or 'high.'")
                    if snapchat2 == 'low':
                        print("Nice job.")
                        snapchat3=input("How does the growth potential of Snapchat Inc. look? Type 'high' or 'low'.")
                        while snapchat3 not in ("high", "low"):
                            snapchat3=input("How does the growth potential of Snapchat Inc. look? Type 'high' or 'low'.")
                        if snapchat3 == "high":
                            print("Nice job, your analysis was correct.")
                            snapchat4=input("How does has recent news been regarding Snapchat Inc.? Type 'good' or 'bad'.")
                            while snapchat4 not in ("good", "bad"):
                                snapchat4=input("How does has recent news been regarding Snapchat Inc.? Type 'good' or 'bad'.")
                            if snapchat4 == "bad":
                                print("You're correct. Good job.")
                                newline()
                                print("You've been promoted to Portfolio Manager. Congratulations.")
#FINISH THIS ONE
                            #FIRED
                            if snapchat4 == "good":
                                print("That is wrong. Do your research.")
                                print("You're fired.")
                        #FIRED
                        if snapchat3 == "low":
                            print("Unfortunately, this is wrong. All analysis and reporting shows the oppposite.")
                            print("You're fired.")

                    #FIRED
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
        if bit == "buy":
            print("The currency went down by 2,000 dollars. Our investors panicked and withdrew some of their money. That was an awful decision.")
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
