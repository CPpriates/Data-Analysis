#Nico Salafranca nms6dz
import pandas as pd
import math
from scipy import stats
import numpy as np
f = open('homework4-output-Salafranca-Nicolas.txt', 'w') 

reviews = pd.read_csv('reviews.txt', 
                        sep='\t',
                        header=None,
                        names=['Reviewer','Movie','Rating','Date'])

reviewers = pd.read_csv('reviewers.txt',
                        sep='|',
                        header=None,
                        names=['Reviewer', 'age','gender','occupation','zip code'])
                        
genres = pd.read_csv('genres.txt', sep='|', header=None,
                     names=['Movie', 'movie title','release date','video release date'
                     ,'IMDb URL', 'unknown', 'Action', 'Adventure','Animation'
                     ,'Childrens','Comedy','Crime','Documentary','Drama','Fantasy'
                     ,'Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi'
                     ,'Thriller','War','Western'])

zipcodes = pd.read_csv('zipcodes.txt', sep=',',header=None,
                       names=['Zipcode','ZipCodeType','City',
                              'State','LocationType','Lat','Long','Location','Decommisioned'])
#1                              
(reviews.groupby(['Rating']).count()/(len(reviews)))*100
print("Problem 1:", file=f)
print(" 1 : 6.110, 2 : 11.370, 3 : 27.145, 4:34.174, 5 : 21.201",file=f)
#2
a = reviews.groupby(['Reviewer']).count().sort_values(by=['Movie'])[-10:]
print("Problem 2: ", file=f)
print("Reviewer : # of Ratings", file=f)
print("393 : 448", file=f)
print("234 : 480", file=f)
print("303 : 484", file=f)
print("537 : 490", file=f)
print("416 : 493", file=f)
print("276 : 518", file=f)
print("450 : 540", file=f)
print("13 : 646", file=f)
print("655 : 685", file=f)
print("405 : 737", file=f)

#3
revlen = len(reviews)
b = reviews.Rating.mean()
bstd = reviews.Rating.std()
#total mean
z = [b - (1.96)*(bstd/math.sqrt(revlen)) ,b + (1.96)*(bstd/math.sqrt(revlen))]
print("problem 3: ", file=f)
print(z,file=f)

#4

reviews.groupby(['Movie']).count().sort_values(by=['Reviewer'])[-10:]
print("Problem 4: ", file=f)
print("Movie : # of ratings", file=f)
print("121 : 429", file=f)
print("300 : 431", file=f)
print("1 : 452", file=f)
print("288 : 478", file=f)
print("286 : 481", file=f)
print("294 : 429", file=f)
print("181 : 507", file=f)
print("100 : 508", file=f)
print("258 : 509", file=f)
print("50 : 583", file=f)

#5
gcount = {'unknown':genres.unknown.sum(),
'Action':genres.Action.sum(),
'Adventure':genres.Adventure.sum(),
'Animation':genres.Animation.sum(),
'Childrens':genres.Childrens.sum(),
'Comedy':genres.Comedy.sum(),
'Crime':genres.Crime.sum(),
'Documentary':genres.Documentary.sum(),
'Drama':genres.Drama.sum(),
'Fantasy':genres.Fantasy.sum(),
'Film-Noir':genres['Film-Noir'].sum(),
'Horror':genres.Horror.sum(),
'Musical':genres.Musical.sum(),
'Mystery':genres.Mystery.sum(),
'Romance':genres.Romance.sum(),
'Sci-Fi':genres['Sci-Fi'].sum(),
'Thriller':genres.Thriller.sum(),
'War':genres.War.sum(),
'Western':genres.Western.sum()}
gcount
print("Problem 5: ", file=f)
print("Most often: Drama - 725", file=f)
print("Least often: unknown - 2", file=f)
#6
count = 0
gg = genrev.drop(genrev[[0,1,2,3,4,5,6,7]], axis=1) #dataframe of only genres
for i in range(0,99999):
    if gg.iloc[i].sum() > 1:#sums the row. if > 1 then review of movie has >1 genre
        count+=1
