west1 = {'Team_Name':'Seattle','Win':13,'Lose':3,'Tie':0}
west2 = {'Team_Name':'San Francisco','Win':12,'Lose':4,'Tie':0}
west3 = {'Team_Name':'Arizona','Win':10,'Lose':6,'Tie':0}
west4 = {'Team_Name':'St. Louis','Win':7,'Lose':9,'Tie':0}
north1 = {'Team_Name':'Green Bay','Win':8,'Lose':7,'Tie':1}
north2 = {'Team_Name':'Chicago','Win':8,'Lose':8,'Tie':0}
north3 = {'Team_Name':'Detroit','Win':7,'Lose':9,'Tie':0}
north4 = {'Team_Name':'Minnesota','Win':5,'Lose':10,'Tie':1}
west_teams = [west1,west2,west3,west4]
north_teams = [north1,north2,north3,north4]
print(f"{'NFC West':<15}{'W':<4}{'L':<3}{'T':<3}")
print("-----------------------")
for team in west_teams:
    print(f"{team['Team_Name']:<15}{team['Win']:<4}{team['Lose']:<3}{team['Tie']:<3}")
print('')
print(f"{'NFC North':<15}{'W':<4}{'L':<3}{'T':<3}")
print("-----------------------")
for team in north_teams:
    print(f"{team['Team_Name']:<15}{team['Win']:<3}{team['Lose']:>2}{team['Tie']:>3}")