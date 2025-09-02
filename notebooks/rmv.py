import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium", layout_file="layouts/rmv.grid.json")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Définition de RMV

    ## Définition

    Le **RMV** (Respiratory Minute Volume / Volume de gaz respiré par minute) est la quantité d'air ou de gaz respiré par un plongeur en une minute. Il est exprimé en litres par minute (L/min).

    ## Formule

    $$
    \text{RMV (L/min)} = \frac{ \text{Volume air consommé (L)} }{ \text{Durée plongée (min)} \times \text{Profondeur moyenne (bar)}}
    $$

    où

    - $\text{Volume air consommé (L)} =  \Big(\text{Pression début (bar)} - \text{Pression fin (bar)}\Big) \times  \text{Volume bouteille (L)}$
    - $\text{Profondeur moyenne (bar)} = \text{Profondeur moyenne (m)} / 10 + 1$
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.function
def compute_rmv(cylinder, start, end, time, depth):
    if not (cylinder and start and end and time and depth):
        return 0
    pressure = depth/10 +1 
    return (cylinder * (start - end)) / (time * pressure)


@app.cell
def _(mo):
    # INPUTS
    cylinder_sizes = ["10 L", "12 L", "15 L", "16 L", "20 L", "24 L"]
    cylinder_volume = mo.ui.radio(
        options=cylinder_sizes, inline=True,
        label="Volume bouteille (en litres) : ",
        value="15 L")
    start_pressure = mo.ui.number(label="Pression début plongée (en bars) : ", value=200)
    end_pressure = mo.ui.number(label="Pression fin plongée (en bars) : ", value=50)
    dive_time = mo.ui.number(label="Temps plongée (en minutes) : ",value=45)
    mean_depth = mo.ui.number(label="Profondeur moyenne (en mètres) : ",value=15.5)
    return cylinder_volume, dive_time, end_pressure, mean_depth, start_pressure


@app.cell
def _(
    cylinder_volume,
    dive_time,
    end_pressure,
    mean_depth,
    mo,
    start_pressure,
):
    mo.vstack(
        [
            mo.md("# Calculer son RMV"),
            cylinder_volume,
            mo.hstack([start_pressure, end_pressure],justify="start"),
            mo.hstack([dive_time, mean_depth],justify="start"),
        ],
        align="stretch",
        gap=1,
    )
    return


@app.cell
def _(
    cylinder_volume,
    dive_time,
    end_pressure,
    mean_depth,
    mo,
    start_pressure,
):
    # OUTPUTS

    cylinder_value = int(cylinder_volume.value[:2])
    rmv = compute_rmv(
        cylinder_value,
        start_pressure.value,
        end_pressure.value,
        dive_time.value,
        mean_depth.value)

    mo.md(f"""## RMV = {rmv:.2f} L/min""" if rmv else "")
    return


if __name__ == "__main__":
    app.run()
