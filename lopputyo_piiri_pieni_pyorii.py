import math
import cmath
import ikkunasto as ik
import piiristo as pi
import SchemCanvas as sc

tila = {
    "syote": None,
    "laatikko": None,
    "piiri": None,
    "vastukset": [],
	"kondensaattorit": [],
	"kelat": [],
	"virta": 0,
    "jannite": 0,
    "taajuus": 0,
	"impedanssi": 0
}

SI_kerrannaisyksikot = {
	"y": 10 ** -24,
	"z": 10 ** -21,
	"a": 10 ** -18,
	"f": 10 ** -15,
	"p": 10 ** -12,
	"n": 10 ** -9,
	"u": 10 ** -6,
	"m": 10 ** -3,
	" ": 10 ** 0,
	"k": 10 ** 3 ,
	"M": 10 ** 6,
	"G": 10 ** 9,
	"T": 10 ** 12,
	"P": 10 ** 15,
	"E": 10 ** 18,
	"Z": 10 ** 21,
	"Y":  10 ** 24
}

arvot = {
		"I": None,
		"U": 0,
		"R": None ,
		"C": None,
		"Z_vastus": None,
		"Z_konkka": None,
		"Z_kela": None,
		"f": 0
}

def aseta_jannite():
	""" Pyytää käyttäjältä tarvittavat tiedot piirin virran laskemiseksi.
		Kyselyä toistetaan kunnes tarvittavat tiedot on annettu. Jännite annettama ilman merkintää V,
		mutta voidaan antaa kerrannaisyksikön kanssa, kuten 1p"""
	tila["jannite"] = ik.lue_kentan_sisalto(jannite_kentta)
	jannite = tila["jannite"][0:-1]
	yksikko = tila["jannite"][-1]
	while True:
		try:
			if tila["jannite"] == "0":
				raise(ValueError)
			else:
				pass
			jannite == int(jannite)
		except ValueError:
			ik.avaa_viesti_ikkuna("Virhe", "Et antanut kelvollista jännitettä!", virhe=False)
			return aseta_jannite
	for yksikko in SI_kerrannaisyksikot:
		U = jannite * SI_kerrannaisyksikot.get("yksikko")  #U = jannite
		if False:
			ik.avaa_viesti_ikkuna("Virhe", "Et antanut kelvollista jännitettä!\nVinkki: Anna jännite ilman yksikköä, esim. muodossa 12.0k", virhe=False)
		else:
			pass
	arvot["U"] = U
	pi.piirra_jannitelahde(piirin_piirto_tila, arvot["U"], arvot["f"], v_asetteluvali=2)
	ik.tyhjaa_kentan_sisalto(jannite_kentta)

def aseta_taajuus():
	"""Pyytää käyttäjältä taajuuden. Oltava nollaa suurempi. """
	tila["taajuus"] = ik.lue_kentan_sisalto(taajuus_kentta)
	taajuus = tila["taajuus"][0:-1]
	yksikko = tila["taajuus"][-1]
	while True:
		try:
			if tila["taajuus"] == "0":
				raise(ValueError)
			else:
				pass
		except ValueError:
			ik.avaa_viesti_ikkuna("Virhe", "Et antanut kelvollista taajuutta!\nVinkki: Anna taajuus ilman yksikköä, esim. muodossa 12.0k", virhe=False)
			return aseta_taajuus
	for yksikko in SI_kerrannaisyksikot:
		f = taajuus * SI_kerrannaisyksikot.get("yksikko")  #f = taajuus
		if False:
			ik.avaa_viesti_ikkuna("Virhe", "Et antanut kelvollista taajuutta!\nVinkki: Anna taajuus ilman yksikköä, esim. muodossa 12.0k", virhe=False)
		else:
			pass
	arvot["f"] = f

def lisaa_vastus():
	"""Pyytää annettavan vastuksen tiedot"""
	tila["vastukset"] = ik.lue_kentan_sisalto(vastus_kentta)
	while True:
		try:
			arvo_vastus = tila["vastukset"][0:-1]
		except ValueError:
			ik.avaa_viesti_ikkuna("Virhe", "Et antanut kelvollista arvoa!\nVinkki: Anna arvo ilman yksikköä, esim. muodossa 12.0n", virhe=False)
			return lisaa_vastus
		else:
			if tila["vastukset"] == "0":
				raise(ValueError)
			elif not SI_kerrannaisyksikot.get("yksikko"):
				ik.avaa_viesti_ikkuna("Virhe", "Et antanut kelvollista arvoa!\nVinkki: Anna arvo ilman yksikköä, esim. muodossa 12.0n", virhe=False)
				return lisaa_vastus
	yksikko = tila["vastukset"][-1]
	R = arvo_vastus * SI_kerrannaisyksikot.get("yksikko")
	arvot["R"] = R

def lisaa_kondensaattori():
	"""Pyytää annettavan kondensaattorin tiedot"""
	tila["kondensaattorit"] = ik.lue_kentan_sisalto(kondensaattori_kentta)
	while True:
		try:
			arvo_kondensaattori = tila["kondensaattorit"][0:-1]
		except ValueError:
			ik.avaa_viesti_ikkuna("Virhe", "Et antanut kelvollista arvoa!\nVinkki: Anna arvo ilman yksikköä, esim. muodossa 12.0k", virhe=False)
			return lisaa_kondensaattori
		else:
			if tila["kondensaattorit"] == "0":
				raise(ValueError)
			elif not SI_kerrannaisyksikot.get("yksikko"):
				ik.avaa_viesti_ikkuna("Virhe", "Et antanut kelvollista arvoa!\nVinkki: Anna arvo ilman yksikköä, esim. muodossa 12.0k", virhe=False)
				return lisaa_kondensaattori
	yksikko = tila["kondensaattorit"][-1]
	C = arvo_kondensaattori * SI_kerrannaisyksikot.get("yksikko")
	arvot["C"] = C

