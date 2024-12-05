from collections import defaultdict

# function to calculate runs 
def calculate_runs(matches_reader): 
    # Total runs scored by teams
    total_teams_runs = defaultdict(int)

    for team in matches_reader:
        total_teams_runs[team['batting_team']] += int(team['total_runs'])
    return total_teams_runs

def top10_batsman_for_rcb(matches_reader):
    batsman_runs_dict = defaultdict(int)
    for team in matches_reader:
        if team['batting_team'] == "Royal Challengers Bangalore":
            batsman_runs_dict[team['batsman']] += int(team['total_runs'])
        
        # sort the dict in decending order by values
    batsman_runs_dict = sorted(batsman_runs_dict.items(), key=lambda x: x[1],reverse=True)[:10]
    return batsman_runs_dict


def matches_played_by_team_per_season():
    pass

def foreign_umpire_analysis(umpires_data,ipl_matches_data):
    foreign_ump_dict = {}
    ipl_umpire_country_dict = defaultdict(int)

    # remove indian umpires
    for umpire in umpires_data:
        if umpire['country'] != 'India':
            foreign_ump_dict[umpire['umpire']] = umpire['country']
    

    for matches in ipl_matches_data:
        for umipre in ['umpire1','umpire2','umpire3']:
            ump_name = matches[umipre]
            if ump_name:
                if ump_name in foreign_ump_dict:
                    country = foreign_ump_dict[ump_name]
                    if country in ipl_umpire_country_dict:
                        ipl_umpire_country_dict[country] += 1
                    else:
                        ipl_umpire_country_dict[country] = 1
    return ipl_umpire_country_dict

def number_of_matches_played_per_year(ipl_data):
    # fech number of seasons

    # ipl_seasons = []
    # for season in ipl_data:
    #     if season['season'] not in ipl_seasons:
    #         ipl_seasons.append(season['season'])
    per_season_matches = defaultdict(int)

    for season in ipl_data:
        per_season_matches[season['season']] += 1
    return per_season_matches


def matches_won_per_team_per_year(ipl_matches_data):
    for data in ipl_matches_data:
        pass
        
    

  

        
    
    


            