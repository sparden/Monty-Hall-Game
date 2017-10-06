# Monty-Hall-Game

Inspired from the movie [Twenty-One](https://en.wikipedia.org/wiki/21_(2008_film)) <br />
where Monty-Hall problem was asked to the students of MIT, <br />
I decided to demonstrate it to the high-school students with the help of Game. <br />


# Programming language and packages used:

1.Python 2.7<br />
2.pygame<br />
Note: if you have multiple version of python you can set alias for python to python2<br />
example in ubuntu: alias python=python2

# Usage:
python main.py

# Problem Description:

-There are three doors. All closed initially. <br />
-Out of the three doors, 2 contains Goats and remaining 1 contains a brand new Car. <br />
-You are asked to choose one of the doors which you guess to have the Car. <br />
-The host of the game knows the position of the Car so he opens one of the doors having Goat in it. <br />
-Now you are given a option to swap your choice. <br />
-What would you do? Swap or no Swap! <br />

-Though our intuition tells it is 50-50 case, therefore swapping or not swapping doesn't make any difference. <br />
-But Mathematics suggests you to Swap your choice each time you play the Game. <br />


# Explanation

-Probability of getting a Goat: 2/3 and that of getting the Car is 1/3 <br />

**Case I: No swap** <br />
	&emsp; The probabilities doesn't change, Car 1/3 and Goat 2/3. <br />

**Case II: Swap** <br />
	&emsp; Case II.1: <br />
		&emsp; &emsp; If initially chosen door had a Goat inside it, Swapping your choice will give you a Car for sure <br />
		&emsp; &emsp; because the host has already opened the door containing a Goat. <br />
	&emsp; Case II.1: <br />
		&emsp; &emsp; If initially chosen door had the Car inside it, Swapping your choice will give you a Goat for sure <br />
		&emsp; &emsp; because the host has already opened the door containing a Goat. <br />

In Case II, we see winning a Car or Goat depends solely on what we chose at the first attempt. <br />
If you chose a Goat at the first attempt, You will get the Car. <br />
If you chose a Car at the first attempt, you will get the Goat. <br />

Hence, <br />
The probability of winning the Car after swapping = probability of chosing a Goat at the first attempt = 2/3 <br />
The probability of winning a Goat after swapping = probability of chosing the Car at the first attempt = 1/3 <br />

So the ratio of wins and losses should be close to 2. --((2/3)/1/3)-- <br />
Now see the below screenshot from the game. The ratio is ~1.85. <br />

# Screenshot

![alt text](https://github.com/speedious/Monty-Hall-Game/blob/master/monty_hall/Monty_Hall_Game.png)