count #69938
count/100000*100
"""69.938"""
print("Problem 6", file=f)
print(69.938, file=f)
#7
merged = pd.merge(reviews,reviewers, on='Reviewer')
mmean = merged[merged.gender == 'M'].Rating.mean()
mstd = merged[merged.gender == 'M'].Rating.std()
fmean = merged[merged.gender == 'F'].Rating.mean()
fstd = merged[merged.gender == 'F'].Rating.std()
len(merged[merged.gender == 'F'].Rating)
t = stats.t.ppf(1 - 0.025, 670)
t2 = stats.t.ppf(1 - 0.025, 273)

mconf = [mmean - t*(mstd/math.sqrt(670)), mmean + t*(mstd/math.sqrt(670))]
fconf = [fmean - t2*(fstd/math.sqrt(273)), fmean + t2*(fstd/math.sqrt(273))]

print("Problem 7: ", file=f)
print("Male Confidence Interval: ", mconf, file=f)
print("Female Confidence Interval: ", fconf, file=f)

#8 Which state/territory/Canada/unknown produced the top-5 most reviews?
print("Problem 8", file=f)
print(merged.groupby(['zip code']).count().sort_values(by='Reviewer')[-5:], file=f)

#9
print("Problem 9: ", file=f)
movrat = reviews.groupby(['Movie']).count().sort_values(by='Reviewer')
r = movrat[movrat['Reviewer'] == 1]/len(movrat)*100
r1=movrat[movrat['Reviewer'] == 2]/len(movrat)*100
r2=movrat[movrat['Reviewer'] == 3]/len(movrat)*100
r3=movrat[movrat['Reviewer'] == 4]/len(movrat)*100
r4=movrat[movrat['Reviewer'] == 5]/len(movrat)*100
r5=movrat[movrat['Reviewer'] == 6]/len(movrat)*100
r6=movrat[movrat['Reviewer'] == 7]/len(movrat)*100
r7=movrat[movrat['Reviewer'] == 8]/len(movrat)*100
r8=movrat[movrat['Reviewer'] == 9]/len(movrat)*100
r9=movrat[movrat['Reviewer'] == 10]/len(movrat)*100
r10=movrat[movrat['Reviewer'] == 11]/len(movrat)*100
r11=movrat[movrat['Reviewer'] == 12]/len(movrat)*100
r12=movrat[movrat['Reviewer'] == 13]/len(movrat)*100
r13=movrat[movrat['Reviewer'] == 14]/len(movrat)*100
r14=movrat[movrat['Reviewer'] == 15]/len(movrat)*100
r15=movrat[movrat['Reviewer'] == 16]/len(movrat)*100
r16=movrat[movrat['Reviewer'] == 17]/len(movrat)*100
r17=movrat[movrat['Reviewer'] == 18]/len(movrat)*100
r18=movrat[movrat['Reviewer'] == 19]/len(movrat)*100
r19=movrat[movrat['Reviewer'] == 20]/len(movrat)*100
print("% of 1", r, file=f)
print("% of 2",r1,file=f)
print("% of 3",r2, file=f)
print("% of 4",r3, file=f)
print("% of 5",r4, file=f)
print("% of 6",r5, file=f)
print("% of 7",r6, file=f)
print("% of 8",r7,file=f)
print("% of 9",r8, file=f)
print("% of 10",r9, file=f)
print("% of 11",r10, file=f)
print("% of 12",r11,file=f)
print("% of 13",r12, file=f)
print("% of 14",r13, file=f)
print("% of 15",r14, file=f)
print("% of 16",r15, file=f)
print("% of 17",r16, file=f)
print("% of 18",r17, file=f)
print("% of 19",r18, file=f)
print("% of 20",r19, file=f)
#10
genrev = pd.merge(reviews, genres, on='Movie')
print("Problem 10: ", file=f)
print("unknown",np.mean(genrev.Rating[genrev['unknown'] == 1]), file=f)
print("Action",np.mean(genrev.Rating[genrev['Action'] == 1]),file=f)
print("Adventure",np.mean(genrev.Rating[genrev['Adventure'] == 1]),file=f)
print("Animation",np.mean(genrev.Rating[genrev['Animation'] == 1]),file=f)
print("Childrens",np.mean(genrev.Rating[genrev['Childrens'] == 1]),file=f)
print("Comedy",np.mean(genrev.Rating[genrev['Comedy'] == 1]),file=f)
print("Crime",np.mean(genrev.Rating[genrev['Crime'] == 1]),file=f)
print("Documentary",np.mean(genrev.Rating[genrev['Documentary'] == 1]),file=f)
print("Drama",np.mean(genrev.Rating[genrev['Drama'] == 1]),file=f)
print("Fantasy",np.mean(genrev.Rating[genrev['Fantasy'] == 1]),file=f)
print("Film Noir", np.mean(genrev.Rating[genrev['Film-Noir'] == 1]),file=f)
print("Horror",np.mean(genrev.Rating[genrev['Horror'] == 1]),file=f)
print("Musical",np.mean(genrev.Rating[genrev['Musical'] == 1]),file=f)
print("Mystery",np.mean(genrev.Rating[genrev['Mystery'] == 1]),file=f)
print("Romance",np.mean(genrev.Rating[genrev['Romance'] == 1]),file=f)
print("Sci-Fi",np.mean(genrev.Rating[genrev['Sci-Fi'] == 1]),file=f)
print("Thriller",np.mean(genrev.Rating[genrev['Thriller'] == 1]),file=f)
print("War",np.mean(genrev.Rating[genrev['War'] == 1]),file=f)
print("Western",np.mean(genrev.Rating[genrev['Western'] == 1]),file=f)

