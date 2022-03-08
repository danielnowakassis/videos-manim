from manimlib import *
#1
class Pucpr(Scene):
    def construct(self):

        puc = SVGMobject("Pucpr-logo.svg", height = 6, fill_opacity = 0, color = RED)
        self.play(
            Write(puc), run_time = 5
        )
        puc.generate_target()
        puc.target.scale(0.8)
        puc.target.to_corner(corner = UP)
        self.wait()
        self.play(MoveToTarget(puc))
        boas = Text("Bem vindos à PUC-PR", t2c = {"PUC-PR" : RED})
        boas.move_to([0,-3,0])
        self.play(Write(boas))
        self.wait(5)
        self.play(FadeOut(puc), FadeOut(boas))
#2
class SurfaceExample(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        torus1 = Torus(r1=1, r2=1)
        torus2 = Torus(r1=3, r2=1)
        sphere = Sphere(radius=3, resolution=torus1.resolution)
        # You can texture a surface with up to two images, which will
        # be interpreted as the side towards the light, and away from
        # the light.  These can be either urls, or paths to a local file
        # in whatever you've set as the image directory in
        # the custom_config.yml file

        # day_texture = "EarthTextureMap"
        # night_texture = "NightEarthTextureMap"
        day_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Whole_world_-_land_and_oceans.jpg/1280px-Whole_world_-_land_and_oceans.jpg"
        night_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/The_earth_at_night.jpg/1280px-The_earth_at_night.jpg"

        surfaces = [
            TexturedSurface(surface, day_texture, night_texture)
            for surface in [sphere, torus1, torus2]
        ]

        for mob in surfaces:
            mob.shift(IN)
            mob.mesh = SurfaceMesh(mob)
            mob.mesh.set_stroke(BLUE, 1, opacity=0.5)

        # Set perspective
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        surface = surfaces[0]

        self.play(
            FadeIn(surface),
            ShowCreation(surface.mesh, lag_ratio=0.01, run_time=3),
        )
        for mob in surfaces:
            mob.add(mob.mesh)
        surface.save_state()
        self.play(Rotate(surface, PI / 2), run_time=2)
        for mob in surfaces[1:]:
            mob.rotate(PI / 2)

        self.play(
            Transform(surface, surfaces[1]),
            run_time=3
        )

        self.play(
            Transform(surface, surfaces[2]),
            # Move camera frame during the transition
            frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES),
            run_time=3
        )
        
        self.play(Rotate(surface, 4*PI), run_time=8)
        self.wait(2)
        self.play(FadeOut(surface))
#3
class Lacofor(Scene):
    def construct(self):
        laco = Text("for i in range(0,10,1):", t2c = {"for" : BLUE, " i ": RED, "10": GREEN})
        laco.move_to([-2,2,0])
        self.play(Write(laco))
        imprime = Text("print( i )", t2c = {" i ": RED})
        imprime.move_to([-2.7,1,0])
        self.wait(1)
        self.play(Write(imprime))    
        valor1 = Text("# Valor de i = 0", t2c = {"i" : RED})
        valor1.move_to([-2,3,0])
        self.wait(2)
        self.play(Write(valor1))
        saida = Text("Saida", t2c = {"Saida" : TEAL_E})
        saida.move_to([4,3,0])

        #NUMEROS
        n0 = Text("0")
        n0.move_to([4,2.3,0])
        n1 = Text("1")
        n1.move_to([4,1.8,0])
        n2 = Text("2")
        n2.move_to([4,1.3,0])
        n3 = Text("3")
        n3.move_to([4,0.8,0])
        n4 = Text("4")
        n4.move_to([4,0.3,0])
        n5 = Text("5")
        n5.move_to([4,-0.2,0])
        n6 = Text("6")
        n6.move_to([4,-0.7,0])
        n7 = Text("7")
        n7.move_to([4,-1.2,0])
        n8 = Text("8")
        n8.move_to([4,-1.7,0])
        n9 = Text("9")
        n9.move_to([4,-2.2,0])
        
        valor2 = Text("# Valor de i = 1", t2c = {"i" : RED})
        valor2.move_to([-2,3,0])
        valor3 = Text("# Valor de i = 2", t2c = {"i" : RED})
        valor3.move_to([-2,3,0])
        valor4 = Text("# Valor de i = 3", t2c = {"i" : RED})
        valor4.move_to([-2,3,0])
        valor5 = Text("# Valor de i = 4", t2c = {"i" : RED})
        valor5.move_to([-2,3,0])
        valor6 = Text("# Valor de i = 5", t2c = {"i" : RED})
        valor6.move_to([-2,3,0])
        valor7 = Text("# Valor de i = 6", t2c = {"i" : RED})
        valor7.move_to([-2,3,0])
        valor8 = Text("# Valor de i = 7", t2c = {"i" : RED})
        valor8.move_to([-2,3,0])
        valor9 = Text("# Valor de i = 8", t2c = {"i" : RED})
        valor9.move_to([-2,3,0])
        valor10 = Text("# Valor de i = 9", t2c = {"i" : RED})
        valor10.move_to([-2,3,0])


        self.play(Write(saida))
        self.wait()
        self.play(Write(n0))
        self.play(Transform(valor1, valor2))
        self.play(Write(n1))
        self.play(Transform(valor1, valor3))
        self.play(Write(n2))
        self.play(Transform(valor1, valor4))
        self.play(Write(n3))
        self.play(Transform(valor1, valor5))
        self.play(Write(n4))
        self.play(Transform(valor1, valor6))
        self.play(Write(n5))
        self.play(Transform(valor1, valor7))
        self.play(Write(n6))
        self.play(Transform(valor1, valor8))
        self.play(Write(n7))
        self.play(Transform(valor1, valor9))
        self.play(Write(n8))
        self.play(Transform(valor1, valor10))
        self.play(Write(n9))
