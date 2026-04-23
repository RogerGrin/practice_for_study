#include <iostream>

using namespace std;

int binary_search(int* array, int n, int k) {
    
    int lower_index = -1;
    int upper_index = n;
    int result_index = -1;

    while (upper_index - lower_index > 1) {
        int middle_index = (upper_index + lower_index) / 2;
        if (k > array[middle_index]) {
            lower_index = middle_index;
        }
        else if (k < array[middle_index]) {
            upper_index = middle_index;
        }
        else if (k == array[middle_index]) {
            return middle_index;
        }
    }
    
    return -1;
    
}

int main()
{
    setlocale(LC_ALL, "rus");
    int n, k;
    cout << "введите количество элементов в массиве: ";
    cin >> n;
    cout << "введите элемент который нужно найти: ";
    cin >> k;

    int* array = new int[n];

    // для примера
    for (int i = 0; i < n; i++) {
        array[i] = i + 100;
    }

    cout << "это изменения для проверки!" << endl;

    cout << binary_search(array, n, k) << endl;

    return 0;
}