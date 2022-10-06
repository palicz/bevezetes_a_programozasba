# coding: utf-8

class Team:
    def __init__(self, name, project, role):
        self.name = name    # Creating and initializing data
        self.project = project
        self.role = role
        print(self) # Output

    def __str__(self):  # Return message (print)
        return f"-- Developer Létrehozva. --\n{self.name} a {self.project}-en dolgozik {self.role} szerepkörben."

    def __eq__(self, secondary_project):      # Two people work on the same project if their project's name match exactly
        return self.project == secondary_project.project

    def sorter(self,secondary_name):    # Avoid duplicates, and avoid pair switch (Example: Peti-Éva, Éva-Peti)
        return self.name < secondary_name.name and self == secondary_name

# List of workers   // EXPANDABLE
worker_list = []

worker_list.append(Team("Ricsi", "SolArch", "Frontend"))
worker_list.append(Team("Angéla", "ZerTeng", "Tesztelő"))
worker_list.append(Team("Peti", "KefERP", "Backend"))
worker_list.append(Team("Éva", "KefERP", "Frontend"))

# Check for 2 people who work on the same project   // Compatible with expandable list.
for workerx in worker_list:
    for workery in worker_list:
        if workerx.sorter(workery):
            print(f"\n{workerx.name} és {workery.name} dolgoznak egy projecten.")