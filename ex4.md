1. Describe the algorithm you will use to find the room. Assume all the
information you have is the one given by the sign; you have no
knowledge of the floor plan [0.5 pts] 

Since you don't know the maximum number of rooms, you could start by picking a room 
at random. Since you know that rooms increment to the right, 
if the chosen room number is greater than 128, then you change your sample size
and limit it to rooms less than your current room. 
If the chosen room is less than 128, you repeat the search but instead limit it to only
rooms larger than your current room. You would use the rooms you selected previously
to eliminate choices. Once you get an interval between two numbers, for example let's say 
you chose 120 your first try and for your second try you chose 130. from here you could take a room 
roughly halfway between the two instead of relying on a random selection. 

2. How many ”steps” it will take to find room EY128? And what is a “step” in
this case? [0.25 pts]

A step in this case would be stopping to see what room you are at. 
Let's consider an average case. In the first step, the person chooses EY118. 
Therefore they know that they must pick a room that is higher than 118. 
In the second step they choose room 130. Since 130 is greater than 128, we know 
that the room must be between 118 and 130. In the third step they would choose 128. 


3. Is this a best-case scenario, worst-case scenario, or neither? [0.25 pts]

This is neither a best case or a worst case. This is an average case. In the scenario above, 
the person chooses a room roughly halfway between the given sample and changes the sample
size based on the chosen room. The scenario assumes that the person reasonably assumes 
distance between rooms. For example the person above picks 128 after 130 since they 
know 128 must be close to 130. 

4. With this particular sign and floor layout, explain what a worst-case or best-
case scenario would look like [0.5 pts]
The best case would be if the person chose 128 on their first try. 
The worst case would be if the person decided to start with room 100 and picked 
the room immediately to the right. It would take 15 steps to find 128. 


5. Suppose after a few weeks in the term you memorize the layout of the floor.
How would you improve the algorithm to make it more efficient? [0.5 pts]

Since you know the that 128 is closer if you go to the right, you could start your 
search there and instead limit your search to values on the upper end. 