import gramfuzz
fuzzer = gramfuzz.GramFuzzer()
#fuzzer.debug = True
fuzzer.load_grammar("words.py")
code = list(fuzzer.gen(cat="program", num=50))
# or like this if GRAMFUZZ_TOP_LEVEL_CAT="name" was defined in the
# names_grammar.py file:
#     names = fuzzer.gen(cat_group="names_grammar", num=10)
print("\n".join([x.decode('utf-8') for x in code]))
