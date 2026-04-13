class LLM:
    def __init__(self, name, token_limit):
        self.name = name
        self.token_limit = token_limit
    
    def get_token_limit(self):
        return self.token_limit
    
    def set_token_limit(self, new_token_limit):
        self.token_limit = new_token_limit
    
    def __str__(self):
        return f'LMM(name={self.name}, token_limit={self.token_limit})'


class AICompany:
    def __init__(self, company_name, founding_year, headquarters):
        self.company_name = company_name
        self.founding_year = founding_year
        self.headquarters = headquarters
        self.llms = []

    def get_headquarters(self):
        return self.headquarters
    
    def get_llms(self):
        return self.llms
    
    def set_headquarters(self, new_headquarters):
        self.headquarters = new_headquarters

    def add_llm(self, llm):
        self.llms.append(llm)

    def display_models(self):
        for model in self.llms:
            print(model)

    def __str__(self):
        return f'AICompany(company_name={self.company_name}, founding_year={self.founding_year}, headquarters={self.headquarters})'

#create objects
llm1 = LLM('xp1', 777)
llm2 = LLM('xp2', 888)

#create ai company
company1 = AICompany('Googley', 2026, 'Mankato')


#add to the LLMS company
company1.add_llm(llm1)
company1.add_llm(llm2)

#Display all models (call it)
company1.display_models()