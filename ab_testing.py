import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import math


def sum_gamerounds_distribution(subset,title,plotscope):
    ax= subset.groupby("sum_gamerounds")["userid"].count()[:plotscope].plot(grid= True,figsize = (10,7))
    ax.set_title("The number of players of {} group that play 0-{} games rounds during first week".format(title,plotscope))
    plt.show()

def retention_rate(subset,days_of_retention):
    rate = subset[days_of_retention].sum()/subset[days_of_retention].count()*100
    return rate

def t_test(control_group, test_group,variable):
    t, p = stats.ttest_ind(
        control_group[variable].values,
                test_group[variable].values,equal_var=False)
    print("This is t-test result of the {} :\nt_value: {}\np_value: {}".format(variable,t, p))


def standard_error(p_pool,n_a,n_b):
    se = math.sqrt(p_pool*(1-p_pool)*(1/n_a + 1/n_b))
    return se

def estimate_differences(a,b):
    return a-b

def margin_for_error(se,d_min):
    margin = se*1.96
    print("With the confident level 95%, the lower bound of confident interval is {} and the upper bound of confident interval is {}".format(d_min-margin,d_min+margin))



if __name__ == '__main__':
    df = pd.read_csv("cookie_cats.csv")
    # Check missing value
    df.info()
    # # Number of players in each groups
    # count_by_version = df.groupby(["version"]).count()["userid"]
    # count_by_version.reset_index()
    # ax = pd.DataFrame(count_by_version).plot(kind="bar")
    # plt.xticks(rotation=0)
    # plt.show()
    # # Statistic summary of gamerounds
    # print(df.groupby("version")["sum_gamerounds"].describe())
    # count_df = pd.DataFrame(df.groupby("sum_gamerounds")["userid"].count())
    # print(count_df)
    #
    #Subset data by groups
    gate_40= df[df["version"] == "gate_40"]
    gate_30= df[df["version"] == "gate_30"]
    #
    # # Plot distribution of game rounds
    # sum_gamerounds_distribution(df, "all", 100)
    # sum_gamerounds_distribution(df, "all", 10)
    # sum_gamerounds_distribution(gate_30, "gate_30", 100)
    # sum_gamerounds_distribution(gate_40, "gate_40", 100)

    # Calculate retention rate
    # print("General retention rate after 1 day is {:.2f} %".format(retention_rate(df, "retention_1")))
    # print("General retention rate after 7 day is {:.2f} %".format(retention_rate(df, "retention_7")))
    #
    # print("Retention rate by group Day 1")
    # print(retention_rate(df.groupby("version"), "retention_1"))
    # print("Retention rate by group Day 7")
    # print(retention_rate(df.groupby("version"), "retention_7"))
    #
    # T-test
    t_test(gate_30,gate_40,"retention_1")
    t_test(gate_30,gate_40,"retention_7")



    # pool_rate_1_day = retention_rate(df,"retention_1")
    #
    # print(retention_rate(df,"retention_1"))    #
    #
    # t,p = stats.ttest_ind(
    #     gate_30["retention_1"].values,
    #             gate_40["retention_1"].values,
    #             equal_var=False)
    # print("This is t-test result of the retention rate after 1 day :\nt_value: {}\np_value: {}".format(t, p))
    #
    # t, p = stats.ttest_ind(
    #     gate_30["retention_7"].values,
    #     gate_40["retention_7"].values,
    #     equal_var=False)
    # print("This is t-test result of the retention rate after 1 day:\nt_value: {}\np_value: {}".format(t, p))

