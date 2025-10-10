def pattern_search(text, pattern):
    print(text)
    print(pattern)
    for i in range(len(text)):
        print('Text Index:', i)
        for j in range(len(pattern)):
            print(' Pattern Index:', j)
    pattern_search(text, pattern)


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
pattern_search(text, pattern)
