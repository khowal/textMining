import pandas as pd
text = "DataCamp is the first online learning platform that focuses on building the best learning experience specifically for Data Science. We have offices in Boston and Belgium and to date, we trained over 250,000 (aspiring) data scientists in over 150 countries. These data science enthusiasts completed more than 9 million exercises. You can take free beginner courses, or subscribe for $25/month to get access to all premium courses."
words = text.split(' ')
df =  pd.DataFrame(words, columns=['words'])
print df['words'].str.lower().value_counts()
