"""
Chapitre 11.2
"""


import numbers
import copy
import collections
import collections.abc


class Matrix:
	"""
	Matrice numérique stockée en tableau 1D en format rangée-major.

	:param height: La hauteur (nb de rangées)
	:param width: La largeur (nb de colonnes)
	:param data: Si une liste, alors les données elles-mêmes (`data` affectée, pas copiée). Si un nombre, alors la valeur de remplissage
	"""

	def __init__(self, height, width, data = 0.0):
		if not isinstance(height, numbers.Integral) or not isinstance(width, numbers.Integral):
			raise TypeError()
		if height == 0 or width == 0:
			raise ValueError(numbers.Integral)
		self.__height = height
		self.__width = width
		if isinstance(data, list):
			if len(data) != len(self):
				raise ValueError(list)
			self.__data = data
		elif isinstance(data, numbers.Number):
			self.__data = [data for i in range(len(self))]
		else:
			raise TypeError()

	@property
	def height(self):
		return self.__height

	@property
	def width(self):
		return self.__width

	@property
	def data(self):
		return self.__data

	# TODO: Accès à un élément en lecture
	def __getitem__(self, indexes):
		"""
		Indexation rangée-major

		:param indexes: Les index en `tuple` (rangée, colonne)
		"""
		if not isinstance(indexes, tuple):
			raise IndexError()
		if indexes[0] >= self.height or indexes[1] >= self.width:
			raise IndexError()
		# TODO: Retourner la valeur
		return self.__data[indexes[0] * self.__width + indexes[1]]


	# TODO: Affectation à un élément
	def __setitem__(self, indexes, value):
		"""
		Indexation rangée-major

		:param indexes: Les index en `tuple` (rangée, colonne)
		"""
		if not isinstance(indexes, tuple):
			raise IndexError()
		if indexes[0] >= self.height or indexes[1] >= self.width:
			raise IndexError()
		# TODO: L'affectation
		self.__data[indexes[0] * self.__width + indexes[1]] = value

	def __len__(self):
		"""
		Nombre total d'éléments
		"""
		return self.height * self.width

	# TODO: Représentation affichable (conversion pour print)
	def __str__(self):
		# TODO: Chaque rangée est sur une ligne, avec chaque élément séparé d'un espace.
		result = ""
		for i in range(self.__height):
			line = ""
			for j in range(self.__width):
				line += str(self.__data[i * self.__width + j]) + " "
			result += line + "\n"
		return result

	# TODO: Représentation officielle
	def __repr__(self):
		# TODO: une string qui représente une expression pour construire l'objet.
		return f"Matrix {self.__height}, {self.__width}, {self.__data}"

	# TODO: String formatée
	def __format__(self, format_specs):
		# TODO: On veut pouvoir dir comment chaque élément doit être formaté en passant la spécification de formatage qu'on passerait à `format()`
		result = ""
		for i in range(self.__height):
			line = ""
			for j in range(self.__width):
				line += str(self.__data[i * self.__width + j]) + " "
			result += line + "\n"
		return result

	def clone(self):
		return Matrix(self.height, self.width, self.data)

	def copy(self):
		return Matrix(self.height, self.width, copy.deepcopy(self.data))

	def has_same_dimensions(self, other):
		return (self.height, self.width) == (other.height, other.width)

	def __pos__(self):
		return self.copy()

	# TODO: Négation
	def __neg__(self):
		return Matrix(self.__height, self.__width, [-i for i in self.__data])

	# TODO: Addition
	def __add__(self, other):
		if not self.has_same_dimensions(other):
			raise ValueError("Pas les mêmes formats")
		new_data = []
		for i in self.__data:
			for j in other.__data:
				new_data.append(i+j)
		return Matrix(self.__height, self.__width, [new_data])
	
	# TODO: Soustraction
	def __sub__(self, other):
		return self + -other
	
	# TODO: Multiplication matricielle/scalaire
	def __mul__(self, other):
		if isinstance(other, Matrix):
			# TODO: Multiplication matricielle.
			# Rappel de l'algorithme simple pour C = A * B, où A, B sont matrices compatibles (hauteur_A = largeur_B)
			# C = Matrice(hauteur_A, largeur_B)
			result = Matrix(self.__height, other.width)
			# Pour i dans [0, hauteur_C[
			for i in range(result.height):
				# Pour j dans [0, largeur_C[
				for j in range(result.width):
					# Pour k dans [0, largeur_A[
					for k in range(self.width):
						# C(i, j) = A(i, k) * B(k, j)
						result[i, j] = self[i, k] * other[k, j]

			pass
		elif isinstance(other, numbers.Number):
			# TODO: Multiplication scalaire.
			return Matrix(self.__height, self.__width, [other * i for i in self.__data])
		else:
			raise TypeError()

	# TODO: Multiplication scalaire avec le scalaire à gauche

	def __abs__(self):
		return Matrix(self.height, self.width, [abs(e) for e in self.data])

	# TODO: Égalité entre deux matrices

	@classmethod
	def identity(cls, width):
		result = cls(width, width)
		for i in range(width):
			result[i, i] = 1.0
		return result

