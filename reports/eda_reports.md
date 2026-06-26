# EDA Report - Titanic Dataset
## Author
Kunal
## 1. Dataset Overview
- Total Rows: 891
- Total Columns: 12
- Source: Titanic Dataset (real-world passenger data)

## 2. Missing Values Found
| Column | Missing Values |
|--------|---------------|
| Age | 177 |
| Cabin | 687 |
| Embarked | 2 |

## 3. Data Cleaning Steps
- Age: Filled with median value
- Embarked: Filled with mode value
- Cabin: Dropped (77% missing)
- Name, Ticket, PassengerId: Dropped (not useful for analysis)

## 4. Feature Engineering
- FamilySize: SibSp + Parch + 1
- IsAlone: 1 if passenger was alone, 0 if with family
- Sex: Label encoded (male=0, female=1)
- Embarked: One-hot encoded (S, C, Q)

## 5. Key Findings from EDA
- More passengers died than survived
- Female passengers had higher survival rate than males
- Majority of passengers were between age 20-40
- Passengers travelling alone were more common

## 6. Data Quality Assessment
- Dataset had missing values in 3 columns
- No duplicate rows found
- After cleaning, dataset is ready for ML modeling