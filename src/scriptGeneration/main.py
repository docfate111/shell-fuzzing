import gramfuzz
import random
fuzzer = gramfuzz.GramFuzzer()
fuzzer.debug = True
fuzzer.load_grammar("specified.py")
#what should flags be?
code = list(fuzzer.gen(cat="start", num=10, max_recursion=20))
print("\n".join([x.decode('utf-8') for x in code]))
