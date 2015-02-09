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

    python chinese.py -o [1, 2, 3, 4, 5, 6]

By supplying a chapter number, only words from the corresponding chapter will appear. An example of configuring your `.bash_profile` to do this is shown below:

    python path/to/chinese.py/chinese.py -o 5

Which will cause your terminal to display only words from Chapter 5 upon opening. If you pass in an argument out of range, a random word from the entire set of words will be chosen instead. 
    

