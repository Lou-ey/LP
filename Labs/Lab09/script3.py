def pattern_search(text, pattern):
    print(text)
    print(pattern)

    for i in range(len(text)):
        print('Text Index:', text[i])
        match_count = 0
        for j in range(len(pattern)):
            print('Pattern Index:', pattern[j])
            if pattern[j] == text[i + j]:
                print(f'Matching index found: {text[i + j]}')
                print("Match count:", match_count)
                match_count += 1
            else:
                print("No match found")
                break
        if match_count == len(pattern):
                print(f'{pattern} found at index {i}')


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
pattern_search(text, pattern)

text2 = "SOMEMORERANDOMWORDSTOpatternSEARCHTHROUGH"
pattern2 = "pattern"
text3 = "This still works with spaces"
pattern3 = "works"
text4 = "722615457824612704202682179992552072047396"
pattern4 = "42"

pattern_search(text2, pattern2)
pattern_search(text3, pattern3)
pattern_search(text4, pattern4)
