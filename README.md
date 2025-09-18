# Algoritme[c++.cpp](https://github.com/user-attachments/files/22409958/c%2B%2B.cpp)
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <list>

int main() {
    // Создание списка строк
    std::list<std::string> string_list = {"apple", "banana", "cherry", "date"};
    
    // Добавление элементов в список
    string_list.push_back("elderberry");
    string_list.push_front("apricot");
    
    // Организация очереди
    std::queue<double> number_queue;
    
    // Добавление элементов в очередь
    number_queue.push(10.5);    // [10.5]
    number_queue.push(20.3);    // [10.5, 20.3]
    number_queue.push(30.7);    // [10.5, 20.3, 30.7]
    number_queue.push(40.1);    // [10.5, 20.3, 30.7, 40.1]
    
    // Удаление из очереди
    double front_element = number_queue.front();  // получаем первый элемент
    number_queue.pop();                          // удаляем его из очереди
    
    std::cout << "Первый элемент очереди: " << front_element << std::endl;
    std::cout << "Размер очереди после pop: " << number_queue.size() << std::endl;
    std::cout << "Следующий элемент в очереди: " << number_queue.front() << std::endl;
    
    // Вывод элементов списка
    std::cout << "\nЭлементы списка: ";
    for (const auto& fruit : string_list) {
        std::cout << fruit << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
