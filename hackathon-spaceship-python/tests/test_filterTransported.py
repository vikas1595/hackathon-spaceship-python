from src.main import *
def test_filterTransported():
    csv_path='./data/train.csv'
    pdf=create_pddf(csv_path)
    #print(pdf.head(10))
    transportedOnly=filterTransported(pdf,True)
    assert transportedOnly['Transported'].drop_duplicates().values==[True]
