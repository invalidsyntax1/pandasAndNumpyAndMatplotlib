#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ## Обработка данных с помощью pandas

# ### Если в файле содержатся просто строчки, где в виде словаря  какие-то столбцы
# 

# In[7]:


dataList =[
    {'date':'2017-07-01', 'value': 100},
    {'date':'2017-07-02', 'value': 200},
    {'date':'2017-07-03', 'value': 300},
    {'date':'2017-07-04', 'value': 400},
    {'date':'2017-07-05', 'value': 500},
]
a = pd.DataFrame(dataList) #pandas это спокойно прочитает  и вернёт как таблицу
a


# In[8]:


dataDict = {
    'date': ['2017-07-01', '2017-07-02', '2017-07-03', '2017-07-04', '2017-07-05'],
    'value': [100, 200, 300, 400, 500]
}
a1 = pd.DataFrame.from_dict(dataDict)
a1


# ### Создание Series

# In[10]:


dataNp = np.random.rand(3)
dataNp


# In[11]:


b = pd.Series(dataNp, index = ["one", "two", "three"])
b


# ### Импорт данных для DataFrame файлов

# In[12]:


data = pd.read_csv('train.csv') #файл train.csv - любой csv файл
b1 = data.head(20) #первые 20 строк того,что есть в файле
b2 = data.tail(20) #последние 20 строк того, что есть в файле
b3 = data.info()
data = pd.read_csv('train.csv', dtype={'SibSp': str, 'Parch': str, 'Pclass':str}) #dtype - указывает, какой тип данных в этом столбце int, str, float или другие
# pandas определяет строки ни как str, а как object
data.describe() #статистические характеристики столбцов, если столбец является числом


# In[13]:


b1


# In[14]:


b2


# In[15]:


data_Pclass = data['Pclass']


# In[16]:


type(data_Pclass)


# In[17]:


data_Pclass.head()


# In[18]:


data_Pclass.value_counts() #количество повторений того числа в столбце


# #### Для того, что рисовать в браузере, matplotlib это встроенная библиотека для строения графиков

# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


get_ipython().run_line_magic('time', '')
data.hist(column=['Age']) #вывод гистограмы она как и value_counts подсчитывает сколько раз был встречен тот или иной объект, после чего строит гистограмму


# In[22]:


data['Age'].hist(bins=25, figsize=(10,5))


# In[23]:


df1 = pd.DataFrame([(0,1), (2,3), (4,5)], columns=['value1', 'value2'])
df1


# In[24]:


df2 = pd.DataFrame([(10,11), (12,13), (14,15), (17, 18)], columns=['value1', 'value2'])
df2


# In[25]:


sum_df = df1 + df2 #сложение двух DataFrame
#при этом складываются только в том месте, где обе DataFrame имеют значение, если в одном из DataFrame нет значений, то будет NaN
sum_df


# In[26]:


df2 = pd.DataFrame([(10,11), (12,13), (14,15), (17, 18)], columns=['value1', 'value3'])
df2


# In[27]:


sum_df = df1 + df2
sum_df # только первый столбец будет не полностью NaN т.к. в других стобцах в одном из DataFrame есть значение, а в другой нет


# In[28]:


df1.add(df2, fill_value = 100).fillna(0) #fill_value заполнит вместо NaN будет 100+значение из одной из DataFrame
#если значения нет ни в одной из DataFrame, то fillna заполнит её в данном случае нулём


# In[29]:


df1.mul(df2, fill_value=0) #перемножение DataFrame


# In[30]:


df1.div(df2, fill_value=1) #деление DataFrame


# In[31]:


df1.sub(df2) #разность DataFrame


# ## НЕ копировать переменные в виде df1=df2 т.к. один из них ссылается на другой
# 

# In[32]:


df1 = pd.DataFrame([(0,1), (2,3), (4,5)], columns=['value1', 'value2'])
df1


# In[33]:


df2 = df1.copy() #правильное копирование, метод pd.DataFrame().copy() он вшит в сам pandas


# In[34]:


df2['value1'][0] = 43
df2


# In[35]:


df1


# ### Сводные таблицы

# In[36]:


data = pd.read_csv('train.csv')
data.head()


# In[37]:


#index - значение столбца, которые будут в строках
#columns - значение столбца, которые образуют столбцы
#values - хначения в ячейках ьаблицы

