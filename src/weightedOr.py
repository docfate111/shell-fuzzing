from gramfuzz.fields import *
from gramfuzz.utils import *
import myrandom
class NRef(Ref):
    cat = "word"
class NDef(Def):
    cat = "word"
class WeightedOr(Field):
    """A ``Field`` subclass that chooses one of the provided values at
    random as the result of a call to the ``build()`` method. Takes an
    odds array rather than just direct values."""
    def __init__(self, *values, **kwargs):
        '''
        values is a list of tuples
        '''
        self.shortest_vals = None
        vals=[x[0] for x in values]
        self.values= list(map(maybe_binstr, vals))
        self.weights = [x[1] for x in values]
        #print(self.weights)
        if abs(1.0 - sum(self.weights)) > 0.0001:
            raise("Weights in WeightedOr don't sum to 1.0: {}".format(self.weights))
        if "options" in kwargs and len(values) == 0:
            self.values = list(map(maybe_binstr, kwargs["options"]))
        self.rolling = kwargs.setdefault("rolling", False)
    def build(self, pre=None, shortest=False):
        """
        :param list pre: The prerequisites list
        :param bool shortest: Whether or not the shortest reference-chain (most minimal)
        version of the field should be generated.
        """
        #self.values=list(map(val, self.values))
        #self.shortest_vals=list(map(val, self.values))
        if pre is None:
            pre = []
        # self.shortest_vals will be set by the GramFuzzer and will
        # contain a list of value options that have a minimal reference chain
        if shortest and self.shortest_vals is not None:
            return utils.val(myrandom.choices(self.shortest_vals, self.weights)[0], pre, shortest=shortest)
        else:
            return utils.val(myrandom.choices(self.values, self.weights)[0], pre, shortest=shortest)
NDef("a", "a string")
NDef("B", NRef("a"))
NDef("c", "c string")
NDef("d", "d string")
y=Or(NRef("a"), NRef("B"), NRef("c"))
x=y=Or(NRef("a"), NRef("B"), NRef("c"))
x=WeightedOr(
    (NRef("c"), 0.25),
    (NRef("B"), 0.25),
    (NRef("a"), 0.25),
    (NRef("r"), 0.25)
)
NDef("r", WeightedOr(
    (NRef("r"), 0.25),
    (And(
        NRef("B"),
        NRef("r")
     ), 0.25),
    (NRef("B"), 0.25),
    (NRef("d"), 0.25)
))
#print(x)
#print(x.build())
assert(type(x.build())==bytes)
#print(y)
#print(y.build())
assert(type(y.build())==bytes)
