def calculate_hash_sum(filename):
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = lines[:-1]
    with open(filename, 'w') as f:
        f.writelines(lines)    
        
    with open(filename, 'rb') as f:
        data = f.read()
        mas=[]
        size_const = 4
        for i in range(0, len(data), size_const):
            block=data[i:i+size_const]
            if len(block)< size_const:
                chisl = b'\x00' * (size_const - len(block))
                block = chisl + block
            mas.append(block)
            
        sum_ = 0
        
        for i in mas:
            num =int(''.join(format(byte, '08b') for byte in i), 2)
            sum_+=num
            
        sum_=bin(sum_)[-32:]
        print(sum_)
        
        with open(filename, 'a') as f2:
            f2.write(f'{sum_}')

calculate_hash_sum("example.txt")
