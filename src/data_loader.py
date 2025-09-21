import pandas as pd

class animeDataLoader:
    def __init__(self, original_path: str, processed_path: str):
        self.original_path = original_path
        self.processed_path = processed_path
    
    def load_process(self):
        df = pd.read_csv(self.original_path, encoding='utf-8', on_bad_lines='skip').dropna()
        required_cols = ['Name','Genres','sypnopsis']
        missing_cols = set(required_cols) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing columns in the dataset: {missing_cols}")
        df['combined_info']= (
            'Title: ' + df['Name'] + '; ' +
            'Genres: ' + df['Genres'] + '; ' +
            'Synopsis: ' + df['sypnopsis'] + '; '
        )
        df = df[['combined_info']]
        df.to_csv(self.processed_path, index=False, encoding ='utf-8')
        return self.processed_path 
