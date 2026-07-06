from pathlib import Path
import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        print(f"Data loaded successfully — {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return None

def clean_data(df):
    try:
        df['Age'] = df['Age'].fillna(df['Age'].median())
        df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
        df.drop(columns=['Cabin', 'Name', 'Ticket', 'PassengerId'], inplace=True)
        return df
    except Exception as e:
        print(f"Error in cleaning: {e}")
        return None

def feature_engineering(df):
    try:
        df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
        df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
        df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
        df = pd.get_dummies(df, columns=['Embarked'])
        return df
    except Exception as e:
        print(f"Error in feature engineering: {e}")
        return None

def save_cleaned_data(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
    except Exception as e:
        print(f"Error saving data: {e}")

def run_pipeline(path):
    df = load_data(path)
    if df is None:
        return None
    df = clean_data(df)
    if df is None:
        return None
    df = feature_engineering(df)
    return df

if __name__ == "__main__":
    base_path = Path(__file__).resolve().parents[1]
    input_path = base_path / "data" / "titanic.csv"
    output_path = base_path / "data" / "cleaned_titanic.csv"
    
    df = run_pipeline(input_path)
    if df is not None:
        save_cleaned_data(df, output_path)
        print("Pipeline completed!")
        print(df.shape)
        print(df.head())