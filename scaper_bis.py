import requests
from bs4 import BeautifulSoup

class Appart:

    def __init__(self, url):

        self._url = url
        self._variables = []
        self._values = []
        self._page = requests.get(url)
        self._soup = BeautifulSoup(self._page.content, 'html.parser')
        for each in self._soup.find_all('span', class_='List-data'):
            self._variables.append(each.get_text())
        for each in self._soup.find_all('strong', class_='List-value'):
            self._values.append(each.get_text())

        self.set_nb_pieces()
        self.set_etage()
        self.set_mode_chauffage()
        self.set_nature_chauffage()
        self.set_surface_habitable()
        self.set_charges_annuelles()
        self.set_categorie()
        self.set_price()



    @property
    def nb_pieces(self):
        return self._nb_pieces

    def set_nb_pieces(self):
        try:
            ind = self._variables.index('Nombre de pièces')
            self._nb_pieces = self._values[ind]
        except:
            self._nb_pieces = "NA"

    @property
    def price(self):
        return self._price

    def set_price(self):
        try:
            self._price = self._soup.find_all('p', class_='OfferTop-price')[0].get_text()
        except:
            self._price = "NA"

    @property
    def etage(self):
        return self._etage

    def set_etage(self):
        try:
            ind = self._variables.index('Étage')
            self._etage = self._values[ind]
        except:
            self._etage = "NA"

    @property
    def mode_chauffage(self):
        return self._nb_pieces

    def set_mode_chauffage(self):
        try:
            ind = self._variables.index('Mode chauffage')
            self._nb_pieces = self._values[ind]
        except:
            self._nb_pieces = "NA"

    @property
    def nature_chauffage(self):
        return self._nature_chauffage

    def set_nature_chauffage(self):
        try:
            ind = self._variables.index('Nature chauffage')
            self._nature_chauffage = self._values[ind]
        except:
            self._nature_chauffage = "NA"


    @property
    def surface_habitable(self):
        return self._surface_habitable

    def set_surface_habitable(self):
        try:
            ind = self._variables.index('Surface habitable')
            self._surface_habitable = self._values[ind]
        except:
            self._surface_habitable = "NA"

    @property
    def charges_annuelles(self):
        return self._charges_annuelles

    def set_charges_annuelles(self):
        try:
            ind = self._variables.index('Charges annuelles')
            self._charges_annuelles = self._values[ind]
        except:
            self._charges_annuelles = "NA"

    @property
    def categorie(self):
        return self._categorie

    def set_categorie(self):
        try:
            ind = self._variables.index('Catégorie')
            self._categorie = self._values[ind]
        except:
            self._categorie = "NA"