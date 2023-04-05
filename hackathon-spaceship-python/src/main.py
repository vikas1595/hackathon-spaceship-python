import pandas as p
import numpy

def create_pddf(path):
    df=p.read_csv(path)
    return df

def filterTransported(pdf,filterCondition):
    return pdf[pdf['Transported'] ==filterCondition]
if __name__=="__main__":
    #print('hello world')
    csv_path='./data/train.csv'
    pdf=create_pddf(csv_path)
    #print(pdf.head(10))
    transportedOnly=filterTransported(pdf,True)
    print()
    