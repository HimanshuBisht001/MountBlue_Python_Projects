import matplotlib.pyplot as plt

def plot_team_runs(total_runs):
    #total_runs = dict(total_runs)
    x = list(total_runs.keys())
    y = list(total_runs.values())

    plt.bar(x,y)
    plt.xticks(rotation=90)
    plt.xlabel("Teams")
    plt.ylabel("Total Runs")    
    plt.show()

def plot_top10_rcb_batsman(top10_batsman):
    batsman = [batter[0] for batter in top10_batsman]
    runs = [total_runs[1] for total_runs in top10_batsman]
    plt.bar(batsman,runs)
    plt.xlabel("Batsman")
    plt.ylabel("Runs")
    plt.show()

def plot_umpire_data(foregin_umpires):
    x = list(foregin_umpires.keys())
    y = list(foregin_umpires.values())
    plt.bar(x,y)
    plt.show()

def plot_per_season_match(per_season_matches):
    x = list(per_season_matches.keys())
    y = list(per_season_matches.values())

    plt.bar(x,y)
    plt.show()



