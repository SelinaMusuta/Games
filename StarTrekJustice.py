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

# if user inputs "a", then print "Rom took a stand against his brother after years of wage theft and emotional abuse"
# if user inputs "b", then print "then print "You may be confused.  Quark was the owner of that popular bar and tried to union bust his brother
# if user inputs "c", "Sisco's second job is not the owner of an away station bar....but being an emissary to the Bajorans takes up a lot of his time"

answer = raw_input("\nYour answer is  ")

if answer != "b":
	print "\nYou maybe confused. Quark was the owner of the only bar on Deep Space 9 and made several attempts to bust up the union that Rom and his wife Leeta formed. "
	
elif answer == "b":
	print "\nCorrect! Rom took a stand against his brother, the owner of Quark's, after years of wage theft and emotional abuse."

else:
	print "\nSisco's second job is not the owner of an away station bar...but being an Emissary to the Bajorans takes up alot of his time." #I'm having problems printing this and I understand the reason why but would like to add value to c but not sure how
	
	
# Section 2.	
# Ask user "What conflict is often used as an analogy in reference to the continued occupation of the Palestinian territories? "

print "\nWhat conflict is often used as an analogy in reference to the continued occupation of the Palestinian territories? "

# if user in puts "a", then print ""
# if user in puts "b", then print ""
