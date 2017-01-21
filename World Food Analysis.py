# -*- coding: utf-8 -*-
#Final Project STAT3250
#Group Members: Ruoqi Gao, Anastasia Polkovnichenko, Nicolas Salafranca	

	
import numpy as np # load NumPy
import pandas as pd # load pandas
from scipy.stats import t
import re

ff = pd.read_csv('FoodFacts.csv', encoding = "ISO-8859-1")
ff

#data cleaning

#remove unnecessary columns
del ff['url']
del ff['code']
del ff['creator']
del ff['emb_codes']
del ff['emb_codes_tags']
del ff['image_url']
del ff['image_small_url']
del ff['manufacturing_places']

#only use rows that are completed 

ff['states_en'].isnull().sum().sum()
ff1 = ff.replace(np.nan,' ', regex=True)
ff1['states_en'].isnull().sum().sum()
ff2=ff1[ff1['states_en'].str.contains("To be checked")]

#remove rows where the product name is empty
ff3 = ff2[pd.notnull(ff2['product_name'])]
ff3['product_name'].isnull().sum().sum()

#change the manufacture country names into a consistent format

ff3['manufacturing_places_tags']=ff3['manufacturing_places_tags'].replace(['charlotte,nc',
'norwalk,ct',], 'usa')

ff3['manufacturing_places_tags']=ff3['manufacturing_places_tags'].replace(['thailande','bangkok,thailande'], 'thailand')

ff3.loc[ff3['manufacturing_places_tags'].str.contains('us'), 'manufacturing_places_tags'] = 'usa'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('u-s-a'), 'manufacturing_places_tags'] = 'usa'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('usa'), 'manufacturing_places_tags'] = 'usa'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('united-states'), 'manufacturing_places_tags'] = 'usa'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('california'), 'manufacturing_places_tags'] = 'usa'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('massachusetts'), 'manufacturing_places_tags'] = 'usa'

ff3.loc[ff3['manufacturing_places_tags'].str.contains('france'), 'manufacturing_places_tags'] = 'france'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('italie'), 'manufacturing_places_tags'] = 'italy'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('italia'), 'manufacturing_places_tags'] = 'italy'

ff3.loc[ff3['manufacturing_places_tags'].str.contains('germany'), 'manufacturing_places_tags'] = 'germany'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('suisse'), 'manufacturing_places_tags'] = 'suisse'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('danmark'), 'manufacturing_places_tags'] = 'danmark'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('australia'), 'manufacturing_places_tags'] = 'australia'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('india'), 'manufacturing_places_tags'] = 'india'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('canada'), 'manufacturing_places_tags'] = 'canada'

ff3.loc[ff3['manufacturing_places_tags'].str.contains('espana'), 'manufacturing_places_tags'] = 'spain'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('united-kingdom'), 'manufacturing_places_tags'] = 'uk'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('great-britain',), 'manufacturing_places_tags'] = 'uk'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('uk'), 'manufacturing_places_tags'] = 'uk'

ff3.loc[ff3['manufacturing_places_tags'].str.contains('grece'), 'manufacturing_places_tags'] = 'grece'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('deutschland'), 'manufacturing_places_tags'] = 'deutschland'
ff3.loc[ff3['manufacturing_places_tags'].str.contains('alemania'), 'manufacturing_places_tags'] = 'alemania'

ff3

#standardize the label column(since we're only interested in Vegetarian food, 
#we only standardize relevent rows)
ff3.loc[ff3['labels_tags'].str.contains('vegetarian'),'labels_tags']='vegetarian'       
ff3.loc[ff3['labels_tags'].str.contains('vegan'),'labels_tags']='vegetarian'       
ff3



##How many countries are represented in the dataset?
#this part also involves datacleaning
list1=ff3.countries_en.unique() #unique country names, however, this 
#includes columns with multiple country names seperated by ','
str1 = ''.join(list1) # convert to string to operate
str1=str1.replace(",", " ")
str1=re.sub(r"(\w)([A-Z])", r"\1 \2", str1) #add space between upper and lower 
#case letters
list2 = str1.split()# split by space
list3=set(list2) #unique values in list2
list3=[ x for x in list3 if "_" not in x ]#clean up the strange names which 
#doesn't correspond to countries
list3=[ x for x in list3 if ":" not in x ]#clean up
#eliminate double counted countries
list3=[ x for x in list3 if "New" not in x ]# bc 'new zealand' is one country
list3=[ x for x in list3 if "Republic" not in x ]# 'Czech Republic'
list3=[ x for x in list3 if "United" not in x ]
list3=[ x for x in list3 if "Arab" not in x ]
#united states, united kingdom and United Arab Emirates has been 
#counted as'states', 'kingdom' and 'emirates'already
list3=[ x for x in list3 if "Saint" not in x ]
list3=[ x for x in list3 if "Pierre" not in x ]
list3=[ x for x in list3 if "and" not in x ]
#'saint pierre and miquelon' is duplicated multiple times
list3=[ x for x in list3 if "Sri" not in x ]#'Sri Lanka'
list3=[ x for x in list3 if "toSouth" not in x ]#'South Africa'

