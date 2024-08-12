from manim import *

class DerivacaoImplicita(Scene):
    def construct(self):
        # Passo 1: Apresentar a equação inicial
        eq_inicial = MathTex("x^2 + y^2 = 1")
        self.play(Write(eq_inicial))
        self.wait(2)

        # Passo 2: Derivar a equação implicitamente em relação a x
        derivada_primeira = MathTex("\\frac{d}{dx}\\left(x^2 + y^2 = 1\\right)")
        self.play(Transform(eq_inicial, derivada_primeira))
        self.wait(2)

        # Passo 3: Mostrar a derivada de cada termo
        termo1 = MathTex("\\frac{d}{dx}(x^2) + \\frac{d}{dx}(y^2) = \\frac{d}{dx}(1)")
        self.play(Transform(eq_inicial, termo1))
        self.wait(2)

        # Passo 4: Simplificar cada derivada
        derivada_simplificada = MathTex("2x + 2y\\frac{dy}{dx} = 0")
        self.play(Transform(eq_inicial, derivada_simplificada))
        self.wait(2)

        # Passo 5: Isolar a primeira derivada dy/dx
        isolando_dy_dx = MathTex("\\frac{dy}{dx} = -\\frac{x}{y}")
        self.play(Transform(eq_inicial, isolando_dy_dx))
        self.wait(2)

        # Passo 6: Derivar novamente para encontrar a segunda derivada
        derivada_segunda = MathTex("\\frac{d}{dx}\\left(\\frac{dy}{dx}\\right) = \\frac{d}{dx}\\left(-\\frac{x}{y}\\right)")
        self.play(Transform(eq_inicial, derivada_segunda))
        self.wait(2)

        # Passo 7: Aplicar a regra do quociente na segunda derivada
        regra_quociente = MathTex("\\frac{d^2y}{dx^2} = -\\frac{y \\cdot \\frac{d}{dx}(x) - x \\cdot \\frac{d}{dx}(y)}{y^2}")
        self.play(Transform(eq_inicial, regra_quociente))
        self.wait(2)

        # Passo 8: Simplificar a expressão para obter a segunda derivada
        segunda_derivada_simplificada = MathTex("\\frac{d^2y}{dx^2} = -\\frac{y \\cdot 1 - x \\cdot \\frac{dy}{dx}}{y^2}")
        self.play(Transform(eq_inicial, segunda_derivada_simplificada))
        self.wait(2)

        # Substituir dy/dx por -x/y
        substituindo_dy_dx = MathTex("\\frac{d^2y}{dx^2} = -\\frac{y + \\frac{x^2}{y}}{y^2}")
        self.play(Transform(eq_inicial, substituindo_dy_dx))
        self.wait(2)

        # Simplificar para obter a forma final
        simplificado_final = MathTex("\\frac{d^2y}{dx^2} = -\\frac{1}{y^3}")
        self.play(Transform(eq_inicial, simplificado_final))
        self.wait(2)

        # Finalizar a animação
        self.play(FadeOut(eq_inicial))

