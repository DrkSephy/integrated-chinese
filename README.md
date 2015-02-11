# integrated-chinese

Learn Chinese vocabulary inside of your terminal! Vocabulary words are taken from the [Integrated Chinese textbook](https://www.cheng-tsui.com/browse/integrated-chinese), and currently supports Chapters 1-6.

    $ python chinese.py
    ----------------------------------------
       Integrated Chinese Word of the Day
    ----------------------------------------
	Chapter:       6
	Vocabulary ID: 8
	Characters:    位
	Pinyin:        wèi
	Type:          measure word
	Translation:   (polite measure word for people)


# Installation

1. Clone this repository 
2. Run: `python chinese.py`

If you would like this to run each time you open up a new terminal, add the following line your `.bash_profile` file as shown below:
	
    python path/to/chinese.py/chinese.py

### Specify specific chapter for word generation

Are you only interested in generating words from a specific chapter? If so, you can add the following command line argument to your `python chinese.py` call:

    python chinese.py --chapter <1, 2, 3, 4, 5, 6>

By supplying a chapter number, only words from the corresponding chapter will appear. An example of configuring your `.bash_profile` to do this is shown below:

    python path/to/chinese.py/chinese.py --chapter 5

Which will cause your terminal to display only words from Chapter 5 upon opening. If you pass in an argument out of range, a random word from the entire set of words will be chosen instead. 
    
### Interactive quiz section

    ----------------------------------------
             Chapter 1 Quiz
	----------------------------------------


	Enter a number to select a choice!
	Press q to quit at any time.


	----------------------------------------
	      Chapter 1 Quiz: Problem # 1
	----------------------------------------


	Word: 李友


	[0]: (a personal name)
	[1]:  Miss; young lady
	[2]: I; me
	[3]: Beijing


	Which translation is correct? 2


	Not quite...the correct answer was: (a personal name)

Want to test your translation skills? Run the following command in your terminal to test your translation skills for a specific chapter:

    python chinese.py --chapter <1, 2, 3, 4, 5, 6> --quiz 1

For example, if you want to test yourself on Chapter 5, run the program as shown below:

    python chinese.py --chapter 5 --quiz 1



