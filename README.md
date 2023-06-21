# icebreaker-maze
Final project that I created for my Intro to CS class. 

# Background
Simulates the movement of an icebreaker ship through the Arctic Ocean. Relies on the Zelle graphics package for visualization. Finds the optimal path via a wavefront algorithm based on a 2d array map to navigate through the obstacles.  

# How it works

Launching the arctic.py file creates the following maze: 

<img width="1401" alt="image" src="https://user-images.githubusercontent.com/62463944/156073249-16e76df6-e0c9-4bce-9daa-ef1ac45dff60.png">

You can then select a starting spot:

<img width="1401" alt="image" src="https://user-images.githubusercontent.com/62463944/156073264-5b4239cc-b083-4e2a-943c-ec240571f014.png">

As well as a target destination. The wavefront algorithm will then find the shortest way through:

<img width="1401" alt="image" src="https://user-images.githubusercontent.com/62463944/156073309-324dfd4e-3907-40d5-87b6-761806b47a3e.png">

As the game advances, more obstacles are added and it gets more difficult:

<img width="1400" alt="image" src="https://user-images.githubusercontent.com/62463944/156073511-e357e791-0217-49e0-9795-ac51a34df0cb.png">
