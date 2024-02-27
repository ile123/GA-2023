import pandas as pd

def read_exe_file(file_path):
    xlsx = pd.read_excel(file_path)
    data = xlsx['Mjesečni \ntroškovi\n(kn)'].array.tolist()
    return data