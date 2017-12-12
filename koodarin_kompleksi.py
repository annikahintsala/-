import cmath
import ikkunasto as ik

elementit = {
	"tekstilaatikko": None,
	"tekstikentta": None
}

def tulosta_muutettu_kompleksiluku(napakoordinaatti, kulma):
	"""Tulostaa testirivin annettuun tekstilaatikkoon."""
	ik.kirjoita_tekstilaatikkoon(elementit["tekstilaatikko"], "{luku:.3f} on osoitinmuodossa {napakoordinaatti:.3f} < {kulma:.3f}°".format(luku=elementit["tekstikentta"], napakoordinaatti=napakoordinaatti, kulma=kulma))

def muuta_osoitinmuotoon():
	"""Lukee kompleksiluvun syötekentästä ja muuttaa sen osoitinmuotoon, jossa osoittimen kulma on esitetty asteina.
	Kompleksiluku sekä sen osoitinmuoto tulostetaan käyttöliittymässä olevaan tekstilaatikkoon."""
	elementit["tekstikentta"] = ik.lue_kentan_sisalto(tekstikentta)
	luku = elementit["tekstikentta"]
	luku = complex(" ".join(luku.split()))
	try:
		isinstance(luku, complex)
	except ValueError:
		ik.avaa_viesti_ikkuna("Virhe", "Et antanut kelvollista kompleksilukua!", virhe=False)
		return muuta_osoitinmuotoon
	else:
		napakoordinaatti = cmath.polar(luku[0])
		kulma = cmath.degrees(luku[1])
		return napakoordinaatti, kulma
	tulosta_muutettu_kompleksiluku(napakoordinaatti, kulma)

def main():
	"""Luo käyttöliittymäikkunan, jossa on vasemmalla tekstikenttä otsikoineen,
	kaksi nappia (muunnosnappi ja quit) ja oikealla tekstilaatikko."""
	global tekstilaatikko
	global tekstikentta

	ikkuna = ik.luo_ikkuna("Kompleksilukumuunnin")
	nappikehys = ik.luo_kehys(ikkuna, ik.VASEN)
	tekstirivi = ik.luo_tekstirivi(nappikehys, "Kompleksiluku: ")
	tekstikentta = ik.luo_tekstikentta(nappikehys)
	muutosnappi = ik.luo_nappi(nappikehys, "Muunna", muuta_osoitinmuotoon)
	quitnappi = ik.luo_nappi(nappikehys, "Lopeta", ik.lopeta)
	ylakehys = ik.luo_kehys(ikkuna, ik.VASEN)
	tekstilaatikko = ik.luo_tekstilaatikko(ylakehys, leveys=80, korkeus=20)
	ik.kaynnista()

if __name__ == "__main__":
	main()
