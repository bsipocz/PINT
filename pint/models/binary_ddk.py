from pint import ls,GMsun,Tsun
from .stand_alone_psr_binaries.DDK_model import DDKmodel
from .binary_dd import BinaryDD
from . import parameter as p
from .timing_model import MissingParameter
import astropy.units as u


class BinaryDDK(BinaryDD):
    """This is a PINT pulsar binary ddk model class a subclass of DD model.
    It is a wrapper for independent DDKmodel class defined in
    ./stand_alone_psr_binary/DDK_model.py
    All the detailed calculations are in the independent DDKmodel.
    The aim for this class is to connect the independent binary model with PINT platform
    DDKmodel special parameters:
    KIN inclination angle
    KOM the longitude of the ascending node, Kopeikin (1995) Eq 9. OMEGA
    Reference
    ---------
    KOPEIKIN. 1995, 1996
    """
    register = True
    def __init__(self,):
        super(BinaryDDK, self).__init__()
        self.binary_model_name = 'DDK'
        self.binary_model_class = DDKmodel

        self.add_param(p.floatParameter(name='KIN', value=0.0, units="deg",
                       description="Inclination angle"))
        self.add_param(p.floatParameter(name='KOM', value=0.0, units="deg",
                       description="The longitude of the ascending node"))

        def setup(self):
            """Check out parameters setup.
            """
            super(BinaryDDK,self).setup()
