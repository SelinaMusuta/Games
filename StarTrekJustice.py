# This is a Star Trek trivia game that explores social justice themes.  I need to define
# social justice.  I also want to call out the assimilationist and othering that is in the Star Trek universe but I'd like to
# think more about that. I only finished one question because I stymied myself by not referring to my "answer" value within my if/else
# statement.

print "\t\tWelcome to Another Star Trek Trivia Game: "
print "\t\tThe Social Justice Version" # I need a better name for this game

# Section 1.
# Ask user In Deep Space 9, who organized a union to Defend

print "\nWho organized a union to establish sick leave and other paid benefits for workers at a popular bar on Deep Space 9?"

print "\n\ta) Quark \n\tb) Rom \n\tc) Captain Sisco"

# a) Quark
# b) Rom
# c) Captain Sisco

# if user inputs "a", then print "Rom took a stand against his brother after years of wage theft and emotional abuse"
# if user inputs "b", then print "then print "You may be confused.  Quark was the owner of that popular bar and tried to union bust his brother
# if user inputs "c", "Sisco's second job is not the owner of an away station bar....but being an emissary to the Bajorans takes up a lot of his time"
answer = raw_input("\nYour answer is ")


if answer != "b":
	print "\nYou maybe confused. Quark was the owner of the only bar on Deep Space 9 and made several attempts to bust up the union that Rom and his wife Leeta formed. "
	
elif answer == "b":
	print "\nCorrect! Rom took a stand against his brother, the owner of Quark's, after years of wage theft and emotional abuse."

else:
	print "\nSisco's second job is not the owner of an away station bar...but being an Emissary to the Bajorans takes up alot of his time." #I'm having problems printing this and I understand the reason why but would like to add value to c but not sure how

answer = raw_input("\nNext Question (Y/N)  ")	
	
# Section 2.	
# Ask user "What conflict is often used as an analogy in reference to the continued occupation of the Palestinian territories? "
# a) Romulan and Vulcan split in the 1300s
# b) The Borg wherever they go
# c) The Cardassian occupation of Bajor

# if user inputs "a", then print "Your answer is not close.  But Vulcans and Romulans have been warring cousins"
# if user inputs "b", then print "The answer is c.  The Borg don't occupy, they assimilate, destroy, and leave for the next lifeform"
# if user inputs "c", then print  "You are correct."

print "\nWhat conflict is often used as an analogy in reference to the continued occupation of the Palestinian territories? "

print "\n\ta) Romulan and Vulcan split in the 1300s \n\tb) The Borg wherever they go \n\tc) The Cardassian occupation of Bajor"

answer = raw_input("\nYour answer is ")

if answer == "a":
	print "\nYour answer is not close.  But Vulcans and Romulans have been warring cousins"

elif answer == "b":
	print "\nThe answer is c.  The Borg don't occupy, they assimilate, destroy, and leave for the next lifeform"

else:
	print "\nYou are correct."

answer = raw_input("\nNext Question (Y/N)  ")



# Section 3.
# Ask user "Which beings' central mission is to assimilate the technology and organic information of lifeforms in their collective being?"
# A commentary on communism.  
if answer == "Y":
	print "\nWhich beings' central mission is to assimilate the technology and organic information of lifeforms in their collective being? "

else:
	print "\nLive Long and Prosper!"
# if user inputs "a", then print "Resistance is futile! The Borg 's collectivism put off the '"
# if user inputs "b", then print ""

# Section 4.
# Ask user "Which character in Deep Space 9 is only referred to with male pronouns by others? "


# Trills
