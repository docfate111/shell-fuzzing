import gramfuzz
import random
fuzzer = gramfuzz.GramFuzzer()
fuzzer.debug = True
fuzzer.load_grammar("specified.py")
#what should flags be?
code = list(fuzzer.gen(cat="start", num=random.randint(0, 100), max_recursion=random.randint(0, 50)))
print("\n".join([x.decode('utf-8') for x in code]))
