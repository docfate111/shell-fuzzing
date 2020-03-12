from gramfuzz.fields import *
from gramfuzz.utils import *
import random
class NRef(Ref):
    cat = "word"
class NDef(Def):
    cat = "word"
class WeightedOr(Field):
    """A ``Field`` subclass that chooses one of the provided values at
    random as the result of a call to the ``build()`` method. Takes an
    odds array rather than just direct values."""
    def __init__(self, *odds, **kwargs):
        """Create a new ``WeightedOr`` instance with the provide values
        :param list values: The list of (odds, value) pairs to choose randomly from
        """
        # when building with shortest=True, one of these values will
        # be chosen instead of self.values
        '''
          self.shortest_vals = None
        self.values = list(map(maybe_binstr, values))
        if "options" in kwargs and len(values) == 0:
            self.values = list(map(maybe_binstr, kwargs["options"]))
        self.rolling = kwargs.setdefault("rolling", False)
        '''
        self.shortest_vals = None
        values=[x[0] for x in odds]
        self.values= list(map(maybe_binstr, values))
        #list(map(maybe_binstr, values))
        self.weights = [x[1] for x in odds]
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
        self.values=list(map(val, self.values))
        self.shortest_vals=list(map(val, self.values))
        if pre is None:
            pre = []
        # self.shortest_vals will be set by the GramFuzzer and will
        # contain a list of value options that have a minimal reference chain
        if shortest and self.shortest_vals is not None:
            return utils.val(random.choices(self.shortest_vals, self.weights), pre, shortest=shortest)
        else:
            return utils.val(random.choices(self.values, self.weights), pre, shortest=shortest)

NDef("a", "a string")
NDef("B", "b string")
NDef("c", "c string")
y=Or(NRef("a"), NRef("B"), NRef("c"))
x=WeightedOr((NRef("c"), 0.4), (NRef("a"),0.2), (NRef("B"), 0.4))
print(x)
print(x.build())
print(y)
print(y.build())
