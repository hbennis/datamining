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
        self.set_taxe_fonciere()
        self.set_taxe_ordure()
        self.set_immo_taxe_habitation()
        self.set_surface_carrez()
        self.set_nb_lots()
        self.set_copropriete_en_difficulte()
        self.set_nb_etages()
        self.set_nb_chambres()
        self.set_date_construction()


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

    @property
    def date_construction(self):
        return self._date_construction

    def set_date_construction(self):
        try:
            ind = self._variables.index('Construction')
            self._date_construction = self._values[ind]
        except:
            self._date_construction = "NA"

    @property
    def nb_etages(self):
        return self._nb_etages

    def set_nb_etages(self):
        try:
            ind = self._variables.index("Nombre d'étages")
            self._nb_etages = self._values[ind]
        except:
            self._nb_etages = "NA"
    @property
    def nb_chambres(self):
        return self._nb_etages

    def set_nb_chambres(self):
        try:
            ind = self._variables.index("Nombre de chambres")
            self._nb_chambres = self._values[ind]
        except:
            self._nb_chambres = "NA"

    @property
    def copropriete_en_difficulte(self):
        return self._copropriete_en_difficulte

    def set_copropriete_en_difficulte(self):
        try:
            ind = self._variables.index("Coproprieté en difficulté")
            self._copropriete_en_difficulte = self._values[ind]
        except:
            self._copropriete_en_difficulte = "NA"

    @property
    def nb_lots(self):
        return self._nb_lots

    def set_nb_lots(self):
        try:
            ind = self._variables.index("Nombre de lots")
            self._nb_lots = self._values[ind]
        except:
            self._nb_lots = "NA"

    @property
    def surface_carrez(self):
        return self._surface_carrez

    def set_surface_carrez(self):
        try:
            ind = self._variables.index("Surface Carrez")
            self._surface_carrez = self._values[ind]
        except:
            self._surface_carrez = "NA"

    @property
    def immo_taxe_habitation(self):
        return self._surface_carrez

    def set_immo_taxe_habitation(self):
        try:
            ind = self._variables.index("Taxe habitation")
            self._immo_taxe_habitation = self._values[ind]
        except:
            self._immo_taxe_habitation = "NA"

    @property
    def taxe_ordure(self):
        return self._taxe_ordure

    def set_taxe_ordure(self):
        try:
            ind = self._variables.index("Taxe ordures ménagères")
            self._taxe_ordure = self._values[ind]
        except:
            self._taxe_ordure = "NA"

    @property
    def taxe_fonciere(self):
        return self._taxe_fonciere

    def set_taxe_fonciere(self):
        try:
            ind = self._variables.index("Taxe foncière")
            self._taxe_fonciere = self._values[ind]
        except:
            self._taxe_fonciere = "NA"


