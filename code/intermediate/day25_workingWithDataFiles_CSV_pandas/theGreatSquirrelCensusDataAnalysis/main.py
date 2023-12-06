# Aggregare i dati per Primary Fur Color contando il numero di righe

import pandas

data = pandas.read_csv("./central_park.csv")
groupBy_color = data.groupby("Primary Fur Color", as_index=False)["X"].count()
columns = {
    "X": "Count"
}
groupBy_color = groupBy_color.rename(columns=columns)
groupBy_color.to_csv("new_data.csv")
