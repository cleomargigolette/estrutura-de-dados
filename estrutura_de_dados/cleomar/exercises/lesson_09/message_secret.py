from app import lib


queue_int = lib.Queue()
queue_string = lib.Queue()
string_decoded = ""

list_int = [3, 5, 2, 4, 3, 4, 4, 2, 3, 3, 4, 3, 3, 7]
string_intercepted = "ojrggcfetscrapeooukeszwtteaof-dbcobteqrrjttsmfslua"
indice = 0

for item_int in list_int:
    queue_int.enqueue(item_int)
    
for item in range(len(list_int)):
    
    int_dequeue = int(queue_int.dequeue()-1) + indice
    
    string_decoded = string_decoded + string_intercepted[int_dequeue]
    indice = int_dequeue + 1

print(string_decoded)