#4
class Grafos(Scene):
    def construct(self):
        ponto1 = Dot(color = BLUE_E, radius = 0.5)
        ponto1.move_to([2.5,0,0])

        ponto2 = Dot(color = BLUE_E, radius = 0.5)
        ponto2.move_to([-2.5,0,0])

        self.play(Write(ponto1), Write(ponto2), runtime = 2)
        self.wait(2)

        line1 = Line(np.array([-2,0,0]), np.array([2,0,0]), stroke_width=5, color=WHITE)
        self.play(ShowCreation(line1))
        self.wait(1)

        dot1 = Dot(color = RED_D, radius = 0.2)
        dot1.move_to([-1.7,0,0])
        dot2 = Dot(color = RED_D, radius = 0.2)
        dot2.move_to([1.7,0,0])

        self.play(Write(dot1), Write(dot2))
        self.wait(2)

        grupo1 = VGroup(dot1, dot2, line1, ponto1, ponto2)
        self.play(FadeOut(grupo1))

        self.wait(1)

        ponto1 = Dot(color = BLUE_E, radius = 0.3)
        ponto1.move_to([0,2,0])

        ponto2 = Dot(color = BLUE_E, radius = 0.3)
        ponto2.move_to([-2,0,0])

        ponto3 = Dot(color = BLUE_E, radius = 0.3)
        ponto3.move_to([3,0,0])

        ponto4 = Dot(color = BLUE_E, radius = 0.3)
        ponto4.move_to([1,-2,0])

        ponto5 = Dot(color = BLUE_E, radius = 0.3)
        ponto5.move_to([3,-2,0])

        self.play(Write(ponto1),Write(ponto2), Write(ponto3), Write(ponto4), Write(ponto5))

        line1 = Line(np.array([-1.8,0.2,0]), np.array([-0.2,1.8,0]), stroke_width=3, color=WHITE)
        line2 = Line(np.array([-1.7,0,0]), np.array([2.7,0,0]), stroke_width=3, color=WHITE)
        line3 = Line(np.array([0.2,1.8,0]), np.array([2.8,-1.8,0]), stroke_width=3, color=WHITE)
        line4 = Line(np.array([1.2,-1.8,0]), np.array([2.8,-0.2,0]), stroke_width=3, color=WHITE)
        line5 = Line(np.array([1.3,-2,0]), np.array([2.7,-2,0]), stroke_width=3, color=WHITE)


        self.play(ShowCreation(line1), ShowCreation(line2), ShowCreation(line3),ShowCreation(line4), ShowCreation(line5))

        t2_1 = Tex("2")
        t2_1.move_to([0,2,0])
        t2_2 = Tex("2")
        t2_2.move_to([-2,0,0])
        t2_3 = Tex("2")
        t2_3.move_to([3,0,0])
        t2_4 = Tex("2")
        t2_4.move_to([1,-2,0])
        t2_5 = Tex("2")
        t2_5.move_to([3,-2,0])

        self.play(Write(t2_1), Write(t2_2), Write(t2_3),Write(t2_4),Write(t2_5))
        self.wait(2)
        t10 = Tex("10")
        t10.move_to([-5,0,0])

        self.play(ReplacementTransform(t2_1, t10), ReplacementTransform(t2_2, t10), ReplacementTransform(t2_3, t10), ReplacementTransform(t2_4, t10), Transform(t2_5, t10))
        ttodos = VGroup(t2_1,t2_2, t2_3, t2_4, t2_5)
        pontopreto = Dot(color = BLACK, radius = 0.3)
        pontopreto.move_to([-4,0,0])

        dot1 = Dot(color = BLUE, radius = 0.1)
        dot1.move_to([-1.6,0.4,0])
        dot2 = Dot(color = BLUE, radius = 0.1)
        dot2.move_to([-0.4, 1.6,0])
        self.play(Write(dot1), Write(dot2))

        dot3 = Dot(color = BLUE, radius = 0.1)
        dot3.move_to([-1.5, 0, 0])
        dot4 = Dot(color = BLUE, radius = 0.1)
        dot4.move_to([2.5,0,0])
        self.play(Write(dot3), Write(dot4))

        dot5 = Dot(color = BLUE, radius = 0.1)
        dot5.move_to([0.35, 1.6,0])
        dot6 = Dot(color = BLUE, radius = 0.1)
        dot6.move_to([2.65, -1.6, 0])
        self.play(Write(dot5), Write(dot6))

        dot7 = Dot(color = BLUE, radius = 0.1)
        dot7.move_to([1.3, -1.7,0])
        dot8 = Dot(color = BLUE, radius =0.1)
        dot8.move_to([2.7, -0.3,0])
        self.play(Write(dot7), Write(dot8))

        dot9 = Dot(color = BLUE, radius = 0.1)
        dot9.move_to([1.5,-2,0])
        dot10 = Dot(color = BLUE, radius = 0.1)
        dot10.move_to([2.5,-2,0])
        self.play(Write(dot9), Write(dot10))
        self.wait(1)

        dotswhole = VGroup(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10)
        e10 = Tex("=10", color = BLUE)
        e10.move_to([-4,0,0])
        self.play(ReplacementTransform(dotswhole, pontopreto), ReplacementTransform(pontopreto,e10))

        self.wait(1)

        whole = VGroup(ponto1, ponto2, ponto3, ponto4, ponto5, line1,line2, line3, line4, line5 )
        whole.generate_target()
        whole.target.scale(0.8)
        whole.target.to_edge(RIGHT)

        tampa10 = Dot(color = BLACK, radius = 0.5)
        tampa10.move_to([-5,0,0])
        self.play(Write(tampa10), FadeOut(e10), MoveToTarget(whole))

        formula = Tex('\\sum_{v \\in V}^{} grau(v) = 2|E| ', color = BLUE_E)
        self.play(Write(formula), run_time = 3)
        self.wait(3)
