from django.db import models

# Create your models here.

class Parentesco(models.Model):
    nombre = models.CharField('Parentesco', max_length=50)

    class Meta:
        verbose_name = 'Parentesco'
        verbose_name_plural = 'Parentescos'

    def __str__(self):
        return self.nombre

class TipoIdentificacion(models.Model):
    nombre = models.CharField('Tipo identificación', max_length=50)

    class Meta:
        verbose_name = 'TipoIdentificacion'
        verbose_name_plural = '-TipoIdentificaciones'

    def __str__(self):
        return self.nombre


class Acompanante(models.Model):
    tipoIdentificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE)
    numIdentificacion = models.CharField('Número identificación', max_length=50)
    nombreP = models.CharField('Primer Nombre', max_length=50)
    nombreS = models.CharField('Segundo Nombre', max_length=50)
    apellidoP = models.CharField('Primer Apellido', max_length=50)
    apellidoS = models.CharField('Segundo Apellido', max_length=50)
    municipioHabitual = models.CharField('Municipio de residencia', max_length=50)
    direccionHabitual = models.CharField('Dirección de residencia', max_length=50)
    telefono = models.CharField('telefono', max_length=50)
    parentesco_id = models.ForeignKey(Parentesco, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Acompañante'
        verbose_name_plural = 'Acompañantes'

    def __str__(self):
        return self.numIdentificacion

class Profesional(models.Model):
    numIdentificacion = models.CharField('Número identificación', max_length=50)
    nombreP = models.CharField('Primer Nombre', max_length=50)
    nombreS = models.CharField('Segundo Nombre', max_length=50)
    apellidoP = models.CharField('Primer Apellido', max_length=50)
    apellidoS = models.CharField('Segundo Apellido', max_length=50)
    telefono = models.CharField('telefono', max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return self.numIdentificacion

class Afiliado(models.Model):
    numCarnet = models.CharField('Número de carné', max_length=50)
    tipoIdentificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE)
    numIdentificacion = models.CharField('Número identificación', max_length=50)
    nombreP = models.CharField('Primer Nombre', max_length=50)
    nombreS = models.CharField('Segundo Nombre', max_length=50)
    apellidoP = models.CharField('Primer Apellido', max_length=50)
    apellidoS = models.CharField('Segundo Apellido', max_length=50)
    genero = models.CharField('genero', max_length=50)
    fechaNacimiento = models.DateField('Fecha de nacimiento', max_length=50)
    telefono = models.CharField('telefono', max_length=50)
    regimen = models.CharField('Régimen', max_length=50)
    municipioHabitual = models.CharField('Municipio de residencia', max_length=50)
    direccionHabitual = models.CharField('Dirección de residencia', max_length=50)
    ipsPrimaria = models.CharField('IPS primaria', max_length=50)
    estado = models.CharField('Estado afiliación', max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Afiliado'
        verbose_name_plural = 'Afiliados'

    def __str__(self):
        return self.numIdentificacion


class Remision_Contraremision(models.Model):
    RemiContId = models.CharField('Id remision', max_length=50)
    Afil_numIdentificacion = models.ForeignKey(Afiliado, on_delete=models.CASCADE)
    Acom_numIdentificacion = models.ForeignKey(Acompanante, on_delete=models.CASCADE)
    Prof_numIdentificacion = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'remision'
        verbose_name_plural = 'remisiones'

    def __str__(self):
        return self.RemiContId