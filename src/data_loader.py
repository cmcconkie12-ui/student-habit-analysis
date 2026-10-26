from pathlib import Path
import pandas as pd





def get_data_path():
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "college_students_habits_1M.csv"
    return csv_path


def load_the_data(sample_size=None):
    file_path = get_data_path()
    if sample_size:
        df = pd.read_csv(file_path, nrows=sample_size)
    else:
        df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    test_df = load_the_data(sample_size=3)
    print("Shape: ", test_df.shape)