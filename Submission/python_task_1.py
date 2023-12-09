import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    #x=pd.read_csv('dataset-1.csv')
    df=x.pivot(index='id_1', columns='id_2', values='car')
    df.fillna(0, inplace=True)
    #print(x)

    return df
df = pd.read_csv('dataset-1.csv')

result_df = generate_car_matrix(df)

print(result_df)

def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    car_type=[]
    for value in df['car']:
        if value<=15:
            car_type.append('low')
        elif value<=25 and value>15:
            car_type.append('medium')
        else:
            car_type.append('high')
    #print(car_type)
    df['car_type']=car_type
    df[['car','car_type']]
    #print(df['car'])
    counts = dict()
    for word in df['car_type']:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    #print(counts)
    return counts
df = pd.read_csv('dataset-1.csv')

type_counts = get_type_count(df)

print(type_counts)

def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    x=0
    count=0
    for i in df['bus']:
        x=x+i
        count+=1
    avg=x/count
    #print(df.index.values)
    #print(x,count,avg)
    bus_index=[]
    count=[]
    for i, j in zip(df['bus'], df.index.values):
        if i>(2*avg):
            bus_index.append(j)
    #print(bus_index)
    return bus_index
df = pd.read_csv('dataset-1.csv')

bus_index = get_bus_indexes(df)

print(bus_index)


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    route=[]
    for i, j in zip(df['bus'], df['route']):
        if i>7:
            route.append(j)
        
    route.sort()
    #print(route)
    return route

df = pd.read_csv('dataset-1.csv')

result = filter_routes(df)

print(result)

def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    modified_matrix = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    matrix = modified_matrix.round(1)
    return matrix



def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    df['duration'] = df['end_timestamp'] - df['start_timestamp']

    completeness_check = df.groupby(['id', 'id_2']).apply(lambda x: (x['duration'].sum() >= pd.Timedelta(days=7)) and (x['start_timestamp'].min().time() == pd.Timestamp.min.time()) and (x['end_timestamp'].max().time() == pd.Timestamp.max.time()))

    return completeness_check

dataset_2_df = pd.read_csv('dataset-2.csv')

completeness_results = time_check(dataset_2_df)

print(completeness_results)

