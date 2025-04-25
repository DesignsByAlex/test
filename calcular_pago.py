def calcular_pago_laboral(
    salario_minimo: float,
    horas_extras_diurnas: int,
    horas_extras_nocturnas: int,
    horas_extras_festivas_diurnas: int,
    horas_extras_festivas_nocturnas: int,
    tipo_jornada: str  # "media" o "completa"
) -> dict:

    if salario_minimo <= 0:
        raise ValueError("El salario mínimo debe ser un valor positivo.")
    if any(h < 0 for h in [horas_extras_diurnas, horas_extras_nocturnas, horas_extras_festivas_diurnas, horas_extras_festivas_nocturnas]):
        raise ValueError("Las horas extra no pueden ser negativas.")

    # Valores base
    dias_laborales_mes = 30
    horas_laborales_dia = 8
    horas_laborales_mes = dias_laborales_mes * horas_laborales_dia

    valor_hora = salario_minimo / horas_laborales_mes
    valor_dia = salario_minimo / dias_laborales_mes

    # Recargos en Colombia
    recargo_extra_diurna = 1.25
    recargo_extra_nocturna = 1.75
    recargo_festiva_diurna = 2.0
    recargo_festiva_nocturna = 2.5

    # Cálculo de horas extra
    pago_extra_diurna = horas_extras_diurnas * valor_hora * recargo_extra_diurna
    pago_extra_nocturna = horas_extras_nocturnas * valor_hora * recargo_extra_nocturna
    pago_extra_festiva_diurna = horas_extras_festivas_diurnas * valor_hora * recargo_festiva_diurna
    pago_extra_festiva_nocturna = horas_extras_festivas_nocturnas * valor_hora * recargo_festiva_nocturna

    # Cálculo de jornada
    if tipo_jornada == "media":
        pago_jornada = valor_dia / 2
    elif tipo_jornada == "completa":
        pago_jornada = valor_dia
    else:
        raise ValueError("Tipo de jornada inválido. Usa 'media' o 'completa'.")

    return {
        "valor_hora": round(valor_hora, 2),
        "valor_dia": round(valor_dia, 2),
        "pago_jornada": round(pago_jornada, 2),
        "pago_extra_diurna": round(pago_extra_diurna, 2),
        "pago_extra_nocturna": round(pago_extra_nocturna, 2),
        "pago_extra_festiva_diurna": round(pago_extra_festiva_diurna, 2),
        "pago_extra_festiva_nocturna": round(pago_extra_festiva_nocturna, 2),
        "total_pago": round(
            pago_jornada + 
            pago_extra_diurna + 
            pago_extra_nocturna + 
            pago_extra_festiva_diurna + 
            pago_extra_festiva_nocturna, 2
        )
    }

resultado = calcular_pago_laboral(
    salario_minimo=1500000,  # pesos colombianos
    horas_extras_diurnas=2,
    horas_extras_nocturnas=1,
    horas_extras_festivas_diurnas=0,
    horas_extras_festivas_nocturnas=1,
    tipo_jornada="completa"
)

print(resultado)
