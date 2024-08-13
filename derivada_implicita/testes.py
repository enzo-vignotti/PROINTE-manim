from manim import *

class TransformarPartesEspecificas(Scene):
    def construct(self):
        # Cria uma equação inicial
        eq_inicial = MathTex("a^2", "+", "b^2", "=", "c^2")
        
        # Cria a equação transformada
        eq_transformada = MathTex("a^2", "=", "c^2", "-", "b^2")

        # Posiciona a equação inicial no centro da tela
        eq_inicial.move_to(ORIGIN)
        
        # Adiciona a equação inicial à cena
        self.add(eq_inicial)
        
        # Espera 1 segundo
        self.wait(1)
        
        # Anima a transformação da equação inicial na equação transformada
        self.play(TransformMatchingTex(eq_inicial, eq_transformada))
        
        # Espera mais 2 segundos antes de encerrar a cena
        self.wait(2)
