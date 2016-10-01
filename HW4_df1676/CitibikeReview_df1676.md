## Assignment 1: Citibike Review 

*by Dongjie Fan (df1676)*



## 1.Review

The HW3_3 I read is from Github Account: **kq320**.

His idea is to test **Women have less trip duration than men.**

*NULL HYPOTHESIS* as follow :

**The average trip duration of man is the same or less than the average trip duration of women**

**Mean(m) <= Mean(w)**

*ALTERNATIVE HYPOTHESIS* as follow:

**The average trip duration of man is higher than the average trip duration of women**

**Mean(m) > Mean(w)**

*significance level*: 

**$\alpha$=0.05**


His *NULL* and *ALTERNATIVE*  hypotheses are formulated correctly.

Also, CitiBike dataset can support his idea and hypothesis test.



## 2.Which Test? Why?

In my opinion, his experiment can use **t-test**, specificlly [Welch's *t*-test](https://en.wikipedia.org/wiki/Welch%27s_t-test) since his hypothsis test is to verify whether the locations (mean) of two independent samples are same or not. Besides, in his test, two population variances can not be assumed to be equal (the two sample sizes may or may not be equal). Hence they must be estimated separately. That's why I think **t-test**, specificlly **Welch's t-test** is appropriate.    

#### About Welch's t-test  

![{\displaystyle t={{\overline {X}}_{1}-{\overline {X}}_{2} \over s_{\overline {\Delta }}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/60ad758d34efcbd43dc2b8ec011a242006d5d679)    

where

![{\displaystyle s_{\overline {\Delta }}={\sqrt {{s_{1}^{2} \over n_{1}}+{s_{2}^{2} \over n_{2}}}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/94c0058a955d60e5fdfac3de07ff9577c3b3be63)

Here **$s_{1}^{2}$** is the unbiased estimator of the *variance of each of the two samples* with *$n_i$* = number of participants in group i, i=1 or 2. 

The distribution of this statistic is approximated as an ordinary Student's *t* distribution with the degrees of freedom calculated using:

![ \mathrm{d.f.} = \frac{(s_1^2/n_1 + s_2^2/n_2)^2}{(s_1^2/n_1)^2/(n_1-1) + (s_2^2/n_2)^2/(n_2-1)}.](https://wikimedia.org/api/rest_v1/media/math/render/svg/bb913297c779f950eadb6b3b92bc080a4e96a3ae)



*Reference* :

[Student's *t*-test]( https://en.wikipedia.org/wiki/Student%27s_t-test)

[Welch's t-test](https://en.wikipedia.org/wiki/Welch%27s_t-test)



## 3. Feedback

One thing need to be mentioned, his data is just monthly data (Jan 2015). Maybe there are other factors can affect the averaged duration of rides, for example, seasonal factor. Hence my solutions are:

1. Describe the idea and hypothesis statements more clearly. For example:

   Idea: **In winter, Women have less trip duration than men.**

   NULL Hypothesis: **The average trip duration of man is the same or less than the average trip duration of women in winter months**

2. Or can **combine** dataset of several different months together, including **months in Spring / Summer / Fall / Winter**.

