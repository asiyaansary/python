import matplotlib.pylot as plt
def plot_profits():
        months=list(range(1,13))
        profits=[]
        print("Enter the profits for each of the 2 months:")
        for i in range(1,13):
                profit=float(input(f"profit for month{i}:"))
                profits.append(profit)
                plt.figure(figsize=(10,5))
                plt.plot(months,profits,marker='0',linestyle='-',color='blue')
                plt.xlabel("Month Number")
                plt.ylabel("Total profit")
                plt.title("monthly profit of company ABC")
                plt.grid(True)
                plt.yticks(months)
                plt.show()
plot_profits()
