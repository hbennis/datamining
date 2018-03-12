import requests
from bs4 import BeautifulSoup

class Appart:

    def __init__(self, url):

        self._url = url
        self._variables = []
        self._values = []
        page = requests.get(url)
        self._soup = BeautifulSoup(page.content, 'html.parser')
        for each in self._soup.find_all('span', class_='List-data'):
            self._variables.append(each.get_text())
        for each in soup.find_all('strong', class_='List-value'):
            self._values.append(each.get_text())

        self.set_postal_code()
        self.set_nb_pieces()
        self.set_etage()
        self.set_mode_chauffage()
        self.set_nature_chauffage()
        self.set_surface_habitable()
        self.set_charges_annuelles()
        self.set_categorie()
        self.set_price(url)

    def get_variables(self, url):
        variables = []
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for each in self._soup.find_all('span', class_='List-data'):
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
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            p = soup.find_all('p', class_='OfferTop-loc')
            self._postal_code = p[0]["data-gtm-zipcode"]
        except:
            self._postal_code = "NA"


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
    def price(self):
        return self._price

    def set_price(self, url):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            p = soup.find_all('p', class_='OfferTop-price')
            self._price = p[0]
        except:
            self._price = "NA"

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