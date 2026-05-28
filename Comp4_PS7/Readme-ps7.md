# PS7: Kronos Log Parsing

## Contact
Name: Saad Kapadia
Section: 203
Time to Complete: about 3 hours


## Description
Explain what the project does.

this program parses log files to find boot times and whether the program has launched successfuly or not

### Features
Describe what your major decisions were and why you did things that way.

my major decsisions was to make a functionless approach, made it much easier to visualize in my head, 
### Approach
Describe your overall approach to solving this problem.

i made a functionless approach, the program runs until it finds a begin regex, which causes a search bool to then become true, which then switches the logic of the program to look for the end regex, if another begin is found, we know that the service failed to launch


### Regex
What regular expressions did you use?  Explain what each one does.

bootStart = r"\([a-z]{3}\.[a-z]\.\d{3}\) server started"
looks for three chars a '.' a char, a '.' and then 3 numbers all inside parenthesis, server started was added later because i was having issues in log3 because there is a similar watch dog service that trips it up

bootEnd = r"[A-Z]{4}\:[a-z]{4}\..{17}\:.{7} "
4 captial chars a ':'  4 chars '.' 17 chars, then ':' 7 symbols

just follows the exact format of the the proper sucessful launch message

CORRECTION: I got rid of these in favor of hard coding the regexes, I only use the date regex

grabDate = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

just grabs year month year, hour minute, second


### Issues
What did you have trouble with?  What did you learn?  What doesn't work?  Be honest.  You might be penalized if you claim something works and it doesn't.

just had some trouble relearning python but nothing too crazy

### Extra Credit
Anything special you did.  This is required to earn bonus points.

## Acknowledgements
List all sources of help including the instructor or TAs, classmates, and web pages.

the provided python for cpp developers slides

python documentation for datetime, fileio.

rexegr.com