# we have a list the contain a dictionary :
# we need to write a function that allow us to add a dictionary to our list 

visited_countries=[
    {"Country" : "USA",
     "Num_Of_Visites": 4,
     "Cities":["Washington, D.C","New York","California","Texas"]}
     ,
     {"Country" : "United Kingdom",
     "Num_Of_Visites": 4,
     "Cities":["Birmingham","Bradford","Bristol","Cambridge"]}
]
#this is the function dicliration
def add_country(vis_country,num_of_vist,vis_cities):
    n_Country={}
    n_Country["Country"] = vis_country
    n_Country["Num_Of_Visites"] = num_of_vist
    n_Country["Cities"]=vis_cities

    #add to list 
    visited_countries.append(n_Country)
#this is the line that we need to add 
add_country("Russia",4,["Moscow","Kazan","Ufa","Omsk"])
print(visited_countries)