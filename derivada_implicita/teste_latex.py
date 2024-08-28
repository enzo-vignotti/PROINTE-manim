from manim import*

# COMANDOS PARA MOVER O TEXTO
# move_to
# to_edge
# next_to

class primeiraCena(Scene):
    eq1 = MathTex("x^2 + y^2 = 1")
    eq2 = MathTex("\\frac{d^2y}{dx^2} = -\\frac{1}{y^3}")

    def construct(self):
        self.primeiroBloco(self.eq1, self.eq2)
        a = self.segundoBloco()
        self.terceiroBloco(self.eq1, a)

    def primeiroBloco(self, eq1, eq2):
        # TEXTOS
        enunciado1 = Text("Considerando a seguinte equação: ", font_size=30)
        enunciado2 = Text("Utilize a técnica da derivação implicita para mostrar que: ", font_size=30)
        # EQUAÇÕES

        # OBJETOS
        retangulo = Rectangle(
            width=eq2.width + 0.5,  # Adiciona algum espaço extra ao redor do texto
            height=eq2.height + 0.5,
            color=BLUE,
        )

        # POSICIONANDO ELEMENTOS
        enunciado1.to_edge(UP + LEFT)
        enunciado2.to_edge(LEFT)
        eq1.move_to(LEFT * 5 + UP * 2.5)
        eq2.move_to(DOWN * 2)
        retangulo.move_to(eq2.get_center()) # dessa forma, o retangulo estará sempre centralizado com a equção 2

        # ANIMAÇOES
        self.play(Write(enunciado1))
        self.play(Write(eq1))
        self.play(Write(enunciado2))
        self.play(Write(eq2))
        self.play(FadeIn(retangulo))
        self.wait(3)
        self.play(FadeOut(enunciado1, eq1, enunciado2, eq2, retangulo))
        self.wait(1)
    
    def segundoBloco(self):
        # TEXTOS
        texto1 = Text("Calculando a primeira derivada: ", font_size=30)
        # EQUAÇÕES
        eq01 = MathTex("\\frac{d}{dx}\\left(x^2 + y^2 = 1\\right)")
        eq02 = MathTex("\\frac{d}{dx}(x^2) + \\frac{d}{dx}(y^2) = \\frac{d}{dx}(1)")
        eq03 = MathTex("2x + 2y\\frac{dy}{dx} = 0")
        eq04 = MathTex("2y\\frac{dy}{dx} = -2x")
        eq05 = MathTex("\\frac{dy}{dx} = -\\frac{2x}{2y}")
        eq06 = MathTex("\\frac{dy}{dx} = -\\frac{x}{y}")

        # POSICIONANDO ELEMENTOS
        texto1.to_edge(UP + LEFT)

        # ANIMAÇÕE
        self.play(Write(texto1))
        self.wait(2)
        self.play(Write(eq01))
        self.wait(2)
        self.play(Transform(eq01, eq02))
        self.wait(2)
        self.play(Transform(eq01, eq03))
        self.wait(2)
        self.play(Transform(eq01, eq04))
        self.wait(2)
        self.play(Transform(eq01, eq05))
        self.wait(2)
        self.play(Transform(eq01, eq06))
        self.wait(2)
        self.play(eq01.animate.move_to(RIGHT * 5 + UP * 3 ), run_time=2)
        self.play(FadeOut(texto1))
        self.wait(1)
        return eq01

    def terceiroBloco(self, eq1, eq01):
        # TEXTOS
        texto2 = Text("Calculando a segunda derivada: ", font_size=30)
        texto3 = Text("Usando a regra do quociente: ", font_size=30)
        texto4 = Text("De acordo com o enunciado, temos: ", font_size=30)
        texto5 = Text("Como queríamos demonstrar", font_size=30)

        # EQUAÇÕES
        eq07 = MathTex("\\frac{d}{dx}\\left(\\frac{dy}{dx}\\right) = \\frac{d}{dx}\\left(-\\frac{x}{y}\\right)")
        eq08 = MathTex("\\frac{d^2y}{dx^2} = -\\frac{y \\cdot \\frac{d}{dx}(x) - x \\cdot \\frac{d}{dx}(y)}{y^2}")
        eq09 = MathTex("\\frac{d^2y}{dx^2} = -\\frac{y - x \\cdot \\frac{dy}{dx}}{y^2}")
        eq10 = MathTex("\\frac{d^2y}{dx^2} = -\\frac{y - x \\cdot \\left(-\\frac{x}{y}\\right)}{y^2}")
        eq11 = MathTex("\\frac{d^2y}{dx^2} = -\\frac{y + \\frac{x^2}{y}}{y^2}")
        eq12 = MathTex("\\frac{d^2y}{dx^2} = -\\frac{\\frac{y^2}{y} + \\frac{x^2}{y}}{y^2}}")
        eq12 = MathTex("\\frac{d^2y}{dx^2} = -\\frac{\\left(y^2 + x^2\\right)}{y^3}")
        eq13 = MathTex("\\frac{d^2y}{dx^2} = -\\frac{1}{y^3}")

        # OBJETOS
        retangulo2 = Rectangle(
            width =eq13.width + 0.5,
            height=eq13.height + 0.5,
            color=BLUE,
        )

        # POSICIONANDO OS ELEMENTOS
        texto2.to_edge(UP + LEFT)
        texto3.move_to(DOWN * 1)
        texto4.move_to(DOWN * 1)
        texto5.next_to(retangulo2, DOWN * 1)
        retangulo2.move_to(eq07.get_center())

        # ANIMAÇÃO
        self.play(Write(texto2))
        self.wait(2)        
        self.play(Write(eq07))
        self.wait(2)
        self.play(eq07.animate.move_to(UP * 1), run_time=1)
        self.play(Write(texto3))
        self.wait(2)
        self.play(FadeOut(texto3))
        self.wait(1)
        self.play(eq07.animate.move_to(ORIGIN), run_time=1)
        self.play(Transform(eq07, eq08))
        self.wait(2)
        self.play(Transform(eq07, eq09))
        self.wait(2)
        self.play(Transform(eq07, eq10))
        self.wait(2)
        self.play(FadeOut(eq01))
        self.play(Transform(eq07, eq11))
        self.wait(2)
        self.play(Transform(eq07, eq12)) # não está rodando por algum motivo
        self.wait(2)
        self.play(eq07.animate.move_to(UP * 1), run_time=1)
        self.play(Write(texto4))
        self.wait(2)
        eq1.move_to(DOWN * 2)
        self.play(Write(eq1))
        self.wait(2)
        self.play(FadeOut(texto4, eq1))
        self.play(eq07.animate.move_to(ORIGIN), run_time=1)
        self.play(Transform(eq07, eq13))
        self.wait(0.5)
        self.play(FadeIn(retangulo2), run_time=2)
        self.play(Write(texto5))
        self.wait(2)

