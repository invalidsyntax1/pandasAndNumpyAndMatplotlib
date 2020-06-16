import pandas as pd

mountains = pd.read_csv('train.csv', dtype = {'Height (m)':int})
print(mountains['Height (m)'])

def heightMountains(row):
    if pd.isnull(row['Height (m)']):
        if row['Height (m)'] < 7500:
            return 'High'
        elif row['Height (m)'] > 8500:
            return 'Extremely high'
        else:
            return 'Very high'
    else:
        return 'Undefined'
        
        
        
mountains['heightMountains'] = mountains.apply(heightMountains, axis=1)
print(mountains)