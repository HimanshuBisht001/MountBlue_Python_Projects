from src.data_loader import load_ipl_data, load_umpire_data, load_matches_data
from src.calculate import calculate_runs, top10_batsman_for_rcb,foreign_umpire_analysis,number_of_matches_played_per_year
from src.plot import plot_team_runs, plot_top10_rcb_batsman, plot_umpire_data, plot_per_season_match
from src.calculate import top10_batsman_for_rcb,calculate_runs,foreign_umpire_analysis,number_of_matches_played_per_year,matches_played_by_team_per_season,matches_won_per_team_per_year


def execute():
    matches_data = load_ipl_data()  # get ipl matches data
    umpires_data = load_umpire_data()  # get umpires data
    ipl_matches_data = load_matches_data()  # load data from matches.csv

    total_runs = calculate_runs(matches_data)
    top10_batsman = top10_batsman_for_rcb(matches_data)
    foregin_umpires = foreign_umpire_analysis(umpires_data,ipl_matches_data)
    per_season_matches = number_of_matches_played_per_year(ipl_matches_data)
    matches_won_per_team_per_year(ipl_matches_data)


    #plot_team_runs(total_runs)
    #plot_top10_rcb_batsman(top10_batsman)
    #plot_umpire_data(foregin_umpires)
    #plot_per_season_match(per_season_matches)
    



if __name__ == "__main__":
    execute()
