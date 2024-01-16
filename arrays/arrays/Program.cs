using System;
using System.Linq.Expressions;

class Class1
{
    static void Main(string[] args)
    {
        Console.Write("Введите количество элементов массива:\t");
        int SizeArray = Convert.ToInt32(Console.ReadLine());
        decimal[] array = new decimal[SizeArray];

        for (int i = 0; i < array.Length; i++)
        {
            Console.Write($"\n Введите элемент под индексом {i}:\t ");
            array[i] = Convert.ToDecimal(Console.ReadLine());
        }

        Console.Write($"\nВведите крайнее число:\t");
        int El = Convert.ToInt32(Console.ReadLine());

        decimal[] FirstResult = new decimal[0];
        foreach (int num in array)
        {
            if (num > El)
            {
                Array.Resize(ref FirstResult, FirstResult.Length + 1);
                FirstResult[FirstResult.Length - 1] = num;
            }
        }

        int FirstCount = 0;
        Console.WriteLine($"\n Размер первого массива:\t{FirstResult.Length}");
        do
        {
            Console.Write($"\n Элементы первого массива:\t{FirstResult[FirstCount]}");
            FirstCount++;
        }
        while (FirstCount < FirstResult.Length);
        Console.Write($"\n");

        decimal[] SecondResult = Array.FindAll(array, i => i > El);

        int SecondCount = 0;
        Console.WriteLine($"\n Размер второго массива:\t{SecondResult.Length}");
        while (SecondCount < SecondResult.Length)
        {
            Console.Write($"\n Элементы второго массива:\t{SecondResult[SecondCount]}");
            SecondCount++;
        }
    }
}
