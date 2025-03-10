# Personal Work
Hi! Below I've detailed my work on wildfire prediction, PONG with Machine Learning, and the Cuckoo Search Metaheuristic.

WILDFIRE PREDICTION
I used the UNET architecture to predict wildfires on global wildfire maps.

This first image depicts a binary segmentation scheme
![Alt text](https://github.com/kevhainfo/PersonalWork/blob/76abd92ea668cf097ea97f50b65b146cacdf0ba4/wildfire/prediction.png)
The Jacard Index(area of overlap between prediction and actual) is 0.58

The second image depicts a tertiary segmentation scheme(small or no wildfire, medium wildfire, large wildfire)
More specifically, wildfire size is quantified using Burnt Area(how much of the area encompassed by one pixel is burned)
![Alt text](https://github.com/kevhainfo/PersonalWork/blob/8ac2ec13363c473065d1ca1fdea6e1c29415972f/wildfire/Screen%20Shot%202023-07-08%20at%208.31.06%20PM.png)

The Jacard Index is 0.9(significantly better)

<be>

  
PONG WITH MACHINE LEARNING:
I made an application for my high school computer science club: it creates Pong Bots that mimic a player's movements using Random Forests

<be>
This is a screenshot of the actual gameplay. The bot is on the left, and the player is on the right. The bot's movements are learned from the player's previous movements relative to the ball's position.

![Alt text](https://github.com/kevhainfo/PersonalWork/blob/8e0203f04c79580fcb30660c3f3aba4673db8f47/PongWithMachineLearning/pong.png)


CUCKOO SEARCH:
I used cuckoo search, a nature-based metaheuristic, to find optimal routes to the Traveling Salesman Problem.

<be>
This is the tour produced on iteration 35 of the cuckoo search algorithm. It shows the optimal tour for this particular TSP input.
  
![Alt text](https://github.com/kevhainfo/PersonalWork/blob/bc6c749ca5a84458d2faa1d4cbbee0eeed18d7c5/cuckooSearch/cuckooSearch.png)

