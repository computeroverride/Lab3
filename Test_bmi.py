import Lab2.bmi as bmi

def test_bmi_normal_weight():
    # Example: weight=60kg, height=1.7m → BMI ≈ 20.76
    result = bmi.calculate_bmi(1.7, 60)
    assert result == 0

def test_bmi_over_weight():
    # Example: weight=90kg, height=1.7m → BMI ≈ 31.14
    result = bmi.calculate_bmi(1.7, 90)
    assert result == 1

def test_bmi_under_weight():
    # Example: weight=40kg, height=1.7m → BMI ≈ 13.8
    result = bmi.calculate_bmi(1.7, 40)
    assert result == -1