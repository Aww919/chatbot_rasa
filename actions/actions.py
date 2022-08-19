# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import random
import linecache

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict

ALLOWED_TEMAS=["universo","estrellas","ciclo vida estrellas","planetas","planetas enanos","satelites naturales","tipos satelites naturales","satelites sistema solar","asteroides","meteoroides","cometas","galaxias","agujeros negros",
               "sistema solar",
               "sol","eclipse solar","viento solar",
               "planetas sistema solar","mercurio","venus","tierra","marte","jupiter","saturno","urano","neptuno",
               "luna","eclipse lunar","luna mareas","caras luna",
                
]


ALLOWED_NIVELES=[ "principiante", "avanzado" ]


class ActionNombre(Action):

    def name(self) -> Text:
        return "action_registrar_nombre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for entidades in tracker.latest_message['entities']:
            if entidades['entity'] == 'nombre':
                nombre_usuario=entidades['value']
                if len(nombre_usuario)>1:
                    return[SlotSet("nombre",nombre_usuario)]
                else:
                    return[SlotSet("nombre","Amig@")]
            else: 
                return[SlotSet("nombre","Amig@")]



class ActionTemaElegido(Action):

    def name(self) -> Text:
        return "action_tema_elegido"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for entidades in tracker.latest_message['entities']:
            if entidades['entity'] == 'tema':
                tema_elegido=entidades['value'].lower()
                if tema_elegido in ALLOWED_TEMAS:
                    dispatcher.utter_message(text=f"Has elegido el tema {tema_elegido}")

                    if tema_elegido == "universo":
                        dispatcher.utter_message(text=f"El Universo es el espacio y el tiempo que abarca todo aquello que existe, es decir, todos los tipos de materias, los planetas, la energía, la luz, las estrellas, los satélites, las galaxias y otros objetos celestes, incluso, las leyes y las constantes físicas que los gobiernan.\n\nLa teoría más popular que explica el origen del Universo es el llamado Big Bang o gran explosión. Esta teoría dice que toda la materia del Universo estaba concentrada en un punto que explotó y la materia salió disparada en todas las direcciones. A partir de este momento, comenzó la expansión del Universo, desde las partículas elementales del principio hasta las galaxias de hoy en día.")
                    elif tema_elegido ==  "estrellas":
                        dispatcher.utter_message(text=f"Las estrellas son astros compuestos principalmente por hidrógeno y helio, que producen luz y calor. Cuando se agrupan estrellas creando una forma, se denomina constelaciones. El color de una estrella está determinado por la temperatura de su superficie, de menor a mayor temperatura: rojo-naranja-amarillo-blanco-azul, es decir, las estrellas rojas son las menos calientes, y las azules son las de mayor temperatura.\n\nAdemás, las estrellas pueden ser de diferentes tamaños, desde enanas blancas hasta hipergigantes. Por ejemplo, el Sol es una estrella enana que presenta un color amarillo (su superficie alcanza unos 5800 K de temperatura).")
                    elif tema_elegido == "ciclo vida estrellas":
                        dispatcher.utter_message(text=f"Las estrellas, al igual que las personas, nacen, crecen y mueren. Cuanto más grande y energética es una estrella, su evolución es mucho más rápida, es decir, agota su combustible en menos tiempo.\nTodas las estrellas nacen de la condensación de las partículas de gas y polvo de las nebulosas, que son unas nubes compuestas principalmente de hidrógeno y helio. A medida que una nube pierde tamaño, se fragmenta en grupos más pequeños. Cada fragmento puede finalmente volverse muy calientes y densos, hasta alcanzar una temperatura de millones de grados, que es cuando entra en la primera fase de vida de una estrella, llamada protoestrella.\nLa etapa final de la vida de una estrella es completamente diferente dependiendo de la masa. Una estrella de masa reducida como el Sol se expande convirtiéndose en una gigante roja. Tras desprenderse de sus capas exteriores, se comprime y forma una enana blanca muy densa. Sin embargo, una estrella masiva puede terminar en una explosión muy violenta denominada supernova, cuando se desvanece queda un núcleo muy denso llamado estrella de neutrones. Si la estrella es extremadamente grande, podría formar una estrella de neutrones ultradensa conocida como agujero negro.")
                    elif tema_elegido == "planetas":
                        dispatcher.utter_message(text=f"Un planeta es un cuerpo celeste sin luz propia que cumple las siguientes condiciones.\n• Gira sobre sí mismo y comúnmente alrededor de una estrella.\n• Tiene suficiente masa para que su gravedad supere las fuerzas asociadas a un sólido rígido de manera que asuma una forma prácticamente esférica en equilibrio hidrostático\n• Es gravitatoriamente dominante en su espacio orbital, es decir, que es capaz de \"limpiar\" su órbita frente a otros elementos.")
                    elif tema_elegido == "planetas enanos":
                        dispatcher.utter_message(text=f"Un planeta enano es un cuerpo celeste que al igual que un planeta normal, orbita alrededor de una estrella y además tiene suficiente masa para que su gravedad supere las fuerzas asociadas a un sólido rígido de manera que asuma una forma casi esférica en equilibrio hidrostático. La diferencia es que no tiene limpia la vecindad de su órbita, es decir, no es gravitatoriamente predominante, por lo que tiene que compartir su espacio orbital con otros cuerpos celestes de similar tamaño. Un ejemplo es Plutón, que desde 2006 es considerado planeta enano.")
                    elif tema_elegido == "satelites naturales":
                        dispatcher.utter_message(text=f"Un satélite natural es todo cuerpo celeste sólido no artificial que orbita alrededor de otro, generalmente más grande. El concepto se refiere a todos aquellos que también reciben el nombre de \“lunas\” y se mueven en torno a los planetas del Sistema Solar, aunque pueden hacerlo alrededor de planetas enanos e incluso otros cuerpos más pequeños como los asteroides.")
                    elif tema_elegido == "tipos satelites naturales":
                        dispatcher.utter_message(text=f"Los satélites naturales pueden ser de dos tipos según sus órbitas:\n-Satélites naturales regulares: Son aquellos que mantienen una órbita más circular, ceñida y ecuatorial alrededor de otro cuerpo y giran en el mismo sentido en el que este gira en torno al Sol. \n-Satélites naturales irregulares: siguen órbitas muy alejadas de sus planetas, inclinadas, a menudo excéntricas y retrógradas, debido a que es posible que no se hayan formado en ellas, sino que pudieron ser “capturados” por la atracción gravitacional o haber sido alguna vez cometas.")
                    elif tema_elegido == "satelites sistema solar":
                        dispatcher.utter_message(text=f"La NASA ha confirmado la existencia de al menos 205 satélites naturales de planetas en el Sistema Solar. Varios que están a la espera de ser oficialmente confirmadas además de satélites de planetas enanos, de asteroides y de otros cuerpos celestes. A continuación se muestra una lista de los satélites de planetas del Sistema Solar:\n• Mercurio: 0\n• Venus: 0\n• Tierra: 1 (Luna)\n• Marte: 2 (Fobos y Deimos)\n• Júpiter: 79 (Ío, Europa, Ganímedes, Calisto, etc)\n• Saturno: 82 (Mimas, Encélado, Tetis, Dione, etc)\n• Urano: 27 (Cordelia, Ofelia, Bianca, Crésida, etc)\n• Neptuno: 14 (Tritón, Nereida, Náyade, Talasa, etc)")
                    elif tema_elegido == "asteroides":
                        dispatcher.utter_message(text=f"Un asteroide es un cuerpo rocoso, de tamaño menor que un planeta y mayor que un meteoroide, que orbita alrededor de una estrella. Los asteroides no son esféricos como los planetas, sino que tienen formas irregulares, por lo que cada asteroide es diferente, no es posible encontrar dos asteroides idénticos. La mayoría están hechos de diferentes tipos de roca, pero algunos contienen arcilla o metal. El gran porcentaje de los asteroides del Sistema solar viven en el cinturón de asteroides (una región entre las órbitas de Marte y Júpiter), pero también se encuentran en otros lugares como en las órbitas de los planetas.",
                                                 image="https://spaceplace.nasa.gov/asteroid-or-meteor/en/asteroid-eros.en.png")
                    elif tema_elegido == "meteoroides":
                        dispatcher.utter_message(text=f"Los meteoroides son fragmentos con un diámetro mínimo de 100 µm y máximo de 50 m, que suele provenir de cometas y asteroides, aunque también pueden ser rocas de satélites o planetas que han sido eyectadas en grandes impactos o simplemente restos de la formación de Sistema Solar. Si un meteoroide se acerca lo suficiente a la Tierra y entra en la atmósfera terrestre, se vaporiza y se convierte en un meteoro, que es un rayo de luz en el cielo, comúnmente llamado estrella fugaz. Sin embargo, hay veces que los meteoroides no se desprenden por completo en la atmósfera y aterrizan en la superficie terrestre, en estos casos se les llama meteoritos.",
                                                 image="https://spaceplace.nasa.gov/asteroid-or-meteor/en/asteroid-meteoroid.en.png")
                    elif tema_elegido == "cometas":
                        dispatcher.utter_message(text=f"Los cometas son astros que orbitan alrededor de una estrella compuestos de hielo y polvo, no de roca como en el caso de un asteroide. Se llaman cometas de período corto cuando provienen del cinturón de Kuiper, tardan menos de 200 años en dar una vuelta al Sol. Por otro lado, hay cometas que viven en la Nube de Oort, denominados cometas de período largo ya que tardan mucho más tiempo en orbitar el Sol.\nLos cometas pueden salir de sus hogares debido a la gravedad de un planeta o estrella, cuando están en el Sistema Solar interior pueden ser observados desde la Tierra. Cuando están en el Cinturón de Kuiper o en la Nube de Oort, suelen ser núcleos congelados de hielo y polvo. Pero cuando un cometa se acerca al Sol, comienza a calentarse, convirtiéndose el hielo en gas creando una enorme nube difusa de gas y polvo alrededor del núcleo llamado coma. La presión de la luz y partículas solares empujan los materiales de la coma lejos del Sol, formándose las dos colas de un cometa: cola de polvo (suavemente curvo) y cola de plasma o gas ionizada (apunta directamente en dirección contraria al Sol).",
                                                 image="https://i.pinimg.com/564x/1f/eb/72/1feb7240cf77bacfbf24415c52dde90f.jpg")
                    elif tema_elegido == "agujeros negros":
                        dispatcher.utter_message(text=f"Un agujero negro es un cuerpo celeste con una fuerza gravitatoria tan fuerte que nada, ni siquiera la luz, puede escapar de él o de su proximidad. En teoría un agujero negro se origina cuando una estrella masiva se muere y se contrae más allá de un límite determinado, conocido como radio de Schwarzschild y se hace más pequeña y más densa que una estrella de neutrones. Una vez formados, los agujeros negros crecen por la acumulación de la materia y energía que atrapan.\nLos agujeros negros tienen una frontera esférica llamada horizonte de eventos o de sucesos que actúa como una membrana de un solo sentido, donde las partículas y la radiación pueden entrar, pero no se pueden regresar.",
                                                 image="https://ichef.bbci.co.uk/news/800/cpsprodpb/540D/production/_106371512_small.jpg")
                    
                    elif tema_elegido == "sistema solar":
                        dispatcher.utter_message(text=f"El Sistema Solar es un sistema de la Vía Láctea que está formado por una estrella central (el Sol), 8 planetas que giran a su alrededor (Mercurio, Venus, la Tierra, Marte, Júpiter, Saturno, Urano y Neptuno), planetas enanos (como Plutón, que hasta 2006 era considerado un planeta), satélites que orbitan alrededor de algunos planetas y otros cuerpos celestes como meteoros, asteroides, cometas, etc.")
                    elif tema_elegido == "sol":
                        dispatcher.utter_message(text=f"El Sol es una estrella, es el centro del Sistema Solar, los demás cuerpos orbitan a su alrededor. Es la fuente más importante de luz, energía y calor que tenemos y es imprescindible para la vida en la Tierra.")
                    elif tema_elegido == "eclipse solar":
                        dispatcher.utter_message(text=f"Un eclipse solar se produce cuando la Luna se interpone en el camino de la luz del Sol y proyecta su sombra sobre la Tierra, únicamente puede ocurrir en la fase de luna nueva. Existen varios tipos de eclipse solar: parcial, anular y total. Se dice que es un eclipse parcial cuando la Luna no oculta la luz solar por completo, de modo que desde la Tierra se puede ver una media Luna brillante. Un eclipse solar total se da cuando la Luna cubre el Sol por completo. Sin embargo, si la Luna está un poco más lejos y/o el Sol está un poco más cerca, puede darse un eclipse solar anular, en este caso el tamaño aparente de la Luna no es suficiente para ocultar toda la luz solar, quedando un anillo de luz alrededor de ella.",
                                                 image = "https://upload.wikimedia.org/wikipedia/commons/0/03/Eclipses_Solares.png")
                    elif tema_elegido == "viento solar":
                        dispatcher.utter_message(text=f"El viento solar es una corriente de partículas energéticas liberadas desde la atmósfera superior del Sol (corona solar) que se calienta hasta un punto que la gravedad del Sol no puede retenerla. Su composición es idéntica a la de la corona solar: un 73% de hidrógeno, un 25% de helio y otros elementos. Cuando el viento solar se acerca a un planeta que tiene un campo magnético bien desarrollado (como la Tierra, Júpiter y Saturno),  las partículas son desviadas por la fuerza de Lorentz. Sin embargo, los planetas que tienen una magnetosfera débil o inexistente, están sujetos al agotamiento de su atmósfera por el viento solar. Un ejemplo es Marte, que se piensa que el viento solar ha destruido hasta un tercio de su atmósfera original. En el caso de la Tierra, la magnetosfera hace de escudo frente al viento solar, impidiendo el paso de gran parte de las partículas. Cuando las partículas cargadas impactan con la magnetosfera, se desplazan y se almacenan en ella, cuando esta energía se hace imposible de almacenar se dispara como radiación magnética, provocando unos efectos luminosos llamados auroras polares.")
                    elif tema_elegido == "luna":
                        dispatcher.utter_message(text=f"La Luna es el único satélite que orbita alrededor de la Tierra y tarda 28 días en dar una vuelta completa a la tierra. Sus movimientos de rotación y traslación están sincronizados, por tanto desde la Tierra siempre vemos la misma cara de la Luna. Sin embargo, la Luna nos muestra aspectos diferentes dependiendo de cómo inciden los rayos del Sol en su superficie. Tiene 4 fases principales: luna nueva, cuarto creciente, luna llena y cuarto menguante.")
                    elif tema_elegido == "eclipse lunar":
                        dispatcher.utter_message(text=f"Un eclipse lunar es un fenómeno que ocurre cuando la Tierra se interpone entre el Sol y la Luna, de manera que impide la llegada de toda o parte de la luz solar a la Luna. Esto significa que la Luna llena se desvanece porque la sombra de la Tierra la cubre. Existen 3 tipos de eclipses lunares: penumbrales, parciales y totales. Se dice que es eclipse penumbral cuando la Luna pasa por el cono de penumbra de la Tierra (sombra exterior), por lo que se bloquea parte de los rayos solares pero no todos, este fenómeno es sutil y difícil de observar. El eclipse parcial se da cuando una parte de la Luna pasa a la sombra interior de la Tierra. Cuando la Tierra bloquea toda la luz del Sol se denomina eclipse lunar total, en este caso la Luna presenta un color rojizo.",
                                                 image="https://cimanorte.com/wp-content/uploads/Sin-ti%CC%81tulo-22.jpg")
                    elif tema_elegido == "luna mareas":
                        dispatcher.utter_message(text=f"Las mareas son movimientos periódicos y alternativos de ascenso y descenso de las aguas de mares y océanos. Estas oscilaciones son originadas por la atracción gravitacional del Sol y de la Luna, que atraen hacia sí el agua de mares y océanos modificando el nivel de estos. A pesar de que la fuerza de atracción del Sol sea mayor, su influencia en las mareas es menor porque se encuentra más lejos de la Tierra. Debido a la cercanía de la Luna, su vínculo con las mareas es mucho más fuerte. Según la altura que llega a alcanzar el agua del mar, las mareas pueden ser de 2 tipos: pleamar o marea alta (momento en que la altura del mar llegue a su nivel más alto) y bajamar o marea baja (cuando la altura del mar llega a su nivel más bajo). También se pueden clasificar según las fases de la Luna: se habla de mareas vivas cuando tenemos Luna Llena y Luna Nueva (mayor amplitud por la alineación del Sol y la Luna), y mareas muertas cuando la Luna está en fase de cuarto menguante y cuarto creciente (menor amplitud porque el Sol y la Luna se encuentran en una posición de manera que se compensan las fuerzas de atracción). También podríamos diferenciar mareas lunares y mareas solares en función de si son provocadas en mayor medida por la Luna o el Sol.")
                    elif tema_elegido == "caras luna":
                        dispatcher.utter_message(text=f"Desde la Tierra sólo vemos una cara de la Luna porque su período de rotación es igual al de traslación. La cara visible de la Luna está cubierta de mares lunares, que son como grandes manchas oscuras resultantes de la antigua lava que generó la actividad volcánica en la superficie. Sin embargo, en la cara oculta, estos mares son muy escasos, esta cara está repleta de cráteres y tierras montañosas. ¿Por qué son tan distintas las dos caras de la Luna? Los científicos creen que puede ser debido a un impacto gigante hace miles de millones de años cerca del polo sur de la Luna, que creó una enorme cantidad de calor que hizo que ciertos elementos químicos se depositaran en la cara vista de la luna allanándola con respecto a lo craterosa que es su cara oculta.",
                                                 image="https://cflvdg.avoz.es/sc/bJnOz7dXzpegCkK4k6gQLkumWX8=/768x/2019/01/07/00121546893092370686588/Foto/luna2.jpg")
                    elif tema_elegido == "planetas sistema solar":
                        dispatcher.utter_message(text=f"En este bloque podrás obtener información sobre todos los planetas del Sistema Solar.")
                    elif tema_elegido == "mercurio":
                        dispatcher.utter_message(text=f"Mercurio es el planeta más pequeño del Sistema Solar y el más cercano al Sol. No tiene una atmósfera considerable porque su gravedad no es suficiente para retener los gases a su alrededor y crear una atmósfera. Por tanto, como está desprotegido tiene una superficie sólida que está cubierta de cráteres de impacto.\n• Radio: 2439,7 km\n• Número de satélites naturales: 0\n• Rotación: 58,65 días\n• Traslación: 88 días",
                                                 image="https://ichef.bbci.co.uk/news/640/cpsprodpb/CCBE/production/_109141425_e3a7fc73-ae9e-4118-8a99-dfa6d6b5c9e1.jpg")
                    elif tema_elegido == "venus":
                        dispatcher.utter_message(text=f"Venus no es el planeta más cercano al Sol, pero es el más caliente del Sistema Solar, con una temperatura máxima superior a los 450ºC. Su atmósfera es muy densa, compuesta por gases tóxicos (90-95% dióxido de carbono) que retienen muy bien el calor. Una curiosidad de Venus es que rota en sentido opuesto al resto de los planetas internos, además es el único planeta del sistema solar que su día dura más que su año.\n• Radio: 6051,8 km\n• Número de satélites naturales: 0\n• Rotación: 243 días\n• Traslación: 224,7 días",
                                                 image="https://www.meteorologiaenred.com/wp-content/uploads/2018/08/Planeta-Venus.jpg")
                    elif tema_elegido == "tierra":
                        dispatcher.utter_message(text=f"La Tierra es un planeta rocoso con una superficie sólida y dinámica de montañas, cañones, llanuras y más. La mayor parte de nuestro planeta está cubierto de agua (70%). Nuestra atmósfera tiene el grosor adecuado para mantener el planeta caliente y a una temperatura adecuada para los seres vivos como nosotros, está compuesta principalmente por nitrógeno (78%), oxígeno (21%) y otros gases en menor porcentaje como argón y dióxido de carbono. Es el único planeta de nuestro sistema solar que conocemos que alberga vida.\n• Radio: 6371 km\n• Número de satélites naturales: 1\n• Rotación:24 horas (23 horas y 56 minutos para ser exactos)\n• Traslación: 365 días y 6 horas (esas 6 horas extra se compensan agregando un día más cada cuatro años, llamado año bisiesto)",
                                                 image="https://static.nationalgeographic.es/files/styles/image_3200/public/940.jpg")
                    elif tema_elegido == "marte":
                        dispatcher.utter_message(text=f"Marte es un planeta desértico frío. Presenta un color rojizo debido al hierro oxidado en el suelo, lo que da a suponer que hubo agua abundante en este planeta. Tiene una atmósfera muy delgada compuesta por dióxido de carbono, nitrógeno y argón y una pequeño porcentaje de oxígeno y vapor de agua.\n• Radio: 3389,5 km\n• Número de satélites naturales: 2\n• Rotación: 24 horas y 36 minutos\n• Traslación: 687 días (1,88 años aprox.)",
                                                 image="https://img.freepik.com/foto-gratis/planeta-marte-cielo-estrellado-espacio-viajar-nueva-tierra-marte-estrellas_338491-7350.jpg")
                    elif tema_elegido == "jupiter":
                        dispatcher.utter_message(text=f"Júpiter es el planeta más grande del Sistema Solar. Es un gigante gaseoso, compuesto principalmente por hidrógeno y helio. También tiene anillos, pero estos son demasiado débiles para verlos bien. Su atmósfera es muy densa y es la de mayor tamaño de todos los plantes del Sistema Solar. Tiene grandes tormentas como la Gran Mancha Roja (con el doble de tamaño de la Tierra), que ha estado ocurriendo durante cientos de años y se está haciendo más grande y más rápida.\n• Radio: 69911 km\n• Número de satélites naturales: 79\n• Rotación: 9 horas y 50 minutos\n• Traslación: 4332 días (11,8 años aprox.)",
                                                 image="https://st.depositphotos.com/1034598/3528/i/600/depositphotos_35285169-stock-photo-planet-jupiter.jpg")
                    elif tema_elegido == "saturno":
                        dispatcher.utter_message(text=f"Saturno, al igual que Júpiter, también es un planeta gigante gaseoso, compuesto principalmente por hidrógeno y helio. Tiene el sistema de anillos más espectacular, con 7 anillos y varios huecos y divisiones entre ellos. Sus anillos están hechos de trozos de hielo y roca. En su atmósfera hay diversas bandas de aire, se han registrado tormentas y presencia de nubes de amoniaco.\n• Radio: 58232 km\n• Número de satélites naturales: 82\n• Rotación: 10 horas y 40 minutos\n• Traslación: 10.768 días (29,46 años aprox.)",
                                                 image="http://4.bp.blogspot.com/_EV6HxeajTt0/TSO8JK7OioI/AAAAAAAAAig/HhuUoiwLPx0/s1600/Saturno%2B01.jpg")
                    elif tema_elegido == "urano":
                        dispatcher.utter_message(text=f"Urano es un gigante de hielo con una atmósfera compuesta principalmente de hidrógeno (83%), helio (15%), metano (1,99%) y otros gases en menor proporción. El color azulado que presenta es debido al metano. Tiene 13 anillos conocidos, los interiores son estrechos y oscuros mientras que los exteriores son de colores brillantes y más fáciles de ver.  Al igual que Venus, Urano gira en dirección opuesta a la de la mayoría de los demás planetas. Y a diferencia de cualquier otro planeta, gira casi de lado ya que su eje de rotación está muy inclinado.\n• Radio: 25362 km\n• Número de satélites naturales: 27\n• Rotación: 17 horas y 14 minutos\n• Traslación: 30685 días (84 años aprox.)",
                                                 image="https://static.nationalgeographicla.com/files/styles/image_3200/public/STILL_B_1280x720_1514860611774.jpg")
                    elif tema_elegido == "neptuno":
                        dispatcher.utter_message(text=f"El gigante de hielo Neptuno es el planeta más distante del Sol perteneciente al Sistema Solar, por lo que es oscuro y frío. Su atmósfera es espesa y ventosa, con los vientos más fuertes de todos los planetas de nuestro sistema. Está compuesta principalmente por hidrógeno (80%), helio (19%), metano (1,5%) y otros gases en menor proporción. Neptuno también tiene anillos aunque estos son muy difíciles de ver.\n• Radio: 24622 km\n• Número de satélites naturales: 14\n• Rotación: 16 horas y 7 minutos\n• Traslación: 60225 días (164,88 años aprox.)",
                                                 image="https://spaceplace.nasa.gov/all-about-neptune/en/neptune3.en.jpg")
                    
                    # else:
                    #     dispatcher.utter_message(text=f"No disponible de momento.")
                    return[SlotSet("tema",tema_elegido)]
                else:
                    dispatcher.utter_message(text=f"Todavía no tenemos información de {tema_elegido}, por favor elija otro.")
                    return[SlotSet("tema",None)]



