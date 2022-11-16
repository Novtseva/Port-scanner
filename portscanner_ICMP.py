import pyping

target = input('What do you want to scan?: ')

print('Starting scan on host:', target_ip)
start = time.time()

r = pyping.ping(target)

if r.ret_code == 0:
    print("Success")
else:
    print("Failed with {}".format(r.ret_code))


end = time.time()
print(f'Time taken {end-start:.2f} seconds')