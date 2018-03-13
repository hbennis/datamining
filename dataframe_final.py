import pandas as pd

df_old = pd.read_csv('scrapping_app_test.csv', sep=',')
df_new = pd.read_csv('scrapping_app_test_nb_pieces_nb_chambres.csv', sep=',')

del df_old['nb_piece']
del df_old['nb_chambres']

result = pd.concat([df_old, df_new], axis=1).drop(['taxe_habitation', 'taxe_fonciere', 'taxe_ordure'], axis=1)
result.to_csv("/Users/khairallah/datamining/scrapping_results_final.csv", sep=',')