#11
grever = pd.merge(genrev, reviewers, on='Reviewer')
#Over 30
print("Problem: 11", file=f)
print("Over 30", file=f)
print("Unknown", np.mean((grever.Rating[(genrev['unknown'] == 1) & (grever.age > 30)])),file=f)
print("Action", np.mean((grever.Rating[(genrev['Action'] == 1) & (grever.age > 30)])),file=f)
print("Adventure", np.mean((grever.Rating[(genrev['Adventure'] == 1) & (grever.age > 30)])),file=f)
print("Animation", np.mean((grever.Rating[(genrev['Animation'] == 1) & (grever.age > 30)])),file=f)
print("Children's", np.mean((grever.Rating[(genrev['Childrens'] == 1) & (grever.age > 30)])),file=f)
print("Comedy", np.mean((grever.Rating[(genrev['Comedy'] == 1) & (grever.age > 30)])),file=f)
print("Crime", np.mean((grever.Rating[(genrev['Crime'] == 1) & (grever.age > 30)])),file=f)
print("Docu", np.mean((grever.Rating[(genrev['Documentary'] == 1) & (grever.age > 30)])),file=f)
print("Drama", np.mean((grever.Rating[(genrev['Drama'] == 1) & (grever.age > 30)])),file=f)
print("Fantasy", np.mean((grever.Rating[(genrev['Fantasy'] == 1) & (grever.age > 30)])),file=f)
print("Film Noir", np.mean((grever.Rating[(genrev['Film-Noir'] == 1) & (grever.age > 30)])),file=f)
print("Horror", np.mean((grever.Rating[(genrev['Horror'] == 1) & (grever.age > 30)])),file=f)
print("Musical", np.mean((grever.Rating[(genrev['Musical'] == 1) & (grever.age > 30)])),file=f)
print("Mystery", np.mean((grever.Rating[(genrev['Mystery'] == 1) & (grever.age > 30)])),file=f)
print("Romance", np.mean((grever.Rating[(genrev['Romance'] == 1) & (grever.age > 30)])),file=f)
print("Sci-Fi", np.mean((grever.Rating[(genrev['Sci-Fi'] == 1) & (grever.age > 30)])),file=f)
print("Thriller", np.mean((grever.Rating[(genrev['Thriller'] == 1) & (grever.age > 30)])),file=f)
print("War", np.mean((grever.Rating[(genrev['War'] == 1) & (grever.age > 30)])),file=f)
print("Western", np.mean((grever.Rating[(genrev['Western'] == 1) & (grever.age > 30)])),file=f)
#<=30
print("30 and under", file=f)
print("Unknown", np.mean((grever.Rating[(genrev['unknown'] == 1) & (grever.age <= 30)])),file=f)
print("Action", np.mean((grever.Rating[(genrev['Action'] == 1) & (grever.age <= 30)])),file=f)
print("Adventure", np.mean((grever.Rating[(genrev['Adventure'] == 1) & (grever.age <= 30)])),file=f)
print("Animation", np.mean((grever.Rating[(genrev['Animation'] == 1) & (grever.age <= 30)])),file=f)
print("Childrens", np.mean((grever.Rating[(genrev['Childrens'] == 1) & (grever.age <= 30)])),file=f)
print("Comedy", np.mean((grever.Rating[(genrev['Comedy'] == 1) & (grever.age <= 30)])),file=f)
print("Crime", np.mean((grever.Rating[(genrev['Crime'] == 1) & (grever.age <= 30)])),file=f)
print("Doc", np.mean((grever.Rating[(genrev['Documentary'] == 1) & (grever.age <= 30)])),file=f)
print("Drama", np.mean((grever.Rating[(genrev['Drama'] == 1) & (grever.age <= 30)])),file=f)
print("Fantasy", np.mean((grever.Rating[(genrev['Fantasy'] == 1) & (grever.age <= 30)])),file=f)
print("Film Noir", np.mean((grever.Rating[(genrev['Film-Noir'] == 1) & (grever.age <= 30)])),file=f)
print("Horror", np.mean((grever.Rating[(genrev['Horror'] == 1) & (grever.age <= 30)])),file=f)
print("Musical", np.mean((grever.Rating[(genrev['Musical'] == 1) & (grever.age <= 30)])),file=f)
print("Mystery", np.mean((grever.Rating[(genrev['Mystery'] == 1) & (grever.age <= 30)])),file=f)
print("Romance", np.mean((grever.Rating[(genrev['Romance'] == 1) & (grever.age <= 30)])),file=f)
print("Sci-Fi", np.mean((grever.Rating[(genrev['Sci-Fi'] == 1) & (grever.age <= 30)])),file=f)
print("Thriller", np.mean((grever.Rating[(genrev['Thriller'] == 1) & (grever.age <= 30)])),file=f)
print("War", np.mean((grever.Rating[(genrev['War'] == 1) & (grever.age <= 30)])),file=f)
print("Western", np.mean((grever.Rating[(genrev['Western'] == 1) & (grever.age <= 30)])),file=f)

