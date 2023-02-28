# Vehicle purchase decision support system

## GUI appearance

<p align="center">
  <img src="https://user-images.githubusercontent.com/64035334/221970084-67a0c743-e303-4ca4-9263-03d5e40ac6a6.png">
</p>


## Method implementation

### Metoda Topsis:

Metoda opiera się na koncepcji wyboru alternatywy na podstawie najkrótszej odległości euklidesowej od rozwiązania idealnego oraz najdłuższej odległości od rozwiązania antyidealnego.
Zatem porównujemy zestaw alternatyw, normalizujemy wyniki dla każdego z kryterium i obliczamy odległości geometryczne między każdą alternatywą i idealną alternatywą.

![image](https://user-images.githubusercontent.com/64035334/221970931-aeb7b7c1-809e-4c0f-b0bb-4046f17e87eb.png)

### Metoda RSM:

Metoda jest w pewnym sensie podobna do Topsis, tylko zamiast liczenia odległości od punktu idealnego i anty - idealnego sortujemy w ranking wartości funkcji  scoringowych opartych na obliczaniu odległości od zbioru punktów docelowych oraz punktów anty - idealnych odniesienia

![image](https://user-images.githubusercontent.com/64035334/221971475-748a08ee-57cf-4082-af5b-4bdf5bd3d44f.png)

![image](https://user-images.githubusercontent.com/64035334/221971844-343b0633-2c63-4987-ac5c-47412e1ac82a.png)

![image](https://user-images.githubusercontent.com/64035334/221971971-ed1d1ecb-b1d2-4715-b4f9-50355c69664b.png)
