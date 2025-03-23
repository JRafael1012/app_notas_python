import database

def test_agregar_nota():
    database.agregar_nota("Prueba", "Esto es una prueba")
    notas = database.obtener_notas()
    assert any(nota[1] == "Prueba" for nota in notas), "Error al agregar nota"

def test_eliminar_nota():
    notas = database.obtener_notas()
    if notas:
        database.eliminar_nota(notas[0][0])
        nuevas_notas = database.obtener_notas()
        assert notas[0] not in nuevas_notas, "Error al eliminar nota"

test_agregar_nota()
test_eliminar_nota()
print("Todas las pruebas pasaron correctamente.")
