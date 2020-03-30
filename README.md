# Data Science Mini Project Solutions

## Q1)
#### Note:
This question can also be solved analytically, but this code uses ensemble averaging to solve it numerically. The default number of ensembles has been set to 100000 but can be increased in order to gain higher decimal precision.

### How-to:
The folder deckCalculation contains two .py files: 'Input.py' for getting proper and valid input from user for different parameters of the question and 'Calculate.py' which includes functions for calculating the mean, STD and conditional probability.

In order to solve the first four question about the mean and standard deviation, you should import the 'calculate' function from 'deckCalculation.Calculate' and simply call it. It asks for N (total number of cards in a deck) and M (number of suits to equally divide card between). Then prints out the results.

For the last two questions, we want to calculate the conditional probability for p>p_high given that it is p>p_low.
Note that for this calculation we should satisfy the conditions: 0<=p_low<=p_high<=N. This condition is automatically checked in the Input functions.

Now, you should simply import 'conditionalProb' from 'deckCalculation.Calculate' and then call it. This function asks for four values: N (total number of cards in a deck), M (number of suits to equally divide card between), p_low and p_high (as mentioned above), then prints out the results.

A Jupyter notebook has also been provided with markdowns for demonstration: 'deck.ipynb'

#### Results:
1) N=26, M=2: Mean:	12.00973, STD:	2.5065065982558274
2) N=52, M=4: Mean:   12.00309, STD:	3.0323358079045266

5) conditional probability that P>12 given that it's P>6:	0.42559
6) conditional probability that P>12 given that it's P>6:	0.43584

## Q2)
### How-to:
