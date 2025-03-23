from database import agregar_nota, obtener_notas

class Nota:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def guardar(self):
        agregar_nota(self.titulo, self.contenido)

    @staticmethod
    def listar_notas():
        return obtener_notas()
