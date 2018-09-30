import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt
import pandas as pd

try:
    #Plotting historam stating rewards collected in given range by number of players
    reward = pd.read_csv("player_stats.csv")
    values = reward["Rewards"]
    bins = [0, 100, 100, 200, 300, 400, 500]   #Maximum points can be 500, so divided bins as per that
    plt.figure()
    plt.hist(values, bins, color="olive", rwidth=0.5)
    plt.title("Reward points collected by number of players")
    plt.xlabel("Reward point bins")
    plt.ylabel("No. Of Players")

    # Plotting histogram stating time range taken by number of players
    plt.figure()
    values = reward["Time_Taken"]
    bins = [0, 2, 4, 6, 8, 10] #Total time of game is 10 minutes so bins are divided as per that
    plt.yticks(range(0, 50, 5))
    plt.hist(values, bins, color="cyan", rwidth=0.5)
    plt.title("Completion time by number of players")
    plt.xlabel("Completion time bins ")
    plt.ylabel("No. Of Players")

    #Plotting time series for each player, to see the trend of time taken by player in games he played.
    player_names=reward["Player_Name"].unique();
    for player_name in player_names:
        plt.figure()
        plt.title("TIme taken by Player Name: "+ player_name)
        plt.xlabel("Game number")
        plt.ylabel("Time taken to complete game")
        playerData= reward[reward["Player_Name"]==player_name]["Time_Taken"]
        plt.plot(range(1,playerData.count()+1), playerData,color='m')

    figures = [manager.canvas.figure
               for manager in matplotlib._pylab_helpers.Gcf.get_all_fig_managers()]
    pdf = matplotlib.backends.backend_pdf.PdfPages("Players_Stats_Visualization.pdf")
    for i, figure in enumerate(figures):
        pdf.savefig(figure)
    pdf.close()
    print("Player stats collected are visualized in file 'Players_Stats_Visualization.pdf'")
except Exception:
    print("Error while creating data visualization file, Close 'Players_Stats_Visualization.pdf'")
