from ai4bharat.transliteration import XlitEngine
import pandas as pd


Names = pd.read_excel("Hospital_Names.xlsx")

e = XlitEngine("te")
# out = e.translit_word("Animal Hospital", topk=5, beam_width=10)
# print(out)

Telugu_Names = []
list = []
i = 0
for i in range(0, len(Names)):
    Telugu_Names.append(e.translit_word(
        Names["Hospital Name"][i], lang_code='te'))
    print(Telugu_Names[i])

# Names['Telugu_name'] = Telugu_Names
T = pd.DataFrame(Telugu_Names)
T.to_csv("Transalted_Names.csv")
