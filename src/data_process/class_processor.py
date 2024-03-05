import pandas as pd

class Processor:
    def __init__(self, file):
        self.df = pd.read_csv(file, sep=';', encoding='utf-8')
    
    def rename_columns(self):
        new_columns = {
            "First Name": "first_name",
            "Last Name": "last_name",
            "Email": "email",
            "Application Date": "application_date",
            "Country": "country",
            "YOE": "yoe",
            "Seniority": "seniority",
            "Technology": "technology",
            "Code Challenge Score": "code_challenge_score",
            "Technical Interview Score": "technical_interview_score"
        }
        self.df.rename(columns=new_columns, inplace=True)

    def insert_id(self):
        self.df.insert(0, 'id', range(1, len(self.df) + 1))
    
    def update_hired_column(self):
        self.df['hired'] = 0  # Inicializa toda la columna a 0
        for index, row in self.df.iterrows():
            if row['code_challenge_score'] >= 7 and row['technical_interview_score'] >= 7:
                self.df.at[index, 'hired'] = 1
            else:
                self.df.at[index, 'hired'] = 0

    def technology_category(self):
        self.technology_to_category = {
            'DevOps': 'Development',
            'Development - CMS Backend': 'Development',
            'Development - Frontend': 'Development',
            'Development - FullStack': 'Development',
            'Development - Backend': 'Development',
            'Game Development': 'Development',
            'Development - CMS Frontend': 'Development',
            'QA Automation': 'QA and Testing',
            'QA Manual': 'QA and Testing',
            'Data Engineer': 'Data and Analytics',
            'Database Administration': 'Data and Analytics',
            'Business Analytics / Project Management': 'Data and Analytics',
            'Business Intelligence': 'Data and Analytics',
            'Client Success': 'Sales and Marketing',
            'Social Media Community Management': 'Sales and Marketing',
            'Sales': 'Sales and Marketing',
            'Security Compliance': 'Administration and Security',
            'System Administration': 'Administration and Security',
            'Security': 'Administration and Security',
            'Adobe Experience Manager': 'Tech and Creative Specialties',
            'Mulesoft': 'Tech and Creative Specialties',
            'Salesforce': 'Tech and Creative Specialties',
            'Design': 'Tech and Creative Specialties',
            'Technical Writing': 'Tech and Creative Specialties',
        }

        self.df['category_of_technology'] = self.df['technology'].map(self.technology_to_category)



