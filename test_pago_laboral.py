import unittest

from calcular_pago import calcular_pago_laboral


class TestCalcularPagoLaboral(unittest.TestCase):

    def test_jornada_completa_sin_extras(self):
        resultado = calcular_pago_laboral(1500000, 0, 0, 0, 0, "completa")
        self.assertEqual(resultado["pago_jornada"], 50000.0)

    def test_jornada_media_sin_extras(self):
        resultado = calcular_pago_laboral(1500000, 0, 0, 0, 0, "media")
        self.assertEqual(resultado["pago_jornada"], 25000.0)

    def test_valor_hora_correcto(self):
        resultado = calcular_pago_laboral(1500000, 0, 0, 0, 0, "completa")
        self.assertEqual(resultado["valor_hora"], 6250.0)

    def test_valor_dia_correcto(self):
        resultado = calcular_pago_laboral(1500000, 0, 0, 0, 0, "completa")
        self.assertEqual(resultado["valor_dia"], 50000.0)

    def test_extra_diurna(self):
        resultado = calcular_pago_laboral(1500000, 2, 0, 0, 0, "completa")
        self.assertEqual(resultado["pago_extra_diurna"], 15625.0)

    def test_extra_nocturna(self):
        resultado = calcular_pago_laboral(1500000, 0, 1, 0, 0, "completa")
        self.assertEqual(resultado["pago_extra_nocturna"], 10937.5)

    def test_extra_festiva_diurna(self):
        resultado = calcular_pago_laboral(1500000, 0, 0, 2, 0, "completa")
        self.assertEqual(resultado["pago_extra_festiva_diurna"], 25000.0)

    def test_extra_festiva_nocturna(self):
        resultado = calcular_pago_laboral(1500000, 0, 0, 0, 2, "completa")
        self.assertEqual(resultado["pago_extra_festiva_nocturna"], 31250.0)

    def test_total_pago_completo(self):
        resultado = calcular_pago_laboral(1500000, 1, 1, 1, 1, "completa")
        total = resultado["total_pago"]
        self.assertAlmostEqual(total, 50000 + 7812.5 + 10937.5 + 12500 + 15625, places=2)

    def test_total_pago_media(self):
        resultado = calcular_pago_laboral(1500000, 1, 1, 1, 1, "media")
        total = resultado["total_pago"]
        self.assertAlmostEqual(total, 25000 + 7812.5 + 10937.5 + 12500 + 15625, places=2)

    def test_tipo_jornada_invalido(self):
        with self.assertRaises(ValueError):
            calcular_pago_laboral(1500000, 0, 0, 0, 0, "invalido")

    def test_salario_minimo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_pago_laboral(-1500000, 0, 0, 0, 0, "completa")

    def test_horas_extra_negativas(self):
        with self.assertRaises(ValueError):
            calcular_pago_laboral(1500000, -1, 0, 0, 0, "completa")

    def test_todo_en_cero(self):
        resultado = calcular_pago_laboral(1500000, 0, 0, 0, 0, "completa")
        self.assertEqual(resultado["total_pago"], resultado["pago_jornada"])

    def test_total_pago_redondeado(self):
        resultado = calcular_pago_laboral(1500000, 1, 1, 1, 1, "completa")
        self.assertIsInstance(resultado["total_pago"], float)
        self.assertEqual(round(resultado["total_pago"], 2), resultado["total_pago"])


if __name__ == '__main__':
    unittest.main()
