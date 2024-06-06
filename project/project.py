from tabulate import tabulate

def main():
    course_week_schedule()

def course_select():
    """
    Displays the list of courses available, and takes a course as user input and checks if its valid.

    Returns:
    - str: course name if valid

    """
    print("\n\n\n")

    course_list=[

        "CS50x",
        "CS50 AI",
        "CS50 Business",
        "CS50 Cybersecurity",
        "CS50 for Lawyers",
        "CS50 Games",
        "CS50 Python",
        "CS50 Scratch",
        "CS50 SQL",
        "CS50 Technology",
        "CS50 Web"
     ]

    for course in course_list:  # prints the list of courses for user
        print(course)

    selected_course=str(input("\n\nSelect course:   ")).strip().lower() # users input is considered case insensitive

    for course in course_list:
        if course.lower()==selected_course:
            return course
        elif selected_course=="":
            return ""
    else:
        raise TypeError("Selected course not available, please check your input and try again") # TypeError is raised if course not found in list


def week_select():
    """
    Asks for user to input a value of week and checks if input is valid.

    Returns:
    - float: week value if valid

    """

    try:
        week=(input("Enter the week:  "))
        if week!="": # "" input will taken as a sign to end repeated calling of week_select()
            week=float(week)
    except TypeError:
        raise TypeError("Invalid week") # Rejects invalid week values
    if week!="":
        if float(week)<13:
            pass
        else:
            raise ValueError("Week out of range") # rejects week values higher than 12... as no course offers more than 12 weeks content

    return week

