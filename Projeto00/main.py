from datetime import date
from datetime import datetime
from Modelos.segurado import segurado
from Modelos.Beneficiario import beneficiario
from Modelos.Beneficiario import TipoBeneficiario
from Modelos.Corretor import corretor
from Modelos.Apolice import apolice
from Modelos.Apolice import TipoApolice
from Modelos.Apolice import StatusApolice


benef = beneficiario("Andrea", "Maciel", date(year=1985, month=2, day=7), "13176165750", "224166583",
                     "Rua Jose Bonifacio", "andrea@artur.com", TipoBeneficiario.CONJUGE)

benef2 = beneficiario("Andre", "Barboza", date(year=2007, month=2, day=7), "13176165750", "224166583",
                      "Rua Jose Bonifacio", "andre@artur.com", TipoBeneficiario.FILHO)

benef3 = beneficiario("Mateus", "Barboza", date(year=2014, month=2, day=7), "13176165750", "224166583",
                      "Rua Jose Bonifacio", "mateus@artur.com", TipoBeneficiario.FILHO)

seg = segurado("Artur", "Barboza", date(year=1986, month=8, day=28), "13176165750", "224166583",
               "Rua Jose Bonifacio", "artur@artur.com", [benef, benef2, benef3])


corret = corretor("Marco", "Freitas", date(year=1986, month=8, day=28), "13176165750", "224166583",
                  "Rua Jose Bonifacio", "artur@artur.com", "141516325")

apl = apolice(123, TipoApolice.VIDA, 100.0, seg, corret, datetime(year=2025, month=4, day=3),
              datetime(year=2023, month=4, day=3, hour=7, minute=30), StatusApolice.ATIVA, 10000.0)


apl.Numero