def lisaa_kela():
	"""Pyytää annettavan kelan tiedot"""
	tila["kelat"] = ik.lue_kentan_sisalto(kela_kentta)
	while True:
		try:
			arvo_kela = tila["kelat"][0:-1]
		except ValueError:
			ik.avaa_viesti_ikkuna("Virhe", "Et antanut kelvollista arvoa!\nVinkki: Anna arvo ilman yksikköä, esim. muodossa 12.0k", virhe=False)
			return lisaa_kela
		else:
			if tila["kelat"] == "0":
				raise(ValueError)
			elif not SI_kerrannaisyksikot.get("yksikko"):
				ik.avaa_viesti_ikkuna("Virhe", "Et antanut kelvollista arvoa!\nVinkki: Anna arvo ilman yksikköä, esim. muodossa 12.0k", virhe=False)
				return lisaa_kela
	yksikko = tila["kelat"][-1]
	L = arvo_kela * SI_kerrannaisyksikot.get("yksikko")
	arvot["L"] = L

def piirra_piiri():
	vastukset = tila.get["vastukset"]
	kondensaattorit = tila.get["kondensaattorit"]
	kelat = tila.get["kelat"]
	haara = pi.piirra_haara(piirto_alue, (), h_asetteluvali, v_asetteluvali=2, viimeinen=False)
	pi.piirra_piiri(piirto_alue)

def laske_virta():
	arvot.get(["jannite"], ["vastukset"])
	I = U / R
	arvot["I"] = I

def laske_impedanssi_kondensaattori():
	arvot.get(["f"], ["C"])
	Z = 1 / (2 * pi * f * C * 1j)
	arvot["Z_konkka"] = Z

def laske_impedanssi_kela():
	Z = 2 * pi * f * L * 1j
	arvot["Z_kela"] = Z

def laske_impedanssi_vastus():
	arvot.get["R"]
	Z = R
	arvot["Z_vastus"] = Z

def laske_sarja():
	"""Laskee annettujen vastusten kokonaisresistanssin kun ne oletetaan sarjaan kytketyiksi."""
	sarjaan_kytkenta = sum(tila["vastukset"])
	return float(sarjaan_kytkenta)

def laske_rinnan():
	"""Laskee annettujen vastusten kokonaisresistanssin kun ne oletetaan rinnankytketyiksi."""
	rinnan = 0
	for x in tila["vastukset"]:
		rinnan += (1 / x)
	rinnan_kytkenta = 1 / rinnan
	return float(rinnan_kytkenta)

def main():
	global jannite_kentta
	global taajuus_kentta
	global vastus_kentta
	global kela_kentta
	global kondensaattori_kentta

	ikkuna = ik.luo_ikkuna("Ikkuna")
	nappikehys = ik.luo_kehys(ikkuna, ik.VASEN)
	jannite_rivi = ik.luo_tekstirivi(nappikehys, "Aseta jännitteen suuruus:")
	jannite_kentta = ik.luo_tekstikentta(nappikehys)
	taajuus_rivi =  ik.luo_tekstirivi(nappikehys, "Aseta taajuuden suuruus:")
	taajuus_kentta =  ik.luo_tekstikentta(nappikehys)

	vastus_rivi =  ik.luo_tekstirivi(nappikehys, "Aseta vastuksen arvo:")
	vastus_kentta =  ik.luo_tekstikentta(nappikehys)

	kondensaattori_rivi =  ik.luo_tekstirivi(nappikehys, "Aseta kondensaattorin arvo:")
	kondensaattori_kentta =  ik.luo_tekstikentta(nappikehys)

	kela_rivi =  ik.luo_tekstirivi(nappikehys, "Aseta kelan arvo:")
	kela_kentta =  ik.luo_tekstikentta(nappikehys)

	jannite_nappi = ik.luo_nappi(nappikehys, "Aseta jännite", aseta_jannite)
	taajuus_nappi = ik.luo_nappi(nappikehys, "Aseta taajuus", aseta_taajuus)
	vastus_nappi = ik.luo_nappi(nappikehys, "Lisää vastus", lisaa_vastus)
	kondensaattori_nappi = ik.luo_nappi(nappikehys, "Lisää kondensaattori", lisaa_kondensaattori)
	kela_nappi = ik.luo_nappi(nappikehys, "Lisää kela", lisaa_kela)
	piirto_nappi = ik.luo_nappi(nappikehys, "Piirrä piiri", piirra_piiri)
	lopetusnappi = ik.luo_nappi(nappikehys, "Lopeta", ik.lopeta)
	ylakehys = ik.luo_kehys(ikkuna, ik.VASEN)
	tila["laatikko"] = ik.luo_tekstilaatikko(nappikehys, leveys=20, korkeus=60)
	piirto_alue = pi.luo_piiri(ikkuna, leveys=600, korkeus=400, fonttikoko=16)
	ik.kaynnista()

if __name__ == "__main__":
	main()
