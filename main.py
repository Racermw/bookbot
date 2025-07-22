def get_book_text(filepath):
	with open(filepath) as f:
		contents = f.read()
		return contents
def main():
	import sys
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		return sys.exit(1)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}")
	book_text = get_book_text(sys.argv[1])
	from stats import word_count
	print("----------- Word Count ----------")
	word_count(book_text)
	from stats import char_count
	print("--------- Character Count -------")
	char_count(book_text)
	print("============= END ===============")
main()

