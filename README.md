This python code can be used to calculate the dead time or more accurately, the resolving time of a GM counter.

The code is based on the "Two Source Method" where you have two sources of radiation to calculate the dead time of the GM Counter. 

A brief procedure of the same is as follows:

1) Find operating voltage of the GM Counter, then set the applied voltage as operating voltage and increase the integration time to atleast 10mins (more the integration time, better the statistical accuracy).

2) Start the counting without any sources to measure the background count (CB).

3) Put one source in for counting the number of events (C1) for the set integration time.

4) Now place the second source along with the first source without disturbing the first source and measure the counts (C12) for the set integration time.

5) Take out the first source without disturbing the second source and take the counts (C2) for the set integration time.

6) Repeat this for multiple times. More the number of observations, more accurate the result.

Now that you have the counts and integration time, plug the values in the code and it will calculate the dead time and the uncertainty in the dead time for the GM Counter. It will also plot the gaussian curves for the given dead times considering the uncertainty as one sigma error.

Note: The code uses the formulas based on the non-paralyzable model of detector with an assumption that the square of dead time is too small, thus the term in multiplication with it can be ignored.
