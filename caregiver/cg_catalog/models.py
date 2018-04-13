""" 
----------------------------------------------------
Start from here Importing needed libs and components
----------------------------------------------------
"""
# Boilerplate import
from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
# Required for unique book instances
import uuid
"""
---------------------------------------------------- 
Ends here Importing needed libs and components
----------------------------------------------------
"""

""" 
----------------------------------------------------
Start from here classes declaration
----------------------------------------------------
"""

# Declaring class for Cities register
# The idea now is to keep the maximum of simplicity since some few cities in Brazi that we choose will be covered
# Later, maybe, it will be needed to extend and create models for countries, states and then cities
class City(models.Model):
	# Starts from here declaring City data fields
	city_name = models.CharField(max_length=128, help_text="Digite o nome da cidade")
	BR_STATES = (
		('AC', 'Acre'),
		('AL', 'Alagoas'),
		('AM', 'Amazonas'),
		('AP', 'Amapa'),
		('BA', 'Bahia'),
		('CE', 'Ceara'),
		('DF', 'Distrito Federal'),
		('ES', 'Espirito Santo'),
		('GO', 'Goias'),
		('MA', 'Maranhao'),
		('MG', 'Minas Gerais'),
		('MS', 'Mato Grosso do Sul'),
		('MT', 'Mato Grosso'),
		('PA', 'Para'),
		('PB', 'Paraiba'),
		('PE', 'Pernambuco'),
		('PI', 'Piaui'),
		('PR', 'Parana'),
		('RJ', 'Rio de Janeiro'),
		('RN', 'Rio Grande do Norte'),
		('RO', 'Rondonia'),
		('RR', 'Roraima'),
		('RS', 'Rio Grande do Sul'),
		('SC', 'Santa Catarina'),
		('SE', 'Sergipe'),
		('SP', 'Sao Paulo'),
		('TO', 'Tocantins'),
	)
	
	city_state = models.CharField(max_length=2, choices=BR_STATES, blank=True, default='', help_text='Escolha a UF da cidade')
	# Ends City data fields declaration here
	
	# Defines here the visualization order
	class Meta:
		ordering = ["city_state","city_name"]
	
	# Method for returning string representation
	def __str__(self):
		"""
		String for representing the Model object
		"""
		return '{0} ({1} - {2})'.format(self.id, self.city_state, self.city_name)

# Declaring class for the spoken languages by the caregiver professional
# We have only interest in knowing the languages that the professional speaks fluent
class SpokenLanguage(models.Model):
	# Starts from here declaring SpokenLanguage data fields
	language_name = models.CharField(max_length=64, help_text="Digite o nome da lingua falada")
	# Ends SpokenLanguage data fields declaration here
	
	# Defines here the visualization order
	class Meta:
		ordering = ["language_name"]
	
	# Method for returning string representation
	def __str__(self):
		# String for representing the Model object
		return '{0} {1}'.format(self.id, self.language_name)

# Declaring class for representing the certificates that the professional holds
class Certificate(models.Model):
	# Starts from here declaring Certificate data fields
	CERTIF_TYPE = (
		('PCF', 'Certificado Profissional'),
		('CGT', 'Graduacao em Faculdade/Universidade'),
		('MST', 'Mestrado'),
		('DTD', 'Doutorado'),
		('PHD', 'Pos-Doutorado'),
		('MBA', 'MBA - Mestrado Profissional em Negocios'),
		('MSC', 'MSC - Mestrado Profissional em Ciencias'),
		('OCT', 'Outros Tipos de Certificados'),
	)
	
	certificate_level = models.CharField(max_length=3, choices=CERTIF_TYPE, blank=True, default='PCF', help_text='Escolha o tipo/nivel do certificado/diploma')
	certificate_descrip = models.CharField(max_length=128, help_text="Digite o nome/descricao do certificado/diploma")
	certificate_entity = models.CharField(max_length=200, help_text="Digite o nome da entidade certificadora, faculdade ou universidade")
	certificate_year = models.CharField(max_length=4, help_text="Digite o ano em que obteve o certificado/diploma")
	# Ends Certificate data fields declaration here
	
	# Defines here the visualization order
	class Meta:
		ordering = ["certificate_year","certificate_descrip"]
	
	# Method for returning string representation
	def __str__(self):
		# String for representing the Model object
		return '{0} {1} - {2}'.format(self.id, self.certificate_year, self.certificate_descrip)


# Declaring class for representing the CareGiver proffesional
class CareGiver(models.Model):
	# Starts from here declaring CareGiver data fields
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico do profissional cuidador de idosos")
	first_name = models.CharField(max_length=64, help_text="Digite o  primeiro nome do profissional cuidador de idosos")
	last_name =  models.CharField(max_length=64, help_text="Digite o  sobrenome do profissional cuidador de idosos")
	birth_date = models.DateField(null=True, blank=True)
	current_city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, help_text="Escolha a cidade de residencia do cuidador de idosos")
	summary = models.TextField(max_length=1000, help_text='Digite um breve resumo do profissional cuidador de idosos')
	contact_phone = models.CharField(max_length=128, help_text="telefone(s) de contato do profissional cuidador de idosos")
	contact_email = models.EmailField(max_length=128, help_text="e-mail de contato do profissional cuidador de idosos")
	spoken_languages = models.ManyToManyField(SpokenLanguage, help_text='Escolha os idiomas falados fluentemente pelo profissional cuidador de idosos')
	certificates = models.ManyToManyField(Certificate, help_text='Escolha os certificados/diplomas obtidos pelo profissional cuidador de idosos')
	work_dayshift = models.BooleanField(help_text="Disponivel para trabalhar em turno comercial?")
	dayshift_rate = models.DecimalField(decimal_places=2, max_digits=7, help_text="Valor em Reais por turno comercial")
	work_nightshift = models.BooleanField(help_text="Disponivel para trabalhar em turno noturno?")
	nightshift_rate = models.DecimalField(decimal_places=2, max_digits=7, help_text="Valor em Reais por turno noturno")
	work_weekend = models.BooleanField(help_text="Disponivel para trabalhar em dias de final de semana?")
	weekend_rate = models.DecimalField(decimal_places=2, max_digits=7, help_text="Valor em Reais por dia de final de semana trabalhado")
	fullmonth_rate = models.DecimalField(decimal_places=2, max_digits=7, help_text="Valor em Reais por mes cheio/completo de trabalho sem final de semana")
	cook_available = models.BooleanField(help_text="Disponivel para cozinhar/prepara refeicoes?")
	recommendation_name = models.CharField(max_length=128, help_text="Nome de um contato para recomendacao")
	recommendation_phone = models.CharField(max_length=128, help_text="telefone(s) de um contato para recomendacao")
	recommendation_email = models.EmailField(max_length=128, help_text="e-mail de um contato para recomendacao")
	# Ends CareGiver data fields declaration here 
	
	# Defines here the visualization order
	class Meta:
		ordering = ["current_city", "last_name", "first_name"]
	
	# Method for returning string representation
	def __str__(self):
		# String for representing the Model object
		return '{0} {1} {2}, {3}'.format(self.id, self.current_city, self.last_name, self.first_name)
	
	# Returns the url to access a detail record for this book.
	def get_absolute_url(self):
		return reverse('caregiver-detail', args=[str(self.id)])
