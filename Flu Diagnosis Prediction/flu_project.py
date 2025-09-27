import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel('flu_diagnosis_dataset.xlsx')
df_scaled=data.copy()

features=['Flu_Positive','Cough']
df_scaled[features]=df_scaled[features].applymap(lambda x: True if x=='Yes' else False)

scaler=StandardScaler()
df_scaled[['Fever']]=scaler.fit_transform(df_scaled[['Fever']])


X=df_scaled[['Fever','Cough']]
y=df_scaled['Flu_Positive']
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2,random_state=42)

model=DecisionTreeClassifier()
model.fit(Xtrain,ytrain)

ypred=model.predict(Xtest)
accuracy=accuracy_score(ytest,ypred)
print('Accuracy : ',accuracy)
print(classification_report(ytest, ypred))

plt.figure(figsize=(12, 8))
plot_tree(model, 
          feature_names=['Fever','Cough'],  # or pass a list of feature names
          class_names=["Negative", "Positive"],  # adjust to your labels
          filled=True, 
          rounded=True, 
          fontsize=10)
plt.show()


cm = confusion_matrix(ytest, ypred)
cm_df = pd.DataFrame(cm, index=["Actual Negative", "Actual Positive"],
                         columns=["Predicted Negative", "Predicted Positive"])

plt.figure(figsize=(6, 4))
sns.heatmap(cm_df, annot=True, fmt='d', cmap='YlGnBu', linewidths=0.5)
plt.title("Confusion Matrix Heatmap")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()

try:
    fever=float(input('Enter your fever in Fahrenheit : '))
    cough=input('Do you have cough (Yes/No) : ').capitalize()

    if cough not in ['Yes','No']:
        raise ValueError('cough input must be in Yes/No')
    
    cough_bool=True if cough=='Yes' else False

    scaled_fever=scaler.transform([[fever]])
    user_input=[[scaled_fever.item(),cough_bool]]
    prediction=model.predict(user_input)

    result='Flu positive' if prediction[0] else 'Flu negative'
    print('Diagnosis : ',result)

except Exception as e:
    print(f'Error occured due to {e}')
