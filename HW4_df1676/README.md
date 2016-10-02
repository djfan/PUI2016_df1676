# HW4_df1676

Dongjie Fan

df1676

Group with *Ziman Zhou*

## Assignment 1

After forking and cloning kq320's HW folder, I committed my CitibikeReview_df1676 and make a request for adding this file into his repo.

Here's the request link:

https://github.com/kq320/PUI2016_kq320/pull/2

Here's the screen shot:

![4](PlotForCitibikeReview/4.png)Also I backup the file in my HW4 folder.



## Assignment 2

[*reference*](http://www.csun.edu/~amarenco/Fcs%20682/When%20to%20use%20what%20test.pdf)

| Statistical Analyses    | IV(s)                                    | IV type(s)                               | DV(s)                                    | DV type(s)           | Control Var                      | Control Var type                         | Question to be answered                  | _H0_                                     | alpha | link to paper                            |
| ----------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | -------------------- | -------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ----- | ---------------------------------------- |
| **ANCOVA**              | Pattern (Longtitudinally  Stripped Pattern / Vertically Stripped Pattern / Unicolored Pattern   ) | Categorical                              | Percentage of hits                       | Numeric (Continuous) | 1.Speed 2.Disappearance Duration | 1.Numeric (Continuous)  2.Numeric (Continuous) | Whether pattern, influenced the frequency with which the objects were hit | There is no difference  of percentage  of hits between animals with longtitudinally  stripped pattern / vertically stripped pattern / unicolored pattern | 0.05  | http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0061173  (experiment 1) |
| **Multiple Regression** | 1.The duration of denture use 2. Main Cleaning Method 3.Gender 4.Smocking 5.Tea Consumption 6.Denture Scratching | 1.Continuous 2.Categorical 3.Categorical 4.Categorical 5.Categorical 6.Categorical 7.Categorical | Possibility of having denture plaque and staining probelm | Numeric (Continuous) |                                  |                                          | What the relationship  between Denture Plaque and Staining Probelm and Associated Risk Factors  in Chinese Removable Denture Wearers over 40 Years Old in Xi’an | (t-test for each IV) the parameter of the independent viable is equal to 0, which means there is no relationship between each IV and DV. <br/>(F-test for all IV) the parameters of the independent viable are equal to 0 simultaneously, which means there is no relationship between all IVs and DV. | 0.05  | http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0087749 |

Thanks a lot for *Ziman Zhou* who promptly corrects my misunderstanding about ANOVA and ANCOVA. 



## Assignment 3

see https://github.com/Alan-F/PUI2016_df1676/blob/master/HW4_df1676/HW4_3_df1676.ipynb

Thanks a lot for *Ziman Zhou* who help me understand the Table 2.1 in HW4_3.



## Assignment 4

seehttps://github.com/Alan-F/PUI2016_df1676/blob/master/HW4_df1676/HW4_4_df1676.ipynb

1. For the Pearson's and Spearman's correlation test, I use the whole dataset ( 201502 Citibike Data )to run the test.
2. In my opinion, it's much more meaningful to test the frequencies of different ages (or age intervals) by gender. So I did Pearson's and Spearman's test twice, one for age list, the other for my idea.
3. Thanks a lot for *Yao Wang* who remind me that the Null Hypothesis of K-S test is two samples are from the same distribution.