class ActionPregTest(Action):

    def name(self) -> Text:
        return "action_preguntas_test"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            ''' Abrir el archivo txt, contar el total de lineas '''
            nivel_elegido=tracker.get_slot("nivel")
            if nivel_elegido!=None:
                if nivel_elegido.lower() == "principiante":
                    nombre_fichero = "preg_principiante.txt"
                elif nivel_elegido.lower() == "avanzado":
                    nombre_fichero = "preg_avanzado.txt"
                else:
                    dispatcher.utter_message(text="No existe información para el nivel elegido. Vuelva a intentarlo.")
                    return[]
                with open(nombre_fichero) as myfile:
                    total_lineas = sum(1 for line in myfile)

                ''' numero de preguntas '''
                total_preguntas=total_lineas/5

                ''' hallar un numero aleatorio para lanzar pregunta aleatoria '''
                n_preg_seleccionada=random.randint(1,total_preguntas)
                n_linea_preg=(n_preg_seleccionada-1)*5+1

                preg_seleccionada=linecache.getline(nombre_fichero,n_linea_preg)
                resp1=linecache.getline(nombre_fichero,1+n_linea_preg)
                resp2=linecache.getline(nombre_fichero,2+n_linea_preg)
                resp3=linecache.getline(nombre_fichero,3+n_linea_preg)
                # solucion=linecache.getline(nombre_fichero,4+n_linea_preg)
                
                n_preguntas_seguidas=tracker.get_slot("preguntas_seguidas")
                n_preguntas_seguidas=n_preguntas_seguidas+1

                dispatcher.utter_message(text=f"Pregunta {n_preguntas_seguidas} / 5:")
                dispatcher.utter_message(text=preg_seleccionada, buttons = [
                                {"payload":resp1,"title":resp1},
                                {"payload":resp2,"title":resp2},
                                {"payload":resp3,"title":resp3},
                            ])
                

                return[SlotSet("n_pregunta",n_preg_seleccionada),SlotSet("preguntas_seguidas",n_preguntas_seguidas)]
            else:
                return[]