list3
len(list3)


##top5 countries that manufactured the most products
ff3['manufacturing_places_tags'].groupby(ff3['manufacturing_places_tags']).value_counts().nlargest(7) 

##Most commonly used packaging in top manufacturing countries
ff4=ff3.loc[ff3['manufacturing_places_tags'].isin(['france'])]
ff4['packaging_tags'].groupby(ff4['packaging_tags']).value_counts().nlargest(6) 
ff5=ff3.loc[ff3['manufacturing_places_tags'].isin(['spain'])]
ff5['packaging_tags'].groupby(ff5['packaging_tags']).value_counts().nlargest(6) 
ff6=ff3.loc[ff3['manufacturing_places_tags'].isin(['italy'])]
ff6['packaging_tags'].groupby(ff6['packaging_tags']).value_counts().nlargest(6) 
ff7=ff3.loc[ff3['manufacturing_places_tags'].isin(['usa'])]
ff7['packaging_tags'].groupby(ff7['packaging_tags']).value_counts().nlargest(6) 
ff8=ff3.loc[ff3['manufacturing_places_tags'].isin(['deutschland'])]
ff8['packaging_tags'].groupby(ff8['packaging_tags']).value_counts().nlargest(6) 
# could visualize the result and give a conclusion here
#result in different language we could translate and say what material is most commonly used

#Which foods contain ingredients from palm oil, and what countries manufactured them?
ffpm=ff3[ff3.ingredients_from_palm_oil_n!=0]
ffpm['manufacturing_places_tags']

##which foods are the most environemental friendly? (a better packaging, 
#no plastic, preferably paper or aluminum, no palm oil ingredients, and less 
#additives.)

#1.select product with environ friendly packaging
ffenpack1=ff3[ff3['packaging_tags'].str.contains('paper')]       
ffenpack2=ff3[ff3['packaging_tags'].str.contains('can')]   
       
ffenpack = ffenpack1.append(ffenpack2, ignore_index=True)

#2.select product with environ friendly ingredients
ffpalm=ff3[ff3['ingredients_from_palm_oil_n']==0]
ffadd=ff3[ff3['additives_n']==0]

#3.merge together inner
en1 = pd.merge(ffenpack, ffpalm, how='inner', on=['created_t'])
en2 = pd.merge(en1, ffadd, how='inner', on=['created_t'])

encountry=en2.product_name_x.unique() #products that are most environmentally friendly
print(encountry)

##Do vegetarian foods tend to be more environmentally friendly as compared 
#to other foods?
ffve=ff3[ff3.labels_tags == 'vegetarian']
enve = pd.merge(en2, ffve, how='inner', on=['created_t'])
len(enve.product_name_x.values)/len(ffve.product_name.values)
"""
0.005154639175257732 0.52% vegetarian food are environmental friendly
"""
ffnonve=ff3[ff3.labels_tags != 'vegetarian']
len(ffnonve.product_name.values)
ennonve = pd.merge(en2, ffnonve, how='inner', on=['created_t'])
len(ennonve.product_name_x.values)/len(ffnonve.product_name.values)
"""
0.0035746201966041107 0.36% non vegetarian food are environmental friendly
"""

##For top 3 most common countries, what produce the largest proportion of  
#environmentally friendly products (originally we asked for 'city' but since 
#the number is so small, i think country is ok)?
group1=ff3['countries_en'].groupby(ff3.countries_en)
group1.count().nlargest(3)
"""
france     27477
spain       2598
germany     1995
"""
fffrance=ff3[ff3.countries_en == 'france']
enfr = pd.merge(en2, fffrance, how='inner', on=['created_t'])
len(enfr.product_name_x.values)/len(fffrance.product_name.values)
"""
0.0
"""
ffspain=ff3[ff3.countries_en == 'spain']
ensp = pd.merge(en2, ffspain, how='inner', on=['created_t'])
len(ensp.product_name_x.values)/len(ffspain.product_name.values)
"""
0.0
"""
ffgermany=ff3[ff3.countries_en == 'germany']
enge = pd.merge(en2, ffgermany, how='inner', on=['created_t'])
len(enge.product_name_x.values)/len(ffgermany.product_name.values)
"""
0.012030075187969926 Germany produc the most environmental friendly products
 """
