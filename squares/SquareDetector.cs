using System.Collections.Generic;

static class SquareDetector
{
    static IEnumerable<int> Count()
    {
        int current = 0;
        while (true)
            yield return current++;
    }

    static IEnumerable<long> Accumulate(this IEnumerable<int> source)
    {
        long sum = 0;
        foreach(int i in source)
        {
            sum += i;
            yield return sum;
        }
    }

    /// <summary>Determines whether the given integer is a perfect square.</summary>
    static bool IsSquare(int n) =>
        n < 0 ? false :
        n == 0 ? true :
        Count().Where(i => (i & 1) == 1).Accumulate().TakeWhile(s => s <= n).Contains(n);

    static void Main(string[] args)
    {
        int input;
        if (args.Length < 1 || !int.TryParse(args[0], out input))
        {
            Console.WriteLine("Please provide a numeric argument.");
            return;
        }
        if (IsSquare(input))
            Console.WriteLine($"{input} is a square.");
        else
            Console.WriteLine($"{input} is not a square.");
    }
}