#среднее значение столбца 'Age' в разбивке по Sex и Embarked
pd.pivot_table(data, index = ['Sex', 'Pclass'], columns = ['Embarked'], values = 'Age', aggfunc= np.mean)


# ## НАЧАЛО ПРАКТИКИ

# In[84]:


mountains = pd.read_csv('mountains.csv', dtype={'Height (m)': int})
type(mountains)


# In[39]:


mountains.describe()


# In[46]:


first_ascent = mountains['First ascent']
first_ascent_value = first_ascent.value_counts()
first_ascent_value


# In[41]:


first_ascent.hist(bins=100, figsize=(30,5))


# In[83]:


mountains['Height (m)'][0]


# In[87]:


def heightMountains(row):

    if not pd.isnull(row['Height (m)']):
        if row['Height (m)'] < 7500:
            return 'High'
        elif row['Height (m)'] > 8000:
            return 'Extremely high'
        else:
            return 'Very high'
    else:
        return 'Undef'


# In[89]:


mountains['heightMountains'] = mountains.apply(heightMountains, axis=1)
mountains


# In[91]:


mountains['heightMountains'].value_counts()


# ## КОНЕЦ ПРАКТИКИ

# ### Apply- применить функцию к столбцу или строке

# In[93]:


data = pd.read_csv('train.csv')
data.head()


# In[94]:


def ageGroup(row):
    """
    Простая функция отношения возраста к группе людей
    """
    if not pd.isnull(row['Age']): #проверяем есть ли данные об этом при pd.isnull=False - данные не нулевые, т.е им присвоено какаое-то значение
        if row['Age'] <= 18:
            return 'Child'
        elif row['Age'] >=65:
            return 'Retiree'
        else:
            return 'Young'
    else:
        return 'Undefined'


# In[100]:


#apply - это метод, который говорит взять каждую строчку и применить к ней какую-либо функцию, в данном случае ageGroup
data['ageGroup'] = data.apply(ageGroup, axis = 1) # axis может быть либо 0 либо 1, при 0, функция будет пробегаться по столбцу, при 1 по строке
data
# в data появится новый столбец


# ### Applymap - применение функции к каждой ячейке

# In[96]:


df = pd.DataFrame(np.random.randn(10,3), columns=['first', 'second', 'third']) # создание случайного dataframe
df


# In[97]:


res = df.apply(lambda x: x**2) 
res #в каждой ячейке будет новое чило, которое будет в квадрате ячейки из df


# In[98]:


data['ageGroup'].value_counts()


# In[101]:


data['ageGroup'].isin(['Young', 'Undefined'])


# In[99]:


data[data['ageGroup'].isin(['Young', 'Undefined'])] #isin - фильтр, из DataFrame он возьмёт только те DataFrame где есть в нашем случае Young и Undefined в столбце ageGroup 


# ## Сохранение DataFrame

# In[102]:


data.head()


# In[103]:


#data.to


# In[104]:


# sep - разделитель, по умолчанию запятая
# na_rep - что ставим на место пустых ячеек
# columns - какие стобцы хотим записать
# index - включать ли номер строки
data.to_csv('train_modified.csv', sep=';', na_rep='0', columns=['Survived', 'ageGroup'], index = False)


# In[105]:


# ?pd.DataFrame.to_csv описание методов


# In[114]:


data.to_json('train_json_index.json', orient = 'index')
# создаст json файл в виде {"0":{"PassengerId":1,"Survived":0,"Pclass":3,"Name":"Braund, Mr. Owen Harris","Sex":"male","Age":22.0,"SibSp":1,"Parch":0,"Ticket":"A\/5 21171","Fare":7.25,"Cabin":null,"Embarked":"S","ageGroup":"Young"},"1":{"PassengerId":2,"Survived":1,"Pclass":1,"Name":"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","Sex":"female","Age":38.0,"SibSp":1,"Parch":0,"Ticket":"PC 17599","Fare":71.2833,"Cabin":"C85","Embarked":"C","ageGroup":"Young"},"2":
# это из-за значения orient


# In[115]:


