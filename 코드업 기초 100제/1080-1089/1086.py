# 1086 : [기초-종합] 그림 파일 저장용량 계산하기

w, h, b = map(int, input().split())

file_size_in_bits = w * h * b
file_size_in_mega_bytes = file_size_in_bits / (8 * 1024 * 1024)

print("%0.2f MB" % file_size_in_mega_bytes)

