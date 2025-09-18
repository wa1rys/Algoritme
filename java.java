import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class QueueExample {
    public static void main(String[] args) {
        // Создание связанного списка
        List<String> linkedList = new LinkedList<>();
        linkedList.add("first");
        linkedList.add("second");
        linkedList.add("third");
        
        // Добавление элементов в начало и конец списка
        ((LinkedList<String>) linkedList).addFirst("start");
        ((LinkedList<String>) linkedList).addLast("end");

        // Организация очереди
        Queue<Double> queue = new LinkedList<>();

        // Добавление в очередь
        queue.offer(10.5);    // [10.5]
        queue.offer(20.3);    // [10.5, 20.3]
        queue.offer(30.7);    // [10.5, 20.3, 30.7]
        queue.offer(40.1);    // [10.5, 20.3, 30.7, 40.1]

        // Удаление из очереди
        Double frontElement = queue.poll();  // возвращает 10.5, queue = [20.3, 30.7, 40.1]

        System.out.println("Первый элемент очереди: " + frontElement);
        System.out.println("Размер очереди после poll: " + queue.size());
        System.out.println("Следующий элемент в очереди: " + queue.peek());
        
        // Вывод элементов связанного списка
        System.out.println("\nЭлементы связанного списка:");
        for (String element : linkedList) {
            System.out.print(element + " ");
        }
        System.out.println();
        
        // Дополнительные операции с очередью
        System.out.println("Очередь пустая? " + queue.isEmpty());
        System.out.println("Текущий размер очереди: " + queue.size());
    }
}