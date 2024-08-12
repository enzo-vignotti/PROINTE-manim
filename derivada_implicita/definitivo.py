from manim import*

# COMANDOS PARA MOVER O TEXTO
# move_to
# to_edge
# next_to

class primeiraCena(Scene):
    def construct(self):
        # TEXTOS
        enunciado1 = Text("Considerando a seguinte equação: ", font_size=30)
        enunciado2 = Text("Utilize a técnica da derivação implicita para mostrar que: ", font_size=30)
        
        # EQUAÇÕES
        eq1 = MathTex("x^2 + y^2 = 1")
        eq2 = MathTex("\\frac{d^2y}{dx^2} = -\\frac{1}{y^3}")

        # OBJETOS
        retangulo = Rectangle(
            width=eq2.width + 0.5,  # Adiciona algum espaço extra ao redor do texto
            height=eq2.height + 0.5,
            color=BLUE,
        )

        # POSICIONANDO OS ELEMENTOS
        enunciado1.to_edge(UP + LEFT)
        enunciado2.to_edge(LEFT)

        eq1.move_to(LEFT * 5 + UP * 2.5)
        eq2.move_to(DOWN * 2)
        # retangulo.move_to(DOWN * 2)
        retangulo.move_to(eq2.get_center()) # dessa forma, o retangulo estará sempre centralizado com a equção 2

        # ANIMAÇÃO
        self.play(Write(enunciado1))
        self.play(Write(eq1))
        self.play(Write(enunciado2))
        self.play(Write(eq2))
        self.play(FadeIn(retangulo))
        self.wait(3)
        