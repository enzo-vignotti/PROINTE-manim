from manim import *

class DestacarTextoComRetangulo(Scene):
    def construct(self):
        # Cria o texto
        texto = Text("Texto Destacado")

        # Cria o retângulo ao redor do texto
        retangulo = Rectangle(
            width=texto.width + 0.5,  # Adiciona algum espaço extra ao redor do texto
            height=texto.height + 0.5,
            color=BLUE,
        )
        
        # Posiciona o retângulo e o texto na tela
        retangulo.move_to(texto.get_center())
        texto.move_to(retangulo.get_center())
        
        # Adiciona o texto e o retângulo à cena
        self.add(retangulo, texto)

        # Anima a escrita do texto
        self.play(Write(texto))
        
        self.wait(1)
        
        # Anima o destaque do retângulo
        self.play(retangulo.animate.set_color(YELLOW))
        self.wait(2)
        
        # Opcional: Remove o retângulo e o texto da tela
        self.play(FadeOut(retangulo), FadeOut(texto))
