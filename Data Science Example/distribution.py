#1 coin with 0.5 probanility 
np.random.binomial(1, 0.5)
#size means total task to be performed so we get stimulate the result
np.random.binomial(n,p,size)
#Standard deviation
distribution = np.random.normal(0.75,size=1000)
np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution))
#std with build in fuction
np.std(distribution)
#kurtosis helps check that the graph is flat or peak if flat -ve value if +ve peak
import scipy.stats as stats
stats.kurtosis(distribution)
#If the degree fredom increse the skew shift from right to left hence value changes
chi_squared_df2 = np.random.chisquare(2, size=10000)
stats.skew(chi_squared_df2)
chi_squared_df5 = np.random.chisquare(5, size=10000)
stats.skew(chi_squared_df5)
#if alpha that is 0.05 or any is less then the p value then the null hypothesis is accepted else rejected and the satistic voalue show the differen e
early = df[df['assignment1_submission'] <= '2015-12-31']
late = df[df['assignment1_submission'] > '2015-12-31']
early.mean()
late.mean()
from scipy import stats
stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])
Ttest_indResult(statistic=1.400549944897566, pvalue=0.16148283016060577)
#continuous runing the same hypothesis cause phacking to solve it try using Bonferroni correction=0.05/3 or hold out some of your data =use CV