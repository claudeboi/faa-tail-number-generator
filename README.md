# faa-tail-number-generator
Generate 5 character FAA tail number accounting for all rules
Input the minimum and maximum number of characters beyond the N (1-5 inclusive)
3-5 character tail numbers are recommended as most 1-2 length tail numbers are reserved by the FAA or other special users (ie N1A is a Goodyear Blimp)

The code is biased towards generating longer tail numbers since each addition of a character results in approximately 10x more valid tail numbers.
This bias may be adjusted by changing "LONG_LENGTH_BIAS".
Numbers closer to 0 result in longer average tail numbers; closer to 1 results in shorter average tail numbers. 

Variations within lengths (such as format N10000 vs N1000A vs N100AA) account for the actual number of possible tail numbers in each format. 
These variations may be changed to your preference by editing the constants. All comparisions are in the < direction; therefore, values closer to 1 will result in more numbers in your tail numbers compared to letters.
My personal preference is TWO_LETTERS_CHANCE around .7 and LETTER_OR_NUMBER around .2 (30% chance of ending in 2 letters, 50% chance of ending in 1 letter, 20% chance of ending in a number)

Blame ChatGPT if the default %s are wrong, I ain't doing all that math by hand. (For the record, no other generative AI was used in the making of this script. I write dogshit code for the love of the game.)

There are probably bugs. Let me know if you run into any unexpected behavior.