#5
class Pucpr(Scene):
    def construct(self):
        titulo = Text("Oportunidades dentro da PUC", gradient = (BLUE, GREEN), font_size = 40)
        titulo.move_to([0,3.3,0])
        self.play(Write(titulo))
        pibic = Text("Pibic")
        pibiti = Text("Pibiti")
        monitoria = Text("Monitoria")
        ca = Text("Centro Acadêmico")
        gp = Text("Grupo de estudos")
        ada = Text("Apple Developer Academy")
        inter = Text("Internacionalização")
        pibic.move_to([0, 2.3,0])
        pibiti.move_to([0, 1.3,0])
        monitoria.move_to([0, 0.3,0])
        ca.move_to([0, -0.7,0])
        gp.move_to([0, -1.7,0])
        ada.move_to([0,-2.5,0])
        inter.move_to([0,-3.3,0])
        self.play(FadeIn(VGroup(pibic, pibiti, monitoria, ca, gp, ada, inter)))
      
#6
class Linguas(Scene):
    def construct(self):
        titulo = Text("Línguas (minha opinião)", gradient = (BLUE, GREEN), font_size = 40)
        titulo.move_to([0,3.3,0])
        self.play(Write(titulo))
        tp11 = Text("Se tiver tempo:")
        tp12 = Text("Estude inglês até o C1/C2", t2c = {"inglês" : TEAL_E, "C1/C2": TEAL_E})
        tp13 = Text("Começe uma terceira língua")
        tp11.move_to([-2,2.2,0])
        tp12.move_to([1, 1.5,0])
        tp13.move_to([1.2, 0.8,0])
        tp21 = Text("Se não tiver tempo:", t2c= {"não" : RED})
        tp22 = Text("Estude inglês até o B2", t2c = {"inglês" : TEAL_E, "B2": TEAL_E})
        tp23 = Text("Começe uma terceira língua")
        tp21.move_to([-1.4,-1,0])
        tp22.move_to([0.5, -1.7,0])
        tp23.move_to([1.2, -2.4,0])
        self.play(FadeIn(VGroup(tp11, tp12, tp13)))
        self.play(FadeIn(VGroup(tp21, tp22, tp23)))
#7

class CA(Scene):
    def construct(self):
        ca = Text("@cabcc_pucpr", gradient = (BLUE, GREEN))
        self.play(Write(ca), run_time = 2)
        self.wait(4)
#8
class Bomsemestre(Scene):
    def construct(self):
        ano = Text("Bom Semestre", gradient = (BLUE, GREEN))
        ano1 = Text("Bom Semestre", gradient = (RED, ORANGE))
        
        pix = Text("Deposita ai no pix 423.532.214-21", t2c = {"423.532.214-21" : BLUE})
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(Write(ano), run_time = 2)
        self.wait()
        self.play(TransformMatchingShapes(ano, pix, **kw))
        self.wait()
        self.play(TransformMatchingShapes(pix, ano1, **kw))
        self.wait()
        self.play(TransformMatchingShapes(ano1, pix, **kw))
        self.wait()
        self.play(TransformMatchingShapes(pix, ano, **kw))
        self.wait(4)