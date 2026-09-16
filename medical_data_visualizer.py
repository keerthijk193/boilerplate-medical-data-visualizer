# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# # 1
# df = None

# # 2
# df['overweight'] = None

# # 3


# # 4
# def draw_cat_plot():
#     # 5
#     df_cat = None


#     # 6
#     df_cat = None
    

#     # 7



#     # 8
#     fig = None


#     # 9
#     fig.savefig('catplot.png')
#     return fig


# # 10
# def draw_heat_map():
#     # 11
#     df_heat = None

#     # 12
#     corr = None

#     # 13
#     mask = None



#     # 14
#     fig, ax = None

#     # 15



#     # 16
#     fig.savefig('heatmap.png')
#     return fig
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def draw_cat_plot():
    # 1. Import the data
    df = pd.read_csv("medical_examination.csv")

    # 2. Add overweight column
    df["overweight"] = (
        df["weight"] / ((df["height"] / 100) ** 2) > 25
    ).astype(int)

    # 3. Normalize cholesterol and glucose
    df["cholesterol"] = df["cholesterol"].apply(
        lambda x: 0 if x == 1 else 1
    )

    df["gluc"] = df["gluc"].apply(
        lambda x: 0 if x == 1 else 1
    )

    # 5. Create DataFrame for categorical plot
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=[
            "cholesterol",
            "gluc",
            "smoke",
            "alco",
            "active",
            "overweight",
        ],
    )

    # 6. Group and reformat data
    df_cat = (
        df_cat
        .groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    # 7. Create categorical plot
    fig = sns.catplot(
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        data=df_cat,
        kind="bar",
    )

    # 8. Get the figure
    fig = fig.fig

    # 9. DO NOT MODIFY
    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    # 10. Import the data
    df = pd.read_csv("medical_examination.csv")

    # Add overweight column
    df["overweight"] = (
        df["weight"] / ((df["height"] / 100) ** 2) > 25
    ).astype(int)

    # Normalize cholesterol and glucose
    df["cholesterol"] = df["cholesterol"].apply(
        lambda x: 0 if x == 1 else 1
    )

    df["gluc"] = df["gluc"].apply(
        lambda x: 0 if x == 1 else 1
    )

    # 11. Clean the data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 12. Calculate correlation matrix
    corr = df_heat.corr()

    # 13. Generate mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Plot heat map
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        square=True,
        linewidths=0.5,
        ax=ax,
    )

    # 16. DO NOT MODIFY
    fig.savefig("heatmap.png")
    return fig