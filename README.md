# Python-class-111


 Most data in the world can be plotted as a normal distribution which looks like a bell-curve.
- Mean of a population in a normal distribution is at its peak.
- Most of the data (68%) in the population lie within one standard deviation from the mean.
- 95 % of data lie within two standard deviations from the mean and 99% of data lie within three standard deviation from the mean.



- Sampling distribution is the distribution created when we plot means of 1000s of samples with a fixed sampling size.


- Mean of a sampling distribution is the same as the mean of the population.

- Standard deviation of the sampling distribution (also called standard error of the mean) 
= standard deviation of the population distribution / sqrt (sampling size).


if sampling size is 100 ,sqrt(100)=10

so,
- Standard deviation of the sampling distribution (also called standard error of the mean) 
= standard deviation of the population distribution / 10
****************************************************************************************************
--Study the math scores of students in a population
--- Create a sampling distribution for the population with 100 sampling size
*******************************************
Prasad is a principal of a school. The school has 10000 students across Grades 1 to 12.
The school students performed not so well in the recent math test in their half-yearly exams.
Here is the Math score for all the students in the exam.
<Student Activity 1>

to better understand the data
We can plot the distribution data.
- We can calculate the mean and standard deviation for the data.
- find the mean and standard deviation for this data.

*******************************
Prasad, as the school principal decided to do something to improve the math scores of the students in her school.

Extra classes
- More practice problems
- Workshops
- Use of tech in classrooms

some of these things might be effective and some of these might not be effective in improving the Math scores.
**********************************

She decided to randomly select 3 groups of 100 students each and try different interventions on these groups. She then wants to understand the
impact of each intervention and study if the effect of these interventions was positive enough so that it can be implemented throughout the school.

*******************************
Before that, let us draw a sampling distribution for the data with sampling size of 100. We can take around 1000 samples to create the distribution.
find the mean and plot them on a distribution.
Check if the sample distribution is a bell shaped curve.
*****************************
Mean of sampling distribution should be equal to the mean of the population.
Standard deviation of the sampling distribution = Standard deviation of the population / sqrt (100).
------------------------------
. One group of 100 randomly selected students were given iPad tablets with math reading and learning materials in it.
2. Second group of 100 randomly selected students were given 2 hours of extra classes daily.
3. Third group of 100 randomly selected students were given math fun sheets to practice at home.
4. 
After a month of intervention, all the three groups were tested again.
The results of the score for all the three groups are in data1.csv, data2.csv and data3. csv
*********************************
We know that:
68% of data lie between one standard deviation from the mean.
If the new sample mean lies within one standard deviation, we can say that not much might have changed because of the intervention. In statistics, we say that the change has not been significant.

95% of data lie between two standard deviations from the mean.
If the sample mean lies beyond two standard deviations from the mean, we can say that there must have been a significant change because of the intervention.


99% of data lie between three standard deviations from the mean.
If the sample mean lies even beyond the three standard deviations from the mean, it is highly probable that the intervention has an impact.

If the intervention has been positive, the mean would lie to the right.
If the intervention has been negative, the mean would lie to the left.


*************************************
One way to find the impact of an intervention is by plotting the mean and comparing how many standard deviation away from the mean is the new sample mean by guesstimating.

Another way to do is by mathematically calculating it:
- Find the difference between the mean and the new sample mean: Sampling Distribution Mean - New sample mean
- Calculate how many standard deviations away is the new sample mean from the sampling distribution mean:

z-score = (new Sample Mean - Sampling Distribution Mean)) / standard deviation


z-score tells how many standard deviations away is the new sample mean from the sampling distribution mean.

If z > 3 or z > 2 ; the new sample mean lies more than 3 standard deviations away from the sampling distribution mean. It also means that there has been a large impact of the intervention.
We say that the change in math score is statistically significant.


If z < 1 or z < 2; the impact of the intervention might not be statistically significant.


This example was really important because it helped us identify which intervention worked best on different population sets.
This type of testing to identify the impact of interventions is used by governments, financial institutions and non-profits to understand what works best with a population.
