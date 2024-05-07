Lista = ['red', 'green', 'blue']
Listb = ['#FF0000','#008000', '#0000FF']

hasil = {}
for Lista, Listb in zip(Lista, Listb):
    hasil[Lista] = Listb
    
print(f"hasilnya {hasil}")