def course_week_schedule():
    """
    Prints the table for all courses automatically by default once called,
    Takes inputs with help of course_select() and week_select() and get a track of completed weeks
    Prints the full table again with completed weeks marked ** and percentages of completion

    """

    course_week_dict={
        "CS50x":{0:"Scratch",1:"C",2:"Arrays",3:"Algorithms",4:"Memory",5:"Data Structures",6:"Python",6.5:"Artificial Intelligence",7:"SQL",8:"HTML, CSS, JavaScript",9:"Flask",10:"Cybersecurity"},
        "CS50 AI":{0:"Search",1:"Knowledge",2:"Uncertainty",3:"Optimization",4:"Learning",5:"Neural Networks",6:"Language"},
        "CS50 Business":{0:"Computational thinking",1:"Programming languages ",2:"Internet technologies",3:"Web Development",4:"Technology stacks",5:"Cloud computing"},
        "CS50 Cybersecurity":{0:"Securing Accounts",1:"Securing Data",2:"Securing Systems",3:"Securing Software",4:"Preserving Privacy"},
        "CS50 for Lawyers":{0:"NONE",1:"Computational Thinking",2:"Programming Languages",3:"Algorithms, Data StructuresLoops",4:"Cryptography",5:"Cybersecurity I",6:"Internet Technologies, Cloud Computing",7:"Web Development",8:"Database Design",9:"Cybersecurity II",10:"Challenges at the Intersection of Law and Technology"},
        "CS50 Games":{0:"Pong",1:"Flappy Bird",2:"Breakout",3:"Match 3",4:"Super Mario Bros.",5:"Legend of Zelda",6:"Angry Birds",7:"Pokémon",8:"Helicopter Game 3D",9:"Dreadhalls",10:"Portal",11:"Portal Problems"},
        "CS50 Python":{0:"Introduction",1:"Functions,Variables",2:"Conditionals",3:"Loops",4:"Exceptions",5:"Libraries",6:"Unit Tests",7:"File I/O",8:"Regular Expressions",9:"Object-Oriented Programming",10:"Et Cetera"},
        "CS50 Scratch":{0:"NONE",1:"Sprites",2:"Functions",3:"Events",4:"Values",5:"Conditions",6:"Loops",7:"Variables",8:"Abstraction",9:"Building from Scratch"},
        "CS50 SQL":{0:"Querying",1:"Relating",2:"Designing",3:"Writing",4:"Viewing",5:"Optimizing",6:"Scaling"},
        "CS50 Technology":{0:"NONE",1:"Hardware",2:"Internet",3:"Multimedia",4:"Security",5:"Web Development",6:"Programming"},
        "CS50 Web":{0:"HTML, CSS",1:"Git",2:"Python",3:"Django",4:"SQL, Models, and Migrations",5:"JavaSript",6:"User Interfaces",6:"Testing, CI/CD",7:"Scalability and Security"}
    }

    courses_touched_list=[] # tracks the courses with at least 1 week completed
    percentage_list=[] # tracks percentage for each course in courses_touched_list

    list_tmp=[["COURSE","WEEK","TOPIC"]] # to start table with headers
    # list_tmp holds the values of all course names, week nos and respective topics
    for j in range(len(course_week_dict)):
        for i in range(100):
            try:
                list_tmp.append([list(course_week_dict.keys())[j],list((course_week_dict[list(course_week_dict.keys())[j]]).keys())[i],list((course_week_dict[list(course_week_dict.keys())[j]]).values())[i]])
            except IndexError:
                break

        list_tmp.append(["","",""]) # to create a gap between two courses
        list_tmp.append(["","",""])

        if list(course_week_dict.keys())[j]!="CS50 Web":

            list_tmp.append(["COURSE","WEEK","TOPIC"])

    print(tabulate(list_tmp,tablefmt="grid")) # printing formated table of courses

    while(True):

        course=course_select()
        if course!="":
            list_tmp=[["COURSE","WEEK","TOPIC"],["","",""],*list_tmp]
            print("\n\n\n")
            list_tmp_1=[] #holds values of completed weeks in a selected course

            for i in range(100):
                try:
                    list_tmp_1.append([course,list((course_week_dict[course]).keys())[i],list((course_week_dict[course]).values())[i]])
                except IndexError:
                    break

            list_tmp_1=[["COURSE","WEEK","TOPIC"],["","",""],*list_tmp_1]

            print(tabulate(list_tmp_1,tablefmt="grid"))
            print("\n\n")

            print("Enter the week numbers which you have completed: ")
            week_no_list=[] # stores week nos as a list for each selected course everytime
            while(True):
                week_no=week_select()
                if week_no=="":
                    break
                week_no_list.append(week_no)
            count_of_weeks=0
            for week_no in week_no_list:
                week_no=float(week_no)
                if week_no in list((course_week_dict[course].keys())):
                    if course_week_dict[course][week_no][-2:]!="**": # weeks once completed are not counted again
                        course_week_dict[course][week_no]=course_week_dict[course][week_no]+"**"
                        count_of_weeks+=1 # weeks are counted simultaneously to get perncentage
                else:
                    raise TypeError("invalid week numbers")# raises error for invalid week nos


            list_tmp_2=[] # holds the values of updated table for each course

            for i in range(100):
                try:
                    list_tmp_2.append([course,list((course_week_dict[course]).keys())[i],list((course_week_dict[course]).values())[i]])

                except IndexError:
                    break

            list_tmp_2=[["COURSE","WEEK","TOPIC"],["","",""],*list_tmp_2]
            print(tabulate(list_tmp_2,tablefmt="grid"))
            if list(course_week_dict[course].values())[0]=="NONE": # courses starting with week 1 were given with week 0 as none to fill space
                tot_no_weeks=len(course_week_dict[course])-1
            else:
                tot_no_weeks=len(course_week_dict[course])

            print(f"{(count_of_weeks/tot_no_weeks)*100:.2f} % of {course} completed")
            percentage_list.append(f"{(count_of_weeks/tot_no_weeks)*100:.2f}")
            if (count_of_weeks)>0:
                courses_touched_list.append(course)
        else:
            break
    print("\n\n")
    print("final report:\n")
    list_t=[] # holds values of updated table for all courses
    for j in range(len(course_week_dict)):
        for i in range(100):
            try:
                list_t.append([list(course_week_dict.keys())[j],list((course_week_dict[list(course_week_dict.keys())[j]]).keys())[i],list((course_week_dict[list(course_week_dict.keys())[j]]).values())[i]])
            except IndexError:
                break
        list_t.append(["","",""])
        list_t.append(["","",""])

        if list(course_week_dict.keys())[j]!="CS50 Web":
            list_t.append(["COURSE","WEEK","TOPIC"])
    print(tabulate(list_t,tablefmt="grid"))
    print("\n\n")

    for i in range(len(percentage_list)): # prints the percnetages of completion at end
        print(f"{percentage_list[i]} % of {courses_touched_list[i]} completed")

if __name__=="__main__":
    main()
