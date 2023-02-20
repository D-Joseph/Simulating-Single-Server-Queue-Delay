import random
import matplotlib.pyplot as plt

mu = .75
lamVals = [0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.72, 0.74, 0.745]
l = [] # L, will store the expected queue length for each value of lambda
w = [] # W, will hold the expected waiting time for each value of lambda

# Find the next state that the queue is in
def queueingDynamics(arrival: bool, departure: bool, currState: int) -> int:
  # q(k+1) = q(k) + a(k) - d(k)
  nextState = currState + arrival - departure
  # Ensure that there isn't a negative amount of elements in the queue
  return nextState if nextState > 0 else 0

# Iterate through lambda values, and find the expected queue length
for lam in lamVals:
  currState = 0 # Hold current queue state, starting with nothing in the queue
  avgQ = 0 # Will be used to calculate L

  # Run each simulation for 1,000,000 time slots
  for i in range(1000000):
    # Generate uniform random values for arrival and departure, and compare them to the rate of arrival and departure
    arrVal = random.uniform(0, 1)
    depVal = random.uniform(0, 1)
    # If less than the rates, then this 'packet' has successfully arrived/departed
    currState = queueingDynamics(1 if arrVal <= lam else 0, 1 if depVal <= mu else 0, currState)
    avgQ +=  currState # Running sum of number of elements in queue
  l.append(avgQ / 1000000)

# Find the expected queueing delay per lambda value
for c, i in enumerate(l):
  # Little's Law, W = L / λ
  w.append(i/lamVals[c]) 

# Plot
plt.plot(lamVals, w)
plt.title('Average Queueing Delay by Arrival Rate, $\mu$ = 0.75')
plt.xlabel("Arrival Rate, $\lambda$")
plt.ylabel("Expected Queueing Delay, W")
plt.show()