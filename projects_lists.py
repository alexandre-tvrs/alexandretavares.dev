class Project:
    def __init__(self, name, description, git_url):
        self.name = name
        self.description = description
        self.git_url = git_url
        
def get_projects():
    project_list = [
        Project("ChatTCC", "Creator of a WEB system project to help students and teachers with the final paper process. Developed with Python (Django Rest Framework) and React.", "https://github.com/alexandre-tvrs/backend-tcc"),
        Project("Wrath Of Elements", "Designed and developed a game in Game Maker to help people with math problems. Developed in C# to the ETEC final paper.", "https://github.com/alexandre-tvrs/wrath-of-elements"),
        Project("TargonApp", "Designed and developed a Python application to generate Excel reports with dashboards and filters. Developed with the Pandas, NumPy and Tkinter frameworks.", "https://github.com/alexandre-tvrs/target-generator"),
        Project("[DEVELOPING]Project.ENV", "Designed and developed a Python and React application to configure local (through minikube) or cloud (through API integration) environments. Developed with Python (fastAPI) and React.", "https://github.com/alexandre-tvrs/-api-project.env"),
        Project("[DEVELOPING]KotaroBOT", "Designed and developed a Python bot for Discord whose main function is to import and play music on servers.", "https://github.com/alexandre-tvrs/kotaro-bot"),
        Project("[DEVELOPING]LoLResultPrevision", "Designed and developed a Python application to predict the result of a League of Legends match. Developed with the Pandas, NumPy and Scikit-learn frameworks.", "https://google.com")
    ]
    
    return project_list