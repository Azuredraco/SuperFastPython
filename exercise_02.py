from multiprocessing import Pool, active_children, cpu_count

if __name__ == "__main__":
    print("\nDefault configuration:")
    with Pool() as pool:
        print(f"\tnumber of processes = {len(active_children())}")

    print("\nNumber of physical cores configuration:")
    with Pool(cpu_count()//2) as pool:
        print(f"\tnumber of processes = {cpu_count()//2}")
