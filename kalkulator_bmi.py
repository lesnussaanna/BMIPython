# Program perhitungan BMI

print( "Perhitungan Body Mass Index (BMI)")
print("-----------------------------------")

berat_badan = input("Masukkan berat badan anda (kg):")
berat_badan = float(berat_badan)

tinggi_badan = input("Masukan tinggi badan anda (m):")
tinggi_badan = float(tinggi_badan)

bmi = berat_badan/(tinggi_badan**2)
berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

print(f"Nilai BMI anda adalah {bmi:.2f} kg/m^2")
print("Nilai BMI normal adalah 18.5 kg/m^2 - 25 kg/m^2")
print(f"Berat badan ideal anda adalah dalam rentang "
      f"{berat_badan_ideal['bawah']:.2f} kg - {berat_badan_ideal['atas']:.2f} kg")
print("-----------------------------------")
print("Terimakasih sudah menggunakan program ini :)")