class ActionComprobarRespuesta(Action):

    def name(self) -> Text:
        return "action_comprobar_respuesta"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            nivel_elegido=tracker.get_slot("nivel")
            if nivel_elegido.lower() == "principiante":
                nombre_fich_resp = "resp_principiante.txt"
                nombre_fich_preg = "preg_principiante.txt"
            elif nivel_elegido.lower() == "avanzado":
                nombre_fich_resp = "resp_avanzado.txt"
                nombre_fich_preg = "preg_avanzado.txt"

            ''' hallar el nombre de la intencion en el ultimo mensaje'''
            state = tracker.current_state()
            intencion = state["latest_message"]["intent"]["name"]

            ''' hallar valores de slots'''
            n_preg_seleccionada=tracker.get_slot("n_pregunta")
            numero_correctos=tracker.get_slot("n_correctos")
            n_preg_seguidas=tracker.get_slot("preguntas_seguidas")

            if n_preg_seguidas==5:
                estado_preg="completo"
            else:
                estado_preg="incompleto"

            resp_correcta=linecache.getline(nombre_fich_resp,n_preg_seleccionada)
            user_respuesta=str(tracker.latest_message['text'])
            n_linea_solucion=((n_preg_seleccionada-1)*5+1)+4
            
            if intencion == "desconoce":
                solucion=linecache.getline(nombre_fich_preg,n_linea_solucion)
                dispatcher.utter_message(text=solucion)
            elif user_respuesta.lower() in resp_correcta.lower():
                numero_correctos=numero_correctos+1
                dispatcher.utter_message(text="¡Enhorabuena! Has elegido la respuesta correcta.")
            else:
                solucion=linecache.getline(nombre_fich_preg,n_linea_solucion)
                dispatcher.utter_message(text="Oh no, esa no era la respuesta correcta.")
                dispatcher.utter_message(text=solucion)

            return[SlotSet("n_correctos",numero_correctos),SlotSet("preg_completas",estado_preg)] 

class ActionNota(Action):

    def name(self) -> Text:
        return "action_nota"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            n_total_preg=tracker.get_slot("preguntas_seguidas")
            n_resp_correctas=tracker.get_slot("n_correctos")

            nota=n_resp_correctas/n_total_preg

            if nota == 1:
                dispatcher.utter_message(text=f"Has obtenido {n_resp_correctas} aciertos de {n_total_preg}. Enhorabuena, ¡estás en racha de aciertos! ")
            elif nota >= 0.5:
                dispatcher.utter_message(text=f"Has obtenido {n_resp_correctas} aciertos de {n_total_preg}. Muy bien, has superado la prueba, ¡pero practica más para obtener un 100% de aciertos! ")
            else:
                dispatcher.utter_message(text=f"Has obtenido {n_resp_correctas} aciertos de {n_total_preg}. Oh no...no has superado la prueba, deberías de estudiar más. ")

            
class VaciarNota(Action):

    def name(self) -> Text:
        return "action_vaciar_nota"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return[SlotSet("n_pregunta",0),SlotSet("preguntas_seguidas",0),SlotSet("n_correctos",0),SlotSet("preg_completas",None)]