data.to_json('train_json_records.json', orient = 'records') # создаст json файл в виде [{"PassengerId":1,"Survived":0,"Pclass":3,"Name":"Braund, Mr. Owen Harris","Sex":"male","Age":22.0,"SibSp":1,"Parch":0,"Ticket":"A\/5 21171","Fare":7.25,"Cabin":null,"Embarked":"S","ageGroup":"Young"},{"PassengerId":2,"Survived":1,"Pclass":1,"Name":"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","Sex":"female","Age":38.0,"SibSp":1,"Parch":0,"Ticket":"PC 17599","Fare":71.2833,"Cabin":"C85","Embarked":"C","ageGroup":"Young"},{"PassengerId":3,"Survived":1,"Pclass":3,"Name":"Heikkinen, Miss. Laina","Sex":"female","Age":26.0,"SibSp":0,"Parch":0,"Ticket":"STON\/O2. 3101282","Fare":7.925,"Cabin":null,"Embarked":"S","ageGroup":"Young"},{"PassengerId":4,"Survived":1,"Pclass":1,"Name":"Futrelle, Mrs. Jacques Heath (Lily May Peel)","Sex":


# In[116]:


data.to_json('train_json_columns.json', orient = 'columns') # создаст json файл в виде {"PassengerId":{"0":1,"1":2,"2":3,"3":4,"4":5,"5":6,"6":7,"7":8,"8":9,"9":10,"10":11,"11":12,"12":13,"13":14,"14":15,"15":16,"16":17,"17":18,"18":19,"19":20,"20":21,"21":22,"22":23,"23":24,"24":25,"25":26,"26":27,"27":28,"28":29,"29":30,"30":31,"31":32,"32":33,"33":34,"34":35,"35":36,"36":37,"37":38,"38":39,"39":40,"40":41,"41":42,"42":43,"43":44,"44":45,"45":46,"46":47,"47":48,"48":49,"49":50,"50":51,"51":52,"52":53,"53":54,"54":55,"55":56,"56":57,"57":58,"58":59,"59":60,"60":61,"61":62,"62":63,"63":64,"64":65,"65":66,"66":67,"67":68,"68":69,"69":70,"70":71,"71":72,"72":73,"73":74,"74":75,"75":76,"76":77,"77":78,"78":79,"79":80,"80":81,"81":82,"82":83,"83":84,"84":85,"85":86,"86":87,"87":88,"88":89,"89":90,"90":91,"91":92,"92":93,"93":94,"94":95,"95":96,"96":97,"97":98,"98":99,"99":100,"100":101,"101":102,"102":103,"103":104,"104":105,"105":106,"106":107,"107":108,"108":109,"109":110,"110":111,"111":112,"112":113,"113":114,"114":115,"115":116,"116":117,"117":118,"118":119,"119":120,"120":121,"121":122,"122":123,"123":124,"124":125,"125":126,"126":127,"127":128,"128":129,"129":130,"130":131,"131":132,"132":133,"133":134,"134":135,"135":136,"136":137,"137":138,"138":139,"139":140,"140":141,"141":142,"142":143,"143":144,"144":145,"145":146,"146":147,"147":148,"148":149,"149":150,"150":151,"151":152,"152":153,"153":154,"154":155,"155":156,"156":157,"157":158,"158":159,"159":160,"160":161,"161":162,"162":163,"163":16


# In[118]:


# сохранение в Excel
data.to_excel('train_modified.xlsx', sheet_name = 'data')


# ### Типовые действия с DF

# In[120]:


data = pd.read_csv('train.csv')
data.head(3)


# In[122]:


dataSelected = data.loc[:3, ['Name', 'Age', 'Cabin']] #в pandas будет работать не  0,1,2 как в обычном массиве python, а 0,1,2,3
dataSelected.head()


# In[123]:


dataSelected = data.loc[2:15, ['Name', 'Age', 'Cabin']] #в pandas будет работать не  0,1,2,3,4...14 как в обычном массиве python , а 0,1,2,3, 4... 15
dataSelected


# ### Добавить столбцы

# In[124]:


data['nameLength'] = data['Name'].str.split(' ') #так же, как в python работает split() 
data


# In[126]:


data['nameLength'] = data['Name'].str.split(' ').str.len() #так же, как в python работает len() 
data


# In[127]:


del data['nameLength'] #удаление стобца
data


# In[128]:


data.rename(columns = {'Name':'FIO'}, inplace = True) #переименование столбца
# параметр inplace указывает, что надо подставить новое значение в самом DataFrame data, если inplace - False(по умолчанию), то сделается копия, она выведется, после чего эта копия забудется
data


# In[129]:


data.FIO # так можно обратиться к столбцу, однако, если столбец написан через пробел таким образом обратиться к столбцу не удастся


