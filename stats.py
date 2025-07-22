def word_count(text):
        words = text.split()
        num_words = len(words)
        print(f"Found {num_words} total words")
def char_count(text):
	characters = {}
	lowercase = text.lower()
	for character in lowercase:
		if character.isalpha() == False:
			continue
		if character in characters:
			characters[character] += 1
		else:
			characters[character] = 1
	sorted_chars = sorted(characters.items(), key=lambda x: x[1], reverse=True)
	for char, count in sorted_chars:
		print(f"{char}: {count}")
