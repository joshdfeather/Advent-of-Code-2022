
## Active solution run through:

#### Note: This solution is for day 18. It was a less involved coding problem for this late in the 25 day program. I chose to demonstrate with this as it allows an easy description of my approach without the code understanding being too complicated.


### The provided problem explanation on Advent of Code website
![alt text](images/Explanation1.png)
![alt text](images/Explanation2.png)
![alt text](images/Explanation3.png)

### My Solution
#### - Begin with parsing input
#### - Define six possible adjacent directions
#### - Start with part 1 solution counting each adjacent direction not filled
#### - Adapt part 1 solution to use a popleft double ended queue structure (stack)
#### - Uses a BFS style approach to emulate lava flowing down from [0, 0, 0]
![alt text](images/Solution.png)
