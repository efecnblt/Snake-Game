# Snake-Game
Simple snake game in python

This is simple snake game implemented in python. There are 4 .py files in the file. These are respectively;  

**food.py:** It allows us to create a small blue bait in a random position on the game screen.    

**main.py:** It is our main file. Objects are created in it, controls are provided and functions are called.  

**scoreboard.py:** With the functions we have created in it, it ensures that the score is increased every time the bait is eaten. We write this score to a `score.txt` file instantly. In this way, when the game is opened again, it will first read the high score recorded in the file and print it on the screen. Therefor, the highest score we have made will not be lost even if the game is over.  

**snake.py:** Initially, we create 3 shapes and adjust their positions one after the other. When the bait is eaten, we create another shape again right after our last shape. In this way, the snake grows every time it eats the bait.  

**score.txt:** The value of our highest score is written in it. This file is read and printed to the screen.  

The snake created in the middle of the screen starts to move. We move this snake with our controls. It starts to grow every time it eats the bait. If the snake hits the sides or itself, it's game over.

![snake_game](https://github.com/efecnblt/Basics-Games-with-Python/blob/main/Snake%20Game/snake_game.gif?raw=true)
