# integrated-chinese

Learn Chinese vocabulary inside of your terminal! Vocabulary words are taken from the [Integrated Chinese textbook](https://www.cheng-tsui.com/browse/integrated-chinese), and currently supports Chapters 1-8.

    $ python flashcards.py chinese
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
2. Run: `python flashcards.py chinese`

If you would like this to run each time you open up a new terminal, add the following line your `.bash_profile` file as shown below:
	
    python path/to/flashcards.py chinese

### Specify specific chapter for word generation

Are you only interested in generating words from a specific chapter? If so, you can add the following command line argument to your `python flashcards.py` call:

    python flashcards.py --chapter <1, 2, 3, 4, 5, 6, 7, 8> chinese 

By supplying a chapter number, only words from the corresponding chapter will appear. An example of configuring your `.bash_profile` to do this is shown below:

    python path/to/chinese.py/chinese.py --chapter 5

Which will cause your terminal to display only words from Chapter 5 upon opening. If you pass in an argument out of range, a random word from the entire set of words will be chosen instead. 


### Filters

Are you only interested in a specific type of word? If you would like to get all verbs:

    python flashcards.py --type verb chinese

Or to get all nouns and pronouns from chapters 1, 2 and 3:

    python flashcards.py --type noun,pronoun --chapter 1,2,3 chinese

The filters work in both quiz and card of the day modes.

    
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
	[1]: Miss; young lady
	[2]: I; me
	[3]: Beijing


	Which translation is correct? 2


	Not quite...the correct answer was: (a personal name)

Want to test your translation skills? Run the following command in your terminal to test your translation skills for a specific chapter:

    python flashcards.py --chapter <1, 2, 3, 4, 5, 6, 7, 8> --quiz 1 chinese

For example, if you want to test yourself on Chapter 5, run the program as shown below:

    python flashcards.py --chapter 5 --quiz 1 chinese



