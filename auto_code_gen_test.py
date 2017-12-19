
from linq import Flow
import linq.standard
Flow([1, 2, 3]).Unboxed()
Flow([1, 2, 3]).Sum(lambda x: x)
Flow([1, 2, 3]).Enum()
Flow([1, 2, 3]).Map(lambda x: x)
Flow([1, 2, 3]).Then(lambda x: x)
Flow([1, 2, 3]).Reduce(lambda x, y: x+y)
Flow([1, 2, 3]).Filter(lambda x: x)
Flow([1, 2, 3]).Each(lambda x: x)
Flow([1, 2, 3]).Aggregate(lambda x: x)
Flow([1, 2, 3]).Zip([1, 2])
Flow([1, 2, 3]).Sorted(lambda x: x)
Flow([1, 2, 3]).ArgSorted(lambda x: x)
Flow([1, 2, 3]).Group(lambda x: x)
Flow([1, 2, 3]).GroupBy(lambda x: x)
Flow([1, 2, 3]).Take(1)
Flow([1, 2, 3]).TakeIf(lambda x: x)
Flow([1, 2, 3]).TakeWhile(lambda x: x)
Flow([1, 2, 3]).Drop(1)
Flow([1, 2, 3]).Concat([1, 2])
Flow([1, 2, 3]).ToList()
Flow([1, 2, 3]).ToTuple()
Flow([(1, 1), (2, 2), (3, 3)]).ToDict()
Flow([1, 2, 3]).ToSet()
Flow([1, 2, 3]).All(lambda x: x)
Flow([1, 2, 3]).Any(lambda x: x)
Flow([1, 2, 3]).Extended([1, 2])
Flow([1, 2, 3]).Extend([1, 2])
Flow([1, 2, 3]).Sort(lambda x: x)
Flow([1, 2, 3]).Reverse()
Flow([1, 2, 3]).Reversed()
Flow({1, 2, 3}).Intersects([1, 2])
