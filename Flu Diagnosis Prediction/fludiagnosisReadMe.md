# FLU DIAGNOSIS PROJECT

This project uses a Decision Tree Classifier to predict flu diagnosis based on patient symptoms like fever and cough. It demonstrates a complete machine learning pipeline — from data preprocessing to model training, evaluation, visualization, and user interaction.

# FEATURES

1. Fever: Numeric (Fahrenheit)
2. Cough: Categorical (Yes/No)
3. Flu_Positive: Target label (Yes/No)

# REQUIREMENTS

1. Python
2. Pandas
3. scikit-learn
4. Matplotlib
5. Seaborn

# MODEL PIPELINE

# Data Preprocessing

- Converted categorical values (Yes/No) to boolean
- Scaled Fever using StandardScaler

# Model Training

- Used DecisionTreeClassifier from scikit-learn
- Split data into training and testing sets (80/20)

# Evaluation

- Accuracy score
- Classification report
- Confusion matrix heatmap

# Visualization

- Decision tree plot
- Confusion matrix heatmap

# User Interaction

- CLI-based input for fever and cough
- Real-time prediction output

# RESULTS

1. Model accuracy: [100 %]
2. Visual insights via decision tree and confusion matrix

# HOW TO USE

1. Run the script in a Python environment
2. Enter your fever (in Fahrenheit) and whether you have a cough
3. Get instant flu diagnosis prediction

# Sample CLI Interaction

Enter your fever in Fahrenheit : 101.5
Do you have cough (Yes/No) : Yes
Diagnosis : Flu positive


# VISUALS

1. Decision tree structure for interpretability
2. Confusion matrix heatmap for performance analysis