##which products are consumed in more than one countries, and how many of them?
#consider two categories for this question, then find the unique value of two lists
#1. sampe product name, other columns different, different country names
dictionary ={}
for i in ff3.index:
    food=ff3.loc[i,'product_name']
    country=ff3.loc[i,'countries_en']
    if food not in dictionary:
        dictionary[food]=set()
    dictionary[food].add(country)
dictionary
result1=[]
for key in dictionary:
    if len(dictionary[key])>=2:
        result1.append(key)
print(result1)
print(len(result1))

#2. exact same product, two country names appear in the countries_en column
ff10=ff3[ff3['countries_en'].str.contains(',')]       
result2=[] 
for name in ff10.product_name:
    result2.append(name)
print(result2)
print(len(result2))    

#3. find the unique in two lists
lista=list(set().union(result1, result2))
len(np.unique(lista))
print(len(lista))

"""
1262 products consumed in more than one countries
"""

# create a new dataframe that contains the food consumed in more than one countries
ffm = pd.DataFrame([])
ffm=ffm.append(ff3[ff3.product_name.isin(lista)])
print(ffm)
#to be used in later parts
 

#What are the top three most commonly listed food
ff9=ff3[ff3.duplicated(['product_name'],keep=False)]
ff9['product_name'].groupby(ff9['product_name']).value_counts().nlargest(3)
"""
Huile d'olive vierge extra          Huile d'olive vierge extra            25
Mayonnaise íæ la moutarde de Dijon  Mayonnaise íæ la moutarde de Dijon    24
Moutarde de Dijon                   Moutarde de Dijon                     24
"""

#What is the 95% CI for the average sugar content for American and French and 
#are they significantly different? What about for French vs. Spanish?
ffus=ff3[ff3.countries_en.str.contains('United States')]
listus=[float(i) for i in ffus.sugars_100g.values if i!=' ']
meansugarus=np.mean(listus)
stdsugarus=np.std(listus,ddof=1)
nus=len(listus)
t1=t.ppf(1-0.025,nus-1)
lower1=meansugarus-t1*stdsugarus/nus**0.5
upper1=meansugarus+t1*stdsugarus/nus**0.5
print(lower1,upper1)
"""
12.0626994241 15.0879831155
"""
fffr=ff3[ff3.countries_en.str.contains('France')]
listfr=[float(i) for i in fffr.sugars_100g.values if i!=' ']
meansugarfr=np.mean(listfr)
stdsugarfr=np.std(listfr,ddof=1)
nfr=len(listfr)
t2=t.ppf(1-0.025,nfr-1)
lower2=meansugarus-t2*stdsugarfr/nfr**0.5
upper2=meansugarus+t2*stdsugarfr/nfr**0.5
print(lower2,upper2)
"""
13.3342284437 13.8164540959
"""
m1=meansugarfr-meansugarus
s1=(stdsugarfr**2/nfr+stdsugarus**2/nus)**0.5
td1=m1/s1
"""
-1.5437540875685072, dont't reject null, no significant difference btw US and France
"""
ffsp=ff3[ff3.countries_en.str.contains('Spain')]
listsp=[float(i) for i in ffsp.sugars_100g.values if i!=' ']
meansugarsp=np.mean(listsp)
stdsugarsp=np.std(listfr,ddof=1)
nsp=len(listsp)
t3=t.ppf(1-0.025,nsp-1)
lower3=meansugarsp-t3*stdsugarsp/nsp**0.5
upper3=meansugarsp+t3*stdsugarfr/nsp**0.5
print(lower3,upper3)
"""
9.42439939532 11.1949628496
"""
m2=meansugarfr-meansugarsp
s2=(stdsugarfr**2/nfr+stdsugarsp**2/nsp)**0.5
td2=m2/s2

"""
4.4079551186493076, reject null, significant difference btw Spain and France
"""


#nutrition compared across countries. Compare nutrition of food consumed in 
#more that one countires with the statistics in all countries in terms of 
#nutrition(sugar,salt,fat,fiber,protein)
group1=ff3['countries_en'].groupby(ff3.countries_en)
group1.count().nlargest(5)
"""
france            27477
spain              2598
germany            1995
united kingdom     1215
united states       607

these countries appear most often, could use them to compare with total
"""

ff3.countries_en = ff3.countries_en.str.lower()
def meanv(l):
    return float(sum(l)) / len(l)
