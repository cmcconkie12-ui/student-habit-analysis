import pandas as pd
from data_loader import load_the_data
from pathlib import Path


def z_score(cols: list[str], df: pd.DataFrame) -> pd.DataFrame:
    "Computes z scores for the columns of features in the dataset"
    return (df[cols] - df[cols].mean()) / df[cols].std()


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Makes the 5-domain z score columns from the data.
    Returns the data frame with the newly created features added to the end.
    """
    df = df.copy()

    mental_health_cols = [
        "stress",
        "anxiety",
        "depression",
        "motivation",
        "concentration",
        "self_discipline"
    ]
    pos_mental_health_cols = [
        "motivation",
        "concentration",
        "self_discipline"
    ]
    neg_mental_health_cols = [
        "stress",
        "anxiety",
        "depression"
    ]


    screen_time_cols = [
        "social_media_hours",
        "gaming_hours",
        "netflix_hours",
        "screen_time",
        "phone_unlocks_per_day"
    ]


    financial_cols = [
        "family_income",
        "parental_education_level",
        "part_time_hours",
        "financial_stress"
    ]
    pos_financial_cols = [
        "family_income",
        "parental_education_level"
    ]
    neg_financial_cols = [
        "part_time_hours",
        "financial_stress"
    ]


    physical_health_cols = [
        "sleep_hours",
        "physical_activity",
        "junk_food_frequency",
        "caffeine_mg",
        "late_night_frequency"
    ]
    pos_physical_health_cols = [
        "sleep_hours",
        "physical_activity"
    ]
    neg_physical_health_cols = [
        "junk_food_frequency",
        "caffeine_mg",
        "late_night_frequency"
    ]


    academic_performance_cols = [
        "attendance",
        "assignment_completion",
        "midterm_score",
        "final_score",
        "project_score",
        "online_courses_completed",
        "peer_study_group",
        "class_participation",
        "weekly_study_sessions",
        "group_study_hours",
        "study_hours"
    ]


    df["mental_health_z"] = z_score(pos_mental_health_cols, df).mean(axis=1) - z_score(neg_mental_health_cols, df).mean(axis=1)
    df["digital_discipline_z"] = -z_score(screen_time_cols, df).mean(axis=1)
    df["financial_security_z"] = z_score(pos_financial_cols, df).mean(axis=1) - z_score(neg_financial_cols, df).mean(axis=1)
    df["physical_health_z"] = z_score(pos_physical_health_cols, df).mean(axis=1) - z_score(neg_physical_health_cols, df).mean(axis=1)
    df["academic_performance_z"] = z_score(academic_performance_cols, df).mean(axis=1)

    return df


z_cols = [
    "academic_performance_z",
    "mental_health_z",
    "financial_security_z",
    "physical_health_z",
    "digital_discipline_z"
]


def calculate_correlations(df, z_cols):
    correlations = (df[z_cols].apply(lambda col: col.corr(df["gpa"])).sort_values())
    return correlations


if __name__ == '__main__':
    initial_df = load_the_data()
    featured_df = create_features(initial_df)
    correlations = calculate_correlations(featured_df, z_cols)
    output_dir = Path(__file__).resolve().parent.parent / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    correlations.to_csv(output_dir / "domain_correlations.csv", header=True)
    print("")
    print("=============== GPA Correlations ===============")
    print(correlations)