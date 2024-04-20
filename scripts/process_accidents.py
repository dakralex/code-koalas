import json
import pandas as pd

def filter_and_map_accidents(input):
    print("Read ", len(input), " accident entries from Germany.")
    input = input.query('ULAND == 11')
    print("Read ", len(input), " accidents from Berlin.")
    input = input.query('IstRad == 1')
    print("Filtered ", len(input), " bicycle-related accidents from Berlin.")

    entries = list()
    for i, line in input.iterrows():
        entry = dict()
        entry['year'] = int(line['UJAHR'])
        entry['month'] = int(line['UMONAT'])
        entry['lng'] = float(str(line['XGCSWGS84']).replace(',', '.'))
        entry['lat'] = float(str(line['YGCSWGS84']).replace(',', '.'))
        entry['severity'] = int(line['UKATEGORIE'])
        entry['type'] = bool(line.get('IstPKW', False)) << 4 | bool(line.get('IstFuss', False)) << 3 | bool(
            line.get('IstKrad', False)) << 2 | bool(line.get('IstGkfz', False)) << 1 | bool(line.get('IstSonstig', False))
        entries.append(entry)

    return entries

def main():
    inputs = []
    for i in range(2018, 2022):
        inputs.append(pd.DataFrame(pd.read_csv("../data/source/Unfallorte" + str(i) + "_LinRef.csv", sep=";", encoding="latin1")))
    input = pd.concat(inputs, axis=0, ignore_index=True)
    entries = filter_and_map_accidents(input)
    with open("../data/processed/accidents.json", "w") as f:
        json.dump(entries, f)


if __name__ == "__main__":
    main()
