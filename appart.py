import requests
from bs4 import BeautifulSoup

class Appart:

    def __init__(self, url):

        variables = []
        values = []
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for each in soup.find_all('span', class_='List-data'):
            variables.append(each.get_text())
        for each in soup.find_all('strong', class_='List-value'):
            values.append(each.get_text())

        self.set_postal_code(url)
        self.set_nb_pieces(variables,values)
        self.set_etage(variables, values)
        self.set_mode_chauffage(variables,values)
        self.set_nature_chauffage(variables,values)
        self.set_surface_habitable(variables,values)
        self.set_charges_annuelles(variables,values)
        self.set_categorie(variables,values)

    def get_variables(self, url):
        variables = []
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for each in soup.find_all('span', class_='List-data'):
            variables.append(each.get_text())
        return variables

    def get_values(self, url):
        values = []
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for each in soup.find_all('strong', class_='List-value'):
            values.append(each.get_text())
        return values

    @property
    def postal_code(self):
        return self._postal_code

    def set_postal_code(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        p = soup.find_all('p', class_='OfferTop-loc')
        self._postal_code = p[0]["data-gtm-zipcode"]

    @property
    def nb_pieces(self):
        return self._nb_pieces

    def set_nb_pieces(self, variables, values):
        try:
            ind = variables.index('Nombre de pièces')
            self._nb_pieces = values[ind]
        except:
            self._nb_pieces = "NA"

    @property
    def etage(self):
        return self._etage

    def set_etage(self, variables, values):
        try:
            ind = variables.index('Étage')
            self._etage = values[ind]
        except:
            self._etage = "NA"

    @property
    def mode_chauffage(self):
        return self._nb_pieces

    def set_mode_chauffage(self, variables, values):
        try:
            ind = variables.index('Mode chauffage')
            self._nb_pieces = values[ind]
        except:
            self._nb_pieces = "NA"

    @property
    def nature_chauffage(self):
        return self._nature_chauffage

    def set_nature_chauffage(self, variables, values):
        try:
            ind = variables.index('Nature chauffage')
            self._nature_chauffage = values[ind]
        except:
            self._nature_chauffage = "NA"


    @property
    def surface_habitable(self):
        return self._surface_habitable

    def set_surface_habitable(self, variables, values):
        try:
            ind = variables.index('Surface habitable')
            self._surface_habitable = values[ind]
        except:
            self._surface_habitable = "NA"

    @property
    def charges_annuelles(self):
        return self._charges_annuelles

    def set_charges_annuelles(self, variables, values):
        try:
            ind = variables.index('Charges annuelles')
            self._charges_annuelles = values[ind]
        except:
            self._charges_annuelles = "NA"

    @property
    def categorie(self):
        return self._categorie

    def set_categorie(self, variables, values):
        try:
            ind = variables.index('Catégorie')
            self._categorie = values[ind]
        except:
            self._categorie = "NA"