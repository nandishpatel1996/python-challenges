def tribonacci(signature, n):
	tribonacci_list = []
	if n <= len(signature):return signature[:n]
	else:
		tribonacci_list.extend(signature)
		while n > len(tribonacci_list):tribonacci_list.append(sum(tribonacci_list[-3:]))
		return tribonacci_list


print(tribonacci([0, 0, 0], 10))