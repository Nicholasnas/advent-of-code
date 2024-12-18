#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <list>


using namespace std;

const int TAM = 1000;

int main(){

    vector<int>lista1, lista2;
    list<int>a,b;

    int num1, num2;

    for(int i = 0; i<TAM; i++){
        cin >> num1 >> num2;
        lista1.push_back(num1);
        lista2.push_back(num2);
    }

    sort(lista1.begin(), lista1.end());
    sort(lista2.begin(), lista2.end());

    long int resultado = 0;

    for(int i=0;i<TAM;i++){
        resultado += abs(lista1[i]- lista2[i]);
    }
    cout << resultado << endl; //3714264

    long int soma = 0;
    int cont[1000];
    for(int i=0;i<TAM;i++){
        cont[i] = 0;
    }

    for(int i=0;i<TAM;i++){
        for(int j=0;j<TAM;j++){
            if(lista1[i] == lista2[j]){
                cont[i] += 1;
            }
        }
        soma += lista1[i] * cont[i];
    }
    cout << "Segunda parte: " << soma << endl; // 18805872

    return 0;
}