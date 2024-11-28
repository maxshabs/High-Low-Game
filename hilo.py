import time

low = 1
high = 1000

art = """                                        .                   
                                       -%%#-                
                                   *%%%#####%=              
                                   #%%%##%%%%%#-            
             ::::                  =%%#***##%%%%#.          
          .::::::::               :%%#++:.....*##.          
          :::   :::.               :#*:::.=##=%%#           
               .:::                  .+%:..%@:-+:           
              ::::                   ..::....:.::           
             :::                     .:..:.....:            
              ::                 .:...:......::             
               :                .::::    :==-               
              :::              ..::.:--==:::---:.           
                               ::. -======+========:        
                              .::.-======-:==========.      
                             .::.-=======--======+====-     
                             ...:==+============++++===-    
                            .::.-=============+++=:++=:     
                            .:.-==:.+++++++++++++: .-:.     
                            :::-=. .+++++++++++++   ...     """
for line in art.splitlines():
    print(line)
    time.sleep(0.05)
print("Welcome! I will guess the number you think off")
time.sleep(0.4)
print("Think of a number between {} and {}, I will get it in less than "
      "10 guesses".format(low, high))
input("Press ENTER to start")

guess = 0
guesses = 1
while low != high:
    if guesses > 10:
        print("You are wrong! This is not possible.")
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I higher or lower? Enter H or L,"
                     " or C if my guess was correct: ".format(guess))
    if high_low.casefold() == "h":
        # Guess higher. The low end of the range becomes greater than the guess.
        low = guess + 1
    elif high_low.casefold() == "l":
        # Guess lower. The high end of the range becomes 1 less than the guess.
        high = guess - 1
    elif high_low.casefold() == "c":
        print(r""">>========================================<<
||                                        ||
||      ___  __        __          _      ||
||     |_ _| \ \      / /__  _ __ | |     ||
||      | |   \ \ /\ / / _ \| '_ \| |     ||
||      | |    \ V  V / (_) | | | |_|     ||
||     |___|    \_/\_/ \___/|_| |_(_)     ||
||                                        ||
>>========================================<<""")
        print("Haha, I got it in {} guesses!".format(guesses))
        break
    else:
        print("{} is not an option, choose one of H, L or C!".format(high_low))
    guesses += 1
else:
    print("You thought of the number {}".format(guess))
    print("I got it in {} guesses!".format(guesses))
