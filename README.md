# GPA Correlation with Various College Student Habits
Analyzes the effect of various habits and factors on a college students' GPA score.


## Description
This project performs a statistical analysis on a CSV file from Kaggle that contains various college student habits as well as GPA information. Each row represents a students scores for each category (habit). 

This program begins by calculating z-scores for students in the following domains: mental health, digital discipline, financial security, physical health, and academic performance. It then uses those z-scores to calculate the correlation (from 0 to 1) that each domain has with the students GPA, and these correlations are plotted in a chart. (Note: for the purposes of this project, GPA is a score out of 2)

This program also produces a scatter plot that compares mental health scores (from 0 to 10) with GPA scores (from 0 to 2).

### Domain Descriptions
- Mental Health: stress, anxiety, depression, motivation, concentration, self discipline
- Digital Discipline: social media hours, gaming hours, netflix hours, screen time, phone unlocks per day
- Financial Security: family income, parental education level, part-time hours, financial stress
- Physical Health: sleep hours, physical activity, junk food frequency, caffeine, late night frequency
- Academic Performance: attendance, assignment completion, midterm score, final score, project score, online courses completed, peer study group, class participation, weekly study sessions, group study hours, study hours

### Pipeline Structure
- src/data_loader.py: Receives the CSV, performs preprocessing
- src/features.py: Separates the various domains, determines z-scores, and then uses the z-scores to calculate correlations
- src/plots.py: Visualizes the data

### Results

![Domain Correlation](outputs/figures/correlations_chart.png)
![Mental Health vs. Gpa](outputs/figures/stress_gpa_scatter_plot.png)


## Getting Started

### Dependencies
The project requires Python and these packages:
`pandas`
`numpy`
`matplotlib`
`pathlib`


### Executing the Program
Run the following commands, in the order listed:
```
python src/features.py
python src/plots.py
```