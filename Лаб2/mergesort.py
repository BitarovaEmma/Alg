import numpy
import time
import random


def generate_array(size):
    output = []
    for i in range(size):
        output.append(random.uniform(-1, 1))
    return numpy.array(output)


def merge_sort(input, height=0, memory=0):
    height += 1
    size = len(input)
    if size <= 1:
        return [input, height, memory]
    size_left = int(size // 2)

    left = merge_sort(numpy.array(input[:size_left]), height, memory)
    right = merge_sort(numpy.array(input[size_left:]), height, memory)

    height = max(left[1], right[1])
    left = left[0]
    right = right[0]
    memory += left.nbytes + right.nbytes
    c_left = c_right = 0
    output = numpy.ones(size)
    
    while c_left < size_left and c_right < size - size_left:
        if left[c_left] < right[c_right]:
            output[c_left + c_right] = left[c_left]
            c_left += 1
        else:
            output[c_left + c_right] = right[c_right]
            c_right += 1

    while c_left < size_left:
        output[c_left + c_right] = left[c_left]
        c_left += 1

    while c_right < size - size_left:
        output[c_left + c_right] = right[c_right]
        c_right += 1
        
    del (left)
    del (right)
    return [output, height, memory]

def main():
    sizes = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]
    num = 20
    for i in sizes:
        times = []
        recursions = []
        memories = []
        for j in range(num):
            cur = generate_array(i)

            start_time = time.time()
            sorted = merge_sort(cur)
            working_time = time.time() - start_time

            height = sorted[1]
            memory = round(sorted[2] / 1024 / 1024, 2)
            sorted = sorted[0]

            times.append(working_time)
            recursions.append(height)
            memories.append(memory)

            print("%d №%d, время - %.4f, высота рекурсии - %d, доп память(МБ) %.4f" % (i, j + 1, working_time, height, memory))

            if i <= 4000:
                for k in range(len(sorted) - 1):
                    if sorted[k] > sorted[k + 1]:
                        print("Ошибка")
                        break
            del (sorted)

        cur_avg_time = sum(times) / num
        cur_avg_rec = sum(recursions) / num
        cur_avg_mem = sum(memories) / num
        print(("%d среднее время %.4f, лучшее - %.4f, худшее - %.4f" % (i, cur_avg_time, min(times), max(times))).replace('.', ','))
        print(("%d среднее высота рекурсии %.4f, лучшее - %.4f, худшее - %.4f" % (i, cur_avg_rec, min(recursions), max(recursions))).replace('.', ','))
        print(("%d средняя доп память %.4f, лучшая - %.4f, худшая - %.4f" % (i, cur_avg_mem, min(memories), max(memories))).replace('.', ','))
        

if __name__ == "__main__":
    main()
