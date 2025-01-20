import pandas as pd
var1=pd.DataFrame({'A':[1,2,3,4,5], 'B':[9,8,7,6,5]})
"""print(var1)
   A  B
0  1  9
1  2  8
2  3  7
3  4  6
4  5  5
"""
var1.insert(1,"python",var1["A"])
"""print(var1)
   A  python  B
0  1       1  9
1  2       2  8
2  3       3  7
3  4       4  6
4  5       5  5"""
var1.insert(1,"python_1",[11,12,13,14,15])
"""print(var1)
   A  python_1  python  B
0  1        11       1  9
1  2        12       2  8
2  3        13       3  7
3  4        14       4  6
4  5        15       5  5"""
var1["python_12"]=var1["A"][:3]
"""print(var1)
#copy the data
   A  python_1  python  B  python_12
0  1        11       1  9        1.0
1  2        12       2  8        2.0
2  3        13       3  7        3.0
3  4        14       4  6        NaN
4  5        15       5  5        NaN"""
varDel1=var1.pop("python_1")
"""
print(varDel1)
print(var1)
0    11
1    12
2    13
3    14
4    15
Name: python_1, dtype: int64
   A  python  B  python_12
0  1       1  9        1.0
1  2       2  8        2.0
2  3       3  7        3.0
3  4       4  6        NaN
4  5       5  5        NaN"""
