class DataTransformer:
    @staticmethod
    def replace_abbreviations(df):
        column_mapping = {
            'OD': 'Seg. Odontológica',
            'AMB': 'Seg. Ambulatorial',
        }
        df.columns = [column_mapping.get(col.strip(), col) for col in df.columns]
        return df