import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    df.drop(columns=['Cabin', 'Name', 'Ticket', 'PassengerId'], inplace=True)
    return df

def feature_engineering(df):
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df = pd.get_dummies(df, columns=['Embarked'])
    return df

def run_pipeline(path):
    df = load_data(path)
    df = clean_data(df)
    df = feature_engineering(df)
    return df

if __name__ == "__main__":
    df = run_pipeline('C:/Users/Kunal/Desktop/week-2/data/titanic.csv')
    print("Pipeline completed!")
    print(df.shape)
    print(df.head())