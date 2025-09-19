# Create a new document called quiz1.py copy/ paste the following questions
# on your document and answer the following questions.

# quiz rules:
# - There is no talking during the quiz
# - You may only use your classnotes and w3schools.com for reference
# - If you have a question about a quiz question, please raise your hand
# - Once finished, submit your code to your repository using the source control 
# button. Your commit should be "completed quiz 1."

'note: all written responses should be written/ formatted as strings.'

# 1. In your own words, describe the differences between a linear search and a 
# binary search. Please write your response using complete sentences.
"A liner search goes through the list in order and a binary search divides the list until you get the desired outcome."

# 2. How many steps would it take to get to the desired number of 98 using linear search?
# Please write your response using complete sentences.
"Six steps are needed using linear search"

listA = [10,24,34,35,67,98,101]

# 3. How many steps would it take to get to the desired number of 150 using a binary search?
# Please write your response using complete sentences.
listB = [1,/ 40,/  44,/  55,/ 70,/ 93,/  99,/ 134,/ 145,/  150,/ 200,/ 244 ]
#1,2,3,4,5,6,7,8,9
"Nine steps are need to get to 150"

# 4. In your own words describe what an algorithm is. 
# Please write your response using complete sentences.
"An algorith is concise list of instructions"

# 5. A person and their family is visiting a medical building. the medical building has
# 10 floors. The patient that the person and their family is visiting is on the 7th floor 
# of the building. The family also knows what room they need to go to to visit the
# patient on the 7th floor. which big-O time complexity would best describe the steps it
# would for them to get to the desired room and why? 
# Please write your response using complete sentences.
"selection sort becuase it would start at the smallest number and bring it to the front until it is in order."

# 6. You and your friends are headed out to a party, as you're preparing to walk out the door to meet with
# your pals, your realize you forgot your phone. you you can't remember exactly where you misplaced it 
# but you know it is in one of your pairs of pants. You have 10 pairs of paints. which big-O time complexity
# would best describe the steps it would take to find your phone?
# Please write your response using complete sentences.
"A linear search because with it you would check each one in order one by one"

# 7. Create a class that will represent and create game console objects. 
# Your class should have 4 attributes and 3 methods. 
# Once you've created your class, create 2 unique video game consoles.
class gameConsole:
    def __init__(self,powerbutton, logo, cost, version ):
        self.powerbutton = powerbutton
        self.logo = logo
        self.cost = cost
        self.version = version

    def consoleInfo(self):
    
    
    
    def fan(self):
        print('when overheating turn on')
    def power(self):
        print('when powerbutton is pressed turn on')
    def controller(self):
        print('when console turns on connect to it')

Cross1 = gameConsole('on', 'Cross', '500$', '1.0')

print(Cross1)

Cross1.

    
    

# 8. Create a class that will represent a video game for your console.
# Your class should have 4 attributes and 3 methods objects.
# ONCE You've created your class, create 2 unique video games objects.. 
