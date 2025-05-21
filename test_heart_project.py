import pandas as pd

df = pd.read_csv(r'C:\ahc\heart_failure_prediction\heart_updated.csv')


def convert_gender(val):
    return 'Male' if val == 'M' else 'Female'

def convert_target(val):
    return 'Yes' if val == 1 else 'No'

def test_gender_conversion():
    assert convert_gender('M') == 'Male'
    assert convert_gender('F') == 'Female'

def test_heart_disease_conversion():
    assert convert_target(1) == 'Yes'
    assert convert_target(0) == 'No'

def test_required_columns_exist():
    required_columns = ['Age', 'Sex', 'ChestPainType', 'HeartDisease']
    for col in required_columns:
        assert col in df.columns

def test_no_nulls_in_important_columns():
    important_columns = ['Age', 'Cholesterol', 'HeartDisease']
    for col in important_columns:
        assert df[col].isnull().sum() == 0

def test_data_types_are_valid():
    assert df['Age'].dtype in ['int64', 'float64']
    assert df['Sex'].dtype == 'object'

def test_age_range_validity():
    assert df['Age'].between(0,90).all()

print("Done")