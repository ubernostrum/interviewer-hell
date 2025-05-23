namespace SquareDetector;

internal static class SquareDetector
{
    private static IEnumerable<int> Count()
    {
        var current = 0;
        while (true)
            yield return current++;
    }

    private static IEnumerable<long> Accumulate(this IEnumerable<int> source)
    {
        long sum = 0;
        foreach (var i in source)
        {
            sum += i;
            yield return sum;
        }
    }

    /// <summary>
    /// Determine whether the given value is a perfect square.
    /// </summary>
    /// <param name="n">The value to check.</param>
    /// <returns>Whether the given value is a perfect square.</returns>
    private static bool IsSquare(int n) =>
        n >= 0 && (n == 0 || Count().Where(i => (i & 1) == 1).Accumulate().TakeWhile(s => s <= n).Contains(n));

    private static void Main(string[] args)
    {
        if (args.Length < 1 || !int.TryParse(args[0], out var input))
        {
            Console.WriteLine("Please provide a numeric argument.");
            return;
        }

        Console.WriteLine(IsSquare(input) ? $"{input} is a square." : $"{input} is not a square.");
    }
}