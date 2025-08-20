survey_results = [
    ["Python","Js","c++"], #Participant 1
    ["Python","Js","c#"], #Participant 2
    ["Python","Java"],  #participant 3
    ["Python","c++","js"], #Participant 4
    ["Python","Js","c++","java"],   #Participant 5
]
werwchosenall = set.intersection(*map(set, survey_results))
print("Programming languages chosen by all participants:", werwchosenall)

one = set.union(*map(set, survey_results))
print("Programming languages chosen by at least one participant:", one)