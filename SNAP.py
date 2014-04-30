#The Truth About Food Stamps
# A trivia game that asks multiple choice questions to the user about food stamp benefits in DC.
# It will have five questions

#Welcome Screen
print "\n\n\n\n\n\tThe Truth About Food Stamps:"
print "\t\t5 Answers That May Suprise You"


# Section 1. first question
# This question asks "What is SNAP?"

print "\nWhat is SNAP?"
print "a) Spay-Neuter Assistance Program \nb) Supplemental Nutrition Assistance Program \nc) Stanford Network Analysis Platform"

#Ask the user for their response
answer = raw_input("Your answer: ")

if answer == "a":
	print "The correct answer is b."

elif answer == "b":
	print "You're right!"

else:
	print "Not quite.  The answer is b"

#This question asks "benefited from SNAP program in 2011?"

print "\nHow many D.C. residents benefited from the SNAP program in 2011? "
print "a) 30,000 \nb) 250,000 \nc) 135,000"

#Ask the user for their response
answer = raw_input("Your answer: ")

#If the user inputs the letter c, then print "You got it! Almost a 1/4 of DC's residents have benefited from the SNAP program"

if answer == "c":
	print "You got it! Almost a 1/4 of DC's residents have benefited from the SNAP program"

elif answer == "b":
	print "The answer is c but you are close."

else:
	print "Unfortunately, the need is great. The answer is c). A 1/4 od DC's residents benefited from the SNAP Program in 2011."

# Section 2. second question

print "\nWhat is the SNAP Expansion Act?"
print "a) Expands eligibility of low-income residents \nb) Increases benefits for SNAP recipients \nc) both"

answer = raw_input("Your answer: ")

if answer == "c":
	print "Right on!"

else:
	print "\nThe answer is c. The District of Columbia passed this piece of legislation 2009 to expand eligibility and raise benefits for SNAP recipients"

# Section 3. third question




# Section 4. fourth question



# Section 5. fifth question








