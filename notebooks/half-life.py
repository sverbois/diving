import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import math
    return (math,)


@app.cell
def _(math):
    def compute_saturation_in_percent(minutes, halflive):
        return 100.0*(1.0 - math.pow(0.5, minutes/halflive))
    return (compute_saturation_in_percent,)


@app.cell
def _(mo):
    slider_minutes = mo.ui.slider(start=0, stop=50, step=5)
    return (slider_minutes,)


@app.cell
def _(mo, slider_minutes):
    mo.md(f"""Temps de plongée : {slider_minutes.value} minutes {slider_minutes}""")
    return


@app.cell
def _(compute_saturation_in_percent, mo, slider_minutes):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    halflifes = [5, 10, 20, 40]
    compartiments = [str(hl) for hl in halflifes]
    saturation = [compute_saturation_in_percent(slider_minutes.value, hl) for hl in halflifes]
    bar_labels = [5, 10, 20, 40]
    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

    ax.bar(compartiments, saturation, label=bar_labels, color=bar_colors)

    ax.set_xlabel('demi-vie (minutes)')
    ax.set_ylabel('Saturation (%)')
    ax.set_ylim(0,100)
    ax.set_title(f'Saturation des compartiments après {slider_minutes.value} minutes')

    mo.mpl.interactive(plt.gcf())
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
