projects = {}

x = 1

while 1:
    print("1. Initialize a Project")
    print("2. Close a Project")
    print("3. Project Progress Update")
    print("4. Print a specific Project")
    print("5. Print All Projects")
    print("6. Quit")
    option = int(input("Select an option: "))

    if option ==1:
            managers = []
            tech = []
            team = []
            pid = input("Enter Project ID: ")
            addprojecttitle = input("Project Title: ")
            addmanagers = int(input("How many do you want to enter: "))
            for i in range(0,n):
                managers.append(input("Manager's Name: "))
            addstart_date = input("Start Date: ")
            addend_date = input("End Date: ")
            addsponsor = input("Sponsor: ")
            addbudget = input("Budget: ")
            addtechnologies = int(input("Enter amount of technologies: "))
            for i in range(0,n):
                tech.append(input("Technology Name:"))
            addteammembers = int(input("Enter amount of Team Members: "))
            for i in range(0,n):
                team.append(input("Team Member's Name: "))


            projects.update({pid: {
                "Project_title":addprojecttitle,
                "managers":addmanagers,
                "start_date":addstart_date,
                "end_date":addend_date,
                "sponsor":addsponsor,
                "budget":addbudget,
                "technologies":addtechnologies,
                "teammembers":addteammembers,
            }})

            print(projects)


    elif option == 2:
        pid = input("Enter the Project ID to be deleted: ")
        del projects[pid]
        print("This Project has been deleted:")
