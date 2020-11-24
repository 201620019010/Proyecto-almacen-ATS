from django import forms
from django import models
from django.forms import ValidationError
from django.forms.fields import RegexField, Select
from django.utils.translation import ugettext_lazy as _
from .co_departments import DEPARTMENT_CHOICES
from django_countries.fields import CountryField
from django_extensions.db.fields import AutoSlugField
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Formulario_Empleado(forms.Form):
    Primer_Nombre = forms.CharField(max_Length=100)
    Segundo_Nombre = forms.CharField(max_Length=100)
    Primer_Apellido = forms.CharField(max_Length=100)
    Segundo_Apellido = forms.CharField(max_Length=100)
    Fecha_De_Nacimiento = models.DateField()
    Pais = CountryField()
    Dirección = forms.CharField(max_Length=100)
    Correo = forms.EmailField()
    Celular = forms.IntegerField()
    Telefono_Fijo = forms.IntegerField()


class CODepartmentSelect(Select):
    """A Select widget that uses a list of Colombian states as its choices."""

    def __init__(self, attrs=None):
        super(CODepartmentSelect, self).__init__(attrs, choices=DEPARTMENT_CHOICES)



class CONITField(RegexField):
    """
    This field validates a NIT (NUmero de IdentificaciOn Tributaria). A
    NIT is of the form XXXXXXXXXX-V. The last digit is a check digit. This
    field can be used for people and companies.

    More info:
    http://es.wikipedia.org/wiki/N%C3%BAmero_de_Identificaci%C3%B3n_Tributaria
    """
    default_error_messages = {
        'invalid': _('Enter a valid NIT in XXXXXXXXXXX-Y or XXXXXXXXXXXY format.'),
        'checksum': _('Invalid NIT.'),
    }

    PRIME_PLACES = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]

    def __init__(self, *args, **kwargs):
        super(CONITField, self).__init__(r'^\d{5,12}-?\d$', *args, **kwargs)

    def clean(self, value):
        """
        Value can be either a string in the format XXXXXXXXXX-Y or
        XXXXXXXXXXY.
        """
        value = super(CONITField, self).clean(value)
        if value in self.empty_values:
            return self.empty_value
        value, cd = self._canon(value)
        if self._calc_cd(value) != cd:
            raise ValidationError(self.error_messages['checksum'])
        return self._format(value, cd)


    def _canon(self, nit):
        nit = nit.replace('-', '')
        return nit[:-1], nit[-1]

    def _calc_cd(self, nit):
        # Calculation code based on:
        # http://es.wikipedia.org/wiki/N%C3%BAmero_de_Identificaci%C3%B3n_Tributaria
        tmp = sum([
            self.PRIME_PLACES[idx] * int(value)
            for idx, value in enumerate(reversed(nit))
        ]) % 11
        if tmp > 1:
            dv = 11 - tmp
        else:
            dv = 0
        return str(dv)

    def _format(self, nit, check_digit):
        return '{0}-{1}'.format(nit, check_digit)


class Departamento(models.Model):
    """
    Departamentos de Colombia
    """
    nombre = models.CharField(_("Nombre del Departamento"), max_length=255)
    codigo_dane = models.CharField(_("Codigo DANE"), max_length=3) # No puede ser entero ya que tienen codigos como 05
    codigo_geonames = models.CharField(_("Codigo GeoNames"), max_length=10, null=True, blank=True)
    slug = AutoSlugField(populate_from='nombre')

    class Meta:
        ordering = ("nombre",)

    def __unicode__(self):
        return self.nombre

class Municipio(models.Model):
    """
    Ciudades de Colombia
    """
    departamento = models.ForeignKey(Departamento, related_name='municipios', verbose_name=_("Departamento"))
    nombre = models.CharField(_("Nombre del Municipio"), max_length=255)
    codigo_dane = models.CharField(_("Codigo DANE"), max_length=3)
    slug = AutoSlugField(populate_from='nombre')

    coords_lat = models.FloatField(null=True, blank=True)
    coords_long = models.FloatField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)

    class Meta:
        ordering = ("nombre",)

    def __unicode__(self):
        return '%s, %s' % ( self.nombre, self.departamento.nombre )

    def save(self, *args, **kwargs):
        if self.coords_lat:
            print self.coords_lat
            point = Point(self.coords_long, self.coords_lat)
            print point
            self.location = point
        super(Municipio, self).save(*args, **kwargs)






