#include <iostream>
#include <vector>
#include <cmath>

#define TAM 1000

using namespace std;

int main() {
    int resultado = 0;

    for (int i = 0; i < TAM; i++) {
        vector<int> a;
        while (true) {
            int valor;
            cin >> valor; // Usando cin para ler o valor inteiro
            a.push_back(valor);

            char c;
            cin.get(c); // Usando cin.get() para ler o caractere de controle (enter)

            if (c == '\n') break; // Sai do loop quando uma linha é completada
        }

        bool verifica = true; // Inicializando a variável 'verifica'
        bool crescente = true;
        bool decrescente = true;
        int tam = int(a.size()) - 1;

        for (int j = 0; j < tam; j++) {
            int diff = a[j + 1] - a[j];
            if (diff > 0) {
                decrescente = false;
            }
            if (diff < 0) {
                crescente = false;
            }
            if (abs(diff) > 3) { // Verificando se a diferença é maior que 3
                verifica = false;
                break;
            }
        }

        if (verifica && (crescente || decrescente)) {
            resultado++;
        }
    }

    cout << resultado << endl;

    return 0;
}
