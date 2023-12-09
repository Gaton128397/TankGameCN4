import pygame
import sys

class MedidorPotencia:
		def __init__(self):
				pygame.init()
				self.potencia = 0
				self.tiempo_presionado = 0
				self.tiempo_anterior = 0
				self.presionado = False

		def medir_potencia(self):
				while True:
						tiempo_actual = pygame.time.get_ticks() / 1000.0  # CONVERSIÓN DE SEGUNDOS

						for event in pygame.event.get():
								if event.type == pygame.KEYDOWN:
										if event.key == pygame.K_SPACE:
												self.tiempo_presionado = tiempo_actual
												self.presionado = True
								elif event.type == pygame.KEYUP:
										if event.key == pygame.K_SPACE:
												if tiempo_actual - self.tiempo_presionado >= 5.0:
														self.potencia = 100
												else:
														self.potencia = min((tiempo_actual - self.tiempo_presionado) * 20, 100)

												self.tiempo_anterior = tiempo_actual
												self.presionado = False

						if self.presionado:
								tiempo_presion = tiempo_actual - self.tiempo_presionado
								potencia_actual = min(tiempo_presion * 20, 100)
								print(f'CARGANDO: {potencia_actual:.1f}')

#usar esto para llamar clase
power = MedidorPotencia()
power.medir_potencia()