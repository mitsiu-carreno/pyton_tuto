import sys

def count_words(str):
	world_count =0
	i=0
	in_word = False

	while i < len(str):
		c=str[i]
		is_word_char = (c >="a" and c<="z") or (c >="A" and c<="Z")
		if in_word:
			if not is_word_char:
				in_word = False
		else:
			if is_word_char:
				in_word = True
				world_count +=1
		i+=1
	return world_count

def main():
	line_count = 0
	world_count =0
	byte_count =0

	while True:
		line= sys.stdin.readline()
		if not line:
			break
		byte_count += len(line)
		line_count += 1
		world_count += count_words(line)

	sys.stdout.write("%d words, %d lines, %d bytes\n" %
						(world_count, line_count, byte_count))

main()