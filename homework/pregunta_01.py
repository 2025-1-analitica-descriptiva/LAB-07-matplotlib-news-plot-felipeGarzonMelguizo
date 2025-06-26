import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    El gráfico debe salvarse al archivo `files/plots/news.png`.
    """
    df = pd.read_csv("files/input/news.csv", index_col=0)

    colores = {
        "Television": "grey",
        "Newspaper": "black",
        "Internet": "tab:green",
        "Radio": "red",
    }
    zorders = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }
    line_widths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 3,
        "Radio": 2,
    }

    def plot_endpoints_and_labels(ax, x, y, label, color, zorder, ha):
        ax.scatter(x, y, color=color, zorder=zorder)
        ax.text(
            x + (0.2 if ha == "left" else -0.2),
            y,
            f"{label} {y} %",
            ha=ha,
            va="center",
            color=color,
        )

    fig, ax = plt.subplots(figsize=(10, 6))

    for col in df.columns:
        ax.plot(
            df.index,
            df[col],
            label=col,
            color=colores[col],
            zorder=zorders[col],
            linewidth=line_widths[col],
        )
        # Start point and label
        plot_endpoints_and_labels(
            ax,
            df.index[0],
            df[col].iloc[0],
            col,
            colores[col],
            zorders[col],
            "right",
        )
        # End point and label
        plot_endpoints_and_labels(
            ax,
            df.index[-1],
            df[col].iloc[-1],
            col,
            colores[col],
            zorders[col],
            "left",
        )

    ax.set_title("How people get their news", fontsize=16)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_xticks(df.index)

    os.makedirs("files/plots", exist_ok=True)
    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.close()