#12a
males = merged[(merged['Rating'] > 3) & (merged['gender'] == 'M')]
females =  merged[(merged['Rating'] > 3) & (merged['gender'] == 'F')]
mmean = males.Rating.count()/len(merged)
fmean = females.Rating.count()/len(merged)
len(males.Rating) #368
len(females.Rating) #158

q = [(fmean - mmean) - 1.96*math.sqrt((fmean*(1-fmean))/158)+((mmean*(1-mmean))/368), 
     (fmean - mmean) + 1.96*math.sqrt((fmean*(1-fmean))/158)+((mmean*(1-mmean))/368)]
"""[-0.0082832026075656279, 0.0041031290075656266]"""
print("Problem 12a: ", file=f)
print("[-0.0082832026075656279, 0.0041031290075656266]", file=f)
#12b
zipcodes2 = pd.read_csv('zipcodes.txt')
big = zipcodes2.loc[zipcodes2['State'].isin(['CA','NY','TX','FL','IL'])].drop(zipcodes2[[0,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]], axis=1)
small = zipcodes2.loc[zipcodes2['State'].isin(['CA','NY','TX','FL','IL'])==False].drop(zipcodes2[[0,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]], axis=1)

bigzip = list(map(str, list(big.Zipcode)))
restzip = list(map(str, list(small.Zipcode)))

bigframe = merged[merged['zip code'].isin(bigzip)]
smallframe = merged[merged['zip code'].isin(restzip)]

bigpos = bigframe[bigframe.Rating > 3]
smallpos = smallframe[smallframe.Rating >3]

sm = smallpos.Rating.count()/len(smallframe)
bg = bigpos.Rating.count()/len(bigframe)

len(smallframe)#54553
len(bigframe)#33185

qq = [(bg - sm) - 1.96*math.sqrt((bg*(1-bg))/33185)+((sm*(1-sm))/54553), 
     (bg - sm) + 1.96*math.sqrt((bg*(1-bg))/33185)+((sm*(1-sm))/54553)]
"""[-0.028166739864550837, -0.017437377426093727]"""
print("problem 12b: ", file=f)
print("[-0.028166739864550837, -0.017437377426093727]", file=f)