# In[130]:


# можно заменить все названия столбцов
data.columns = ['ID', 'Survived', 'Class', 'FIO123', 'Gender', 'Age', 'SibSp', 'Parch', 'Ticker number', 'Fare', 'Cabin', 'Emnarked']
data


# ### Действия со строками

# In[131]:


data.loc[0:1]


# In[133]:


dataNew = data.iloc[[1,2,3,44]] # отдельные, определённые столбцы 
dataNew


# In[135]:


dataNew.reset_index(inplace=True) # индексы снова станут 0, 1, 2, 3; а не как в предыдущем примере 1,2,3,44
dataNew


# In[136]:


# при этой операции создаётся новый столбец со старым индексом
# его можно удалить
del dataNew['index']
dataNew


# In[139]:


mask = (data.ID % 2 == 0)
mask


# In[140]:


data.loc[mask]


# In[141]:


data[data.ID % 2 == 0]


# ### Работа с пустыми значениями

# In[142]:


data = pd.read_csv('train.csv')
data.head(10)


# In[143]:


data.info()


# In[144]:


data.loc[pd.isnull(data['Age'])] # фильтрует тех людей у которых не указан возраст


# In[145]:


data.loc[~pd.isnull(data['Age'])]# фильтрует тех людей у которых указан возраст


# In[146]:


medianAge = data['Age'].median() # средний возраст людей в таблице
medianAge


# In[148]:


data.fillna(medianAge, inplace=True) # заполнит все значения NaN средним возрастом(в данном случае 28)
data


# ### Сортировка

# In[149]:


data.sort_index(ascending=False)


# In[150]:


# сортировка по значениям
data[~pd.isnull(data['Age'])].sort_values(by = 'Age', ascending=False)


# In[152]:


# сортировка по значениям нескольких столбцов
data.sort_values(by = ['Sex', 'Age'], ascending = [True, False])


# ### Агрегация и группировка

# In[153]:


data = pd.read_csv('train.csv')
data


# In[158]:


#число непустых строк в DataFrame
data.count()


# In[157]:


data['Age'].count()


# In[159]:


data.sum() #сумма


# In[160]:


data.mean() #среднее значение


# In[161]:


data.aggregate(['sum','mean']) #и сумма и среднее значение


# In[162]:


data.agg({'Age':['mean'], 'Survived':['mean', 'sum']})


# In[167]:


# группировка по столбцу с вычислением среднего
data.groupby('Sex').mean().reset_index()


# In[170]:


data.groupby(['Sex', 'Age']).mean().reset_index()


# ### Объединение DataFrame

# In[175]:


df1 = pd.DataFrame({'key1':['one', 'two', 'three', 'only1'], 'value':[1,2,3,4]})
df1


# In[178]:


df2 = pd.DataFrame({'key2':['one', 'two', 'three', 'only2'], 'value':[11,12,13,14]})
df2


# In[179]:


df1.merge(df2, how='left', left_on='key1', right_on='key2') # из-за left он берёт все ключи из df1 и ищет их в df2 в key2 если находит то пишет значение, если нет, то NaN
#в df1 все значение сохраняются а в df2 остаётся только то, что есть в df1


# In[180]:


df1.merge(df2, how='right', left_on='key1', right_on='key2')
#соответственно наоборот,все значения сохраняются в df2, а в df1 только те, которые есть в df2


# In[181]:


df1.merge(df2, how='outer', left_on='key1', right_on='key2')
#все значения ключей. Те ключи которые не совпали просто уходят на следующую строку


# In[182]:


df1.merge(df2, how='inner', left_on='key1', right_on='key2')
#объединяются только те ключи, которые есть в обох df


# In[184]:


# Concat - склеивание DataFrame
pd.concat([df1, df2]) # по вертикали


# In[185]:


pd.concat([df1, df2], axis = 1) # по горизантали


# #### Join - объединение по индексу

# In[186]:


df1 = pd.DataFrame({'key1':['one', 'two', 'three', 'only1'], 'value':[1,2,3,4]}, index = ['0', '1', '2', '3'])
df1


# In[187]:


df2 = pd.DataFrame({'key2':['one', 'two', 'three', 'only2'], 'value':[11,12,13,14]}, index = ['2', '3', '4', '5'])
df2


# In[188]:


df1.join(df2, how='left', lsuffix="_df1", rsuffix='_df2')


# In[ ]:




