# Даланкинова Эмма Бпи205
# Вариант 1 и 14
# перед запуском надо скачать библиотеку pip install memory_profiler
import read_write
from shell_sorting import shell_sort_by_area
import sys
import memory_profiler

if __name__ == '__main__':
    args = sys.argv
    input_file = args[1]
    output_file = args[2]
    fig_list = read_write.read_info(input_file)
    mem_used = memory_profiler.memory_usage((shell_sort_by_area, (fig_list[:],), {}))
    fig_list, result_time = shell_sort_by_area(fig_list)
    print('Максимально использовано памяти -', max(mem_used), 'MiB')
    print('Времени затрачено -', result_time, 'сек.')
    read_write.write_info(args, fig_list, output_file)
