import statsmodels.formula.api as smf
import pandas as pd, numpy as np

data = pd.read_csv("https://github.com/dustywhite7/Econ8320/blob/master/AssignmentData/assignment8Data.csv?raw=true")


reg = smf.ols("hhincome ~ year", data=data).fit()
print(reg.summary())


reg = smf.ols("np.log(hhincome+1) ~ educ + age + I(age**2)+ female + married + C(race)", data=data[data['hhincome']>0]).fit()
print(reg.summary())

import statsmodels.api as sm
myformula="married ~ hhincome + C(statefip) + C(year) + educ"
model= smf.Logit.from_formula(myformula, data=data).fit()


from sklearn import tree
from sklearn.metrics import accuracy_score
import pandas as pd
import patsy as pt

data = pd.read_csv("https://github.com/dustywhite7/pythonMikkeli/raw/master/exampleData/roomOccupancy.csv")

