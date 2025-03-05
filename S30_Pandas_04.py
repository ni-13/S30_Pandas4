# Pandas_04

# 177. Nth Highest Salary_Solution_Q1

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    dist = employee.drop_duplicates(subset='salary')
    dist['rnk'] = dist['salary'].rank(method='dense', ascending=False)
    ans = dist[dist.rnk == N][['salary']]
    if not len(ans):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    ans = ans.rename(columns={'salary':f'getNthHighestSalary({N})'})
    return ans

#Alternative1

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    result_set = set()
    for i in range(len(employee)):
        salary = employee['salary'][i]
        result_set.add(salary)
    result= []
    for element in result_set:
        result.append(element)
    result.sort(reverse =True)

    if N > len(result) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    
    return pd.DataFrame({f'getNthHighestSalary({N})' : [result[N-1]]})

#Alternative2

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df= employee[['salary']].drop_duplicates()
    if N > len(df) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    
    return df.sort_values('salary', ascending = False).head(N).tail(1)[['salary']].rename(columns ={'salary':f'getNthHighestSalary({N})'})

______________________________________________________________________________________________________________________________________

# 176. Second Highest Salary_Solution_Q2

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(["salary"])
    if len(employee["salary"].unique()) < 2:
        return pd.DataFrame({"SecondHighestSalary": [np.NaN]})
    employee = employee.sort_values("salary", ascending=False)
    employee.drop("id", axis=1, inplace=True)
    employee.rename({"salary": "SecondHighestSalary"}, axis=1, inplace=True)
    return employee.head(2).tail(1)