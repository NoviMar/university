using System;
using System.Threading.Tasks;

class Node
{
    public int Data { get; set; }
    public Node Next { get; set; }

    public Node(int data)
    {
        Data = data;
        Next = null;
    }
}

class LinkedList
{
    public Node Head { get; set; }

    public void Append(int data)
    {
        Node newNode = new Node(data);
        if (Head == null)
        {
            Head = newNode;
            return;
        }

        Node lastNode = Head;
        while (lastNode.Next != null)
        {
            lastNode = lastNode.Next;
        }

        lastNode.Next = newNode;
    }

    public void SortList()
    {
        if (Head == null)
        {
            return;
        }

        bool swapped;
        do
        {
            Node currentNode = Head;
            swapped = false;
            while (currentNode.Next != null)
            {
                if (currentNode.Data > currentNode.Next.Data)
                {
                    int temp = currentNode.Data;
                    currentNode.Data = currentNode.Next.Data;
                    currentNode.Next.Data = temp;
                    swapped = true;
                }
                currentNode = currentNode.Next;
            }
        } while (swapped);
    }

    public void PrintList()
    {
        Node currentNode = Head;
        while (currentNode != null)
        {
            Console.Write(currentNode.Data + " ");
            currentNode = currentNode.Next;
        }
        Console.WriteLine();
    }

    public Node Merge(Node secondHead)
    {
        if (Head == null)
        {
            return secondHead;
        }

        if (secondHead == null)
        {
            return Head;
        }

        LinkedList mergedList = new LinkedList();
        Node currentNode1 = Head;
        Node currentNode2 = secondHead;

        if (currentNode1.Data <= currentNode2.Data)
        {
            mergedList.Head = currentNode1;
            currentNode1 = currentNode1.Next;
        }
        else
        {
            mergedList.Head = currentNode2;
            currentNode2 = currentNode2.Next;
        }

        Node mergedNode = mergedList.Head;

        while (currentNode1 != null && currentNode2 != null)
        {
            if (currentNode1.Data <= currentNode2.Data)
            {
                mergedNode.Next = currentNode1;
                currentNode1 = currentNode1.Next;
            }
            else
            {
                mergedNode.Next = currentNode2;
                currentNode2 = currentNode2.Next;
            }
            mergedNode = mergedNode.Next;
        }

        if (currentNode1 != null)
        {
            mergedNode.Next = currentNode1;
        }
        else if (currentNode2 != null)
        {
            mergedNode.Next = currentNode2;
        }

        return mergedList.Head;
    }
}

class Program
{
    static void Main()
    {
        LinkedList list1 = new LinkedList();
        Console.Write("Введите длину первого списка: ");
        int lengthFirst = int.Parse(Console.ReadLine());
        Random random = new Random();
        for (int i = 0; i < lengthFirst; i++)
        {
            list1.Append(random.Next(-50, 50));
        }

        LinkedList list2 = new LinkedList();
        Console.Write("Введите длину второго списка: ");
        int lengthSecond = int.Parse(Console.ReadLine());
        for (int i = 0; i < lengthSecond; i++)
        {
            list2.Append(random.Next(-50, 50));
        }

        Task task1 = Task.Run(() =>
        {
            list1.SortList();
            list1.PrintList();
        });

        Task task2 = Task.Run(() =>
        {
            list2.SortList();
            Console.WriteLine();
            list2.PrintList();
        });

        Task.WaitAll(task1, task2);

        list1.Head = list1.Merge(list2.Head);
        Console.WriteLine("Объединенный список:");
        list1.PrintList();
    }
}