ffsugars = ff3[ff3.sugars_100g!=' ']

def r_sugars(country):
    return ffsugars[ffsugars.countries_en.str.contains(country)].sugars_100g.tolist() 
uk_sugars = r_sugars('united kingdom')
us_sugars = r_sugars('united states')
sp_sugars = r_sugars('spain')
fr_sugars = r_sugars('france') 
de_sugars = r_sugars('germany')
all_sugars= ffsugars.sugars_100g.tolist()
morethantwo_sugars=ffsugars[ffsugars.product_name.isin(lista)].sugars_100g.tolist()
countries = [ 'UK', 'US', 'SP', 'FR', 'DE','ALL','MTT']
sugars_l = [meanv(uk_sugars), 
            meanv(us_sugars), 
            meanv(fr_sugars),
            meanv(sp_sugars), 
            meanv(de_sugars),
            meanv(all_sugars),
            meanv(morethantwo_sugars)]


ffsalt = ff3[ff3.salt_100g!=' ']
def r_salt(country):
    return ffsalt[ffsalt.countries_en.str.contains(country)].salt_100g.tolist() 
uk_salt = r_salt('united kingdom')
us_salt = r_salt('united states')
sp_salt = r_salt('spain')
fr_salt = r_salt('france') 
de_salt = r_salt('germany')
all_salt= ffsalt.salt_100g.tolist()
morethantwo_salt=ffsalt[ffsalt.product_name.isin(lista)].salt_100g.tolist()
countries = [ 'UK', 'US', 'SP', 'FR', 'DE','ALL','MTT']
salt_l = [meanv(uk_salt), 
            meanv(us_salt), 
            meanv(fr_salt),
            meanv(sp_salt), 
            meanv(de_salt),
            meanv(all_salt),
            meanv(morethantwo_salt)]  
  
  
fffat = ff3[ff3.fat_100g!=' ']
def r_fat(country):
    return fffat[fffat.countries_en.str.contains(country)].fat_100g.tolist() 
uk_fat = r_fat('united kingdom')
us_fat = r_fat('united states')
sp_fat = r_fat('spain')
fr_fat = r_fat('france') 
de_fat = r_fat('germany')
all_fat= fffat.fat_100g.tolist()
morethantwo_fat=fffat[fffat.product_name.isin(lista)].fat_100g.tolist()
countries = [ 'UK', 'US', 'SP', 'FR', 'DE','ALL','MTT']
fat_l = [meanv(uk_fat), 
            meanv(us_fat), 
            meanv(fr_fat),
            meanv(sp_fat), 
            meanv(de_fat),
            meanv(all_fat),
            meanv(morethantwo_fat)]    
            
fffiber = ff3[ff3.fiber_100g!=' ']
def r_fiber(country):
    return fffiber[fffiber.countries_en.str.contains(country)].fiber_100g.tolist() 
uk_fiber = r_fiber('united kingdom')
us_fiber = r_fiber('united states')
sp_fiber = r_fiber('spain')
fr_fiber = r_fiber('france') 
de_fiber = r_fiber('germany')
all_fiber= fffiber.fiber_100g.tolist()
morethantwo_fiber=fffiber[fffiber.product_name.isin(lista)].fiber_100g.tolist()
countries = [ 'UK', 'US', 'SP', 'FR', 'DE','ALL','MTT']
fiber_l = [meanv(uk_fiber), 
            meanv(us_fiber), 
            meanv(fr_fiber),
            meanv(sp_fiber), 
            meanv(de_fiber),
            meanv(all_fiber),
            meanv(morethantwo_fiber)]    

ffpro = ff3[ff3.proteins_100g!=' ']
def r_pro(country):
    return ffpro[ffpro.countries_en.str.contains(country)].proteins_100g.tolist() 
uk_pro = r_pro('united kingdom')
us_pro = r_pro('united states')
sp_pro = r_pro('spain')
fr_pro = r_pro('france') 
de_pro = r_pro('germany')
all_pro= ffpro.proteins_100g.tolist()
morethantwo_pro=ffpro[ffpro.product_name.isin(lista)].proteins_100g.tolist()
countries = [ 'UK', 'US', 'SP', 'FR', 'DE','ALL','MTT']
protein_l = [meanv(uk_pro), 
            meanv(us_pro), 
            meanv(fr_pro),
            meanv(sp_pro), 
            meanv(de_pro),
            meanv(all_pro),
            meanv(morethantwo_pro)]     
            
#pnns_groups_1 categories could be used
            
#(if we want more analysis we could analyse the nutrition in different categories
#depending on the